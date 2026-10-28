# downloader

_Kaynak: scanner\downloader.py - 230 satir_

```python
"""
URL'den JAR dosyası indirme modülü
GitHub ve doğrudan bağlantıları destekler
GitHub repo URL'lerinden otomatik JAR bulma
"""

import os
import tempfile
import urllib.request
import urllib.parse
import json
import re
from pathlib import Path
from typing import List, Dict


class JarDownloader:
    """JAR dosyalarını URL'den indiren sınıf"""
    
    @staticmethod
    def is_url(path: str) -> bool:
        """Verilen string bir URL mi kontrol et"""
        return path.startswith('http://') or path.startswith('https://')
    
    @staticmethod
    def is_github_repo(url: str) -> bool:
        """
        URL bir GitHub repository mi yoksa direkt dosya mı?
        
        Repo: https://github.com/user/repo
        Dosya: https://github.com/user/repo/releases/download/.../file.jar
        """
        # Releases/download, blob, raw içeriyorsa direkt dosya
        if any(x in url for x in ['/releases/download/', '/blob/', '/raw/']):
            return False
        
        # github.com/user/repo formatı - repo URL'i
        pattern = r'https?://github\.com/[^/]+/[^/]+/?$'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def extract_github_info(url: str) -> Dict[str, str]:
        """GitHub URL'den user ve repo adını çıkar"""
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if match:
            return {
                'user': match.group(1),
                'repo': match.group(2).rstrip('/')
            }
        return None
    
    @staticmethod
    def find_jars_in_github_repo(url: str, verbose: bool = False) -> List[str]:
        """
        GitHub repository'sinde JAR dosyalarını bul
        
        Returns:
            JAR dosyalarının direkt download URL'leri
        """
        info = JarDownloader.extract_github_info(url)
        if not info:
            return []
        
        user = info['user']
        repo = info['repo']
        
        jar_urls = []
        
        if verbose:
            print(f"  → GitHub API kullanılıyor: {user}/{repo}")
        
        # 1. Releases'leri kontrol et
        try:
            api_url = f"https://api.github.com/repos/{user}/{repo}/releases"
            req = urllib.request.Request(
                api_url,
                headers={'User-Agent': 'LeraScanner/1.0'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                releases = json.loads(response.read())
                
                for release in releases:
                    for asset in release.get('assets', []):
                        if asset['name'].endswith('.jar'):
                            jar_urls.append(asset['browser_download_url'])
                            if verbose:
                                print(f"  → Bulundu: {asset['name']} (Release: {release.get('tag_name', 'unknown')})")
        
        except Exception as e:
            if verbose:
                print(f"  ⚠ Release kontrolü başarısız: {e}")
        
        # 2. Ana branch'te JAR dosyalarını ara (tree API)
        try:
            # Önce default branch'i öğren
            repo_url = f"https://api.github.com/repos/{user}/{repo}"
            req = urllib.request.Request(
                repo_url,
                headers={'User-Agent': 'LeraScanner/1.0'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                repo_data = json.loads(response.read())
                default_branch = repo_data.get('default_branch', 'main')
            
            # Tree API ile tüm dosyaları al
            tree_url = f"https://api.github.com/repos/{user}/{repo}/git/trees/{default_branch}?recursive=1"
            req = urllib.request.Request(
                tree_url,
                headers={'User-Agent': 'LeraScanner/1.0'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                tree_data = json.loads(response.read())
                
                for item in tree_data.get('tree', []):
                    if item['path'].endswith('.jar') and item['type'] == 'blob':
                        # Raw URL oluştur
                        raw_url = f"https://github.com/{user}/{repo}/raw/{default_branch}/{item['path']}"
                        jar_urls.append(raw_url)
                        if verbose:
                            print(f"  → Bulundu: {item['path']} (Repository)")
        
        except Exception as e:
            if verbose:
                print(f"  ⚠ Repository taraması başarısız: {e}")
        
        return jar_urls
    
    @staticmethod
    def convert_github_url(url: str) -> str:
        """
        GitHub URL'ini raw download URL'e çevir
        
        Örnekler:
        - https://github.com/user/repo/blob/main/file.jar -> raw URL
        - https://github.com/user/repo/releases/download/v1.0/file.jar -> aynı kalır
        """
        # /blob/ içeren GitHub URL'lerini /raw/ ile değiştir
        if 'github.com' in url and '/blob/' in url:
            url = url.replace('/blob/', '/raw/')
        
        return url
    
    @staticmethod
    def get_filename_from_url(url: str) -> str:
        """URL'den dosya adını çıkar"""
        parsed = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed.path)
        
        # Dosya adı yoksa veya .jar ile bitmiyorsa
        if not filename or not filename.endswith('.jar'):
            filename = 'downloaded.jar'
        
        return filename
    
    @staticmethod
    def download_jar(url: str, verbose: bool = False) -> str:
        """
        URL'den JAR dosyasını indir ve geçici dizine kaydet
        
        Args:
            url: JAR dosyasının URL'i
            verbose: Detaylı çıktı göster
            
        Returns:
            İndirilen dosyanın yolu
            
        Raises:
            Exception: İndirme hatası durumunda
        """
        # GitHub URL'ini dönüştür
        download_url = JarDownloader.convert_github_url(url)
        
        if verbose:
            print(f"  → Orijinal URL: {url}")
            if download_url != url:
                print(f"  → Dönüştürülen URL: {download_url}")
        
        # Dosya adını al
        filename = JarDownloader.get_filename_from_url(download_url)
        
        # Geçici dizine kaydet
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, 'lera_scanner_' + filename)
        
        try:
            if verbose:
                print(f"  → İndiriliyor: {filename}...")
            
            # User-Agent ekle (bazı siteler gerektirir)
            req = urllib.request.Request(
                download_url,
                headers={
                    'User-Agent': 'LeraScanner/1.0 (Minecraft Ghost Client Detector)'
                }
            )
            
            # İndir
            with urllib.request.urlopen(req, timeout=30) as response:
                content = response.read()
                
                # Dosyayı kaydet
                with open(temp_path, 'wb') as f:
                    f.write(content)
            
            if verbose:
                size_mb = len(content) / (1024 * 1024)
                print(f"  → İndirildi: {size_mb:.2f} MB")
                print(f"  → Geçici yol: {temp_path}")
            
            return temp_path
            
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP Hatası {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            raise Exception(f"URL Hatası: {e.reason}")
        except Exception as e:
            raise Exception(f"İndirme hatası: {str(e)}")
    
    @staticmethod
    def cleanup(filepath: str):
        """İndirilen geçici dosyayı sil"""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
        except:
            pass  # Geçici dosya silinmezse sorun değil
```
