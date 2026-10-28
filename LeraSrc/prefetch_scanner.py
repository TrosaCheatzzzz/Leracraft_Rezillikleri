"""
Windows Prefetch Scanner - Geçmişte çalıştırılan JAR'ları bul
"""

import os
import glob
import struct
from pathlib import Path
from typing import List, Dict
import ctypes


class PrefetchScanner:
    """Windows Prefetch dosyalarını analiz eder"""
    
    PREFETCH_PATH = r"C:\Windows\Prefetch"
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.is_admin = self._check_admin()
    
    def _check_admin(self) -> bool:
        """Admin yetkisi kontrolü"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    
    def can_access_prefetch(self) -> bool:
        """Prefetch klasörüne erişim kontrolü"""
        try:
            return os.path.exists(self.PREFETCH_PATH) and os.access(self.PREFETCH_PATH, os.R_OK)
        except:
            return False
    
    def find_jar_references(self) -> List[Dict]:
        """Prefetch dosyalarında JAR referanslarını bul"""
        if not self.is_admin:
            return [{
                'error': 'Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!'
            }]
        
        if not self.can_access_prefetch():
            return [{
                'error': f'Prefetch klasörüne erişim yok: {self.PREFETCH_PATH}'
            }]
        
        jar_references = []
        
        try:
            # Tüm .pf dosyalarını tara
            pf_files = glob.glob(os.path.join(self.PREFETCH_PATH, "*.pf"))
            
            if self.verbose:
                print(f"  → {len(pf_files)} Prefetch dosyası bulundu")
            
            for pf_file in pf_files:
                try:
                    # Dosyayı binary olarak oku
                    with open(pf_file, 'rb') as f:
                        data = f.read()
                    
                    # JAR referanslarını ara (basit string arama)
                    data_str = data.decode('utf-16-le', errors='ignore')
                    
                    # .jar içeren satırları bul
                    if '.jar' in data_str.lower():
                        # Java process'i mi?
                        pf_name = os.path.basename(pf_file)
                        if 'JAVA' in pf_name.upper():
                            jar_references.append({
                                'prefetch_file': pf_name,
                                'found_jars': self._extract_jar_paths(data_str),
                                'modified_time': os.path.getmtime(pf_file)
                            })
                
                except Exception as e:
                    if self.verbose:
                        print(f"  ⚠ {os.path.basename(pf_file)}: {e}")
        
        except Exception as e:
            return [{
                'error': f'Prefetch taraması başarısız: {e}'
            }]
        
        return jar_references
    
    def _extract_jar_paths(self, data: str) -> List[str]:
        """String'den JAR yollarını çıkar"""
        jar_paths = []
        
        # .jar içeren tüm kelimeleri bul
        words = data.split()
        for word in words:
            if '.jar' in word.lower():
                # Temizle
                cleaned = word.replace('\x00', '').strip()
                if len(cleaned) > 4 and cleaned not in jar_paths:
                    jar_paths.append(cleaned)
        
        return jar_paths[:10]  # Max 10 JAR
    
    def analyze_jar_history(self) -> Dict:
        """JAR geçmişini analiz et"""
        jar_refs = self.find_jar_references()
        
        if not jar_refs or 'error' in jar_refs[0]:
            return {
                'total_java_executions': 0,
                'total_jar_references': 0,
                'suspicious_jars': [],
                'error': jar_refs[0].get('error') if jar_refs else None
            }
        
        # Şüpheli dosya isimleri
        suspicious_keywords = [
            'doomsday', 'ghost', 'client', 'cheat', 'hack',
            'vape', 'liquidbounce', 'wurst', 'meteor'
        ]
        
        suspicious_jars = []
        total_jar_count = 0
        
        for ref in jar_refs:
            for jar in ref.get('found_jars', []):
                total_jar_count += 1
                jar_lower = jar.lower()
                
                for keyword in suspicious_keywords:
                    if keyword in jar_lower:
                        suspicious_jars.append({
                            'jar_path': jar,
                            'keyword': keyword,
                            'prefetch': ref['prefetch_file'],
                            'last_execution': ref['modified_time']
                        })
                        break
        
        return {
            'total_java_executions': len(jar_refs),
            'total_jar_references': total_jar_count,
            'suspicious_jars': suspicious_jars
        }
