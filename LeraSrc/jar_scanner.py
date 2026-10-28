"""
JAR dosyalarını analiz eden ana modül
Ghost client tespiti için özel dosyaları arar
"""

import zipfile
import os
from pathlib import Path
from typing import List, Dict, Tuple


class GhostClientSignature:
    """Ghost client imzası - aranan dosyalar"""
    
    SUSPICIOUS_FILES = {
        '0': 'Doomsday Client',
        '1': 'Doomsday Client',
        'l.png': 'Doomsday Client'
    }
    
    @staticmethod
    def check_any_match(filename: str) -> bool:
        """
        Dosya adının herhangi bir eşleşme kontrolü
        Her yerdeki dosyaları bulur (dizin farketmez)
        """
        filename_lower = filename.lower()
        basename = os.path.basename(filename_lower)
        
        # Exact match
        for suspicious_file in GhostClientSignature.SUSPICIOUS_FILES.keys():
            if basename == suspicious_file.lower():
                return True, suspicious_file
        
        return False, None
    
    @staticmethod
    def check_file_match(filename: str) -> bool:
        """Dosya adının tam eşleşme kontrolü"""
        return filename in GhostClientSignature.SUSPICIOUS_FILES
    
    @staticmethod
    def check_path_match(filepath: str) -> Tuple[bool, str]:
        """
        Tam dosya yolu kontrolü - dizin içinde de arar
        Returns: (eşleşme_var_mı, eşleşen_dosya_adı)
        """
        filepath = filepath.replace('\\', '/')
        parts = filepath.split('/')
        
        for part in parts:
            if part in GhostClientSignature.SUSPICIOUS_FILES:
                return True, part
        
        return False, ''


class JarScanner:
    """JAR dosyalarını analiz eden sınıf"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.scanned_count = 0
        self.detected_count = 0
    
    def scan_jar(self, jar_path: str) -> Dict:
        """
        Bir JAR dosyasını tarar - DEEP SCAN
        
        Args:
            jar_path: JAR dosyasının yolu
            
        Returns:
            Tarama sonucu dictionary
        """
        result = {
            'path': jar_path,
            'filename': os.path.basename(jar_path),
            'is_suspicious': False,
            'found_files': [],
            'all_files_scanned': 0,
            'error': None
        }
        
        try:
            if not zipfile.is_zipfile(jar_path):
                result['error'] = 'Geçerli bir JAR/ZIP dosyası değil'
                return result
            
            with zipfile.ZipFile(jar_path, 'r') as jar:
                file_list = jar.namelist()
                result['all_files_scanned'] = len(file_list)
                
                if self.verbose:
                    print(f"  → {len(file_list)} dosya bulundu, derin tarama yapılıyor...")
                
                # Her dosyayı kontrol et - DEEP SCAN
                for file_path in file_list:
                    # Dosya ismini al (path'den bağımsız)
                    filename = os.path.basename(file_path)
                    
                    # Tüm suspicious dosyaları kontrol et
                    for suspicious_file, client_name in GhostClientSignature.SUSPICIOUS_FILES.items():
                        if filename.lower() == suspicious_file.lower():
                            result['found_files'].append({
                                'name': suspicious_file,
                                'actual_name': filename,
                                'full_path': file_path,
                                'description': client_name,
                                'location': os.path.dirname(file_path) if os.path.dirname(file_path) else '(root)'
                            })
                            result['is_suspicious'] = True
                            
                            if self.verbose:
                                print(f"  → 🚨 BULUNDU: {file_path}")
            
            self.scanned_count += 1
            if result['is_suspicious']:
                self.detected_count += 1
                
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def scan_directory(self, directory: str, recursive: bool = True) -> List[Dict]:
        """
        Bir dizindeki tüm JAR dosyalarını tarar
        
        Args:
            directory: Taranacak dizin
            recursive: Alt dizinlere de bakılsın mı
            
        Returns:
            Tarama sonuçları listesi
        """
        results = []
        jar_files = []
        
        directory_path = Path(directory)
        
        if not directory_path.exists():
            return [{
                'error': f'Dizin bulunamadı: {directory}',
                'path': directory
            }]
        
        # JAR dosyalarını bul
        if recursive:
            jar_files = list(directory_path.rglob('*.jar'))
        else:
            jar_files = list(directory_path.glob('*.jar'))
        
        if not jar_files:
            return [{
                'error': 'Dizinde JAR dosyası bulunamadı',
                'path': directory
            }]
        
        print(f"\n📦 {len(jar_files)} JAR dosyası bulundu, taranıyor...\n")
        
        # Her JAR'ı tara
        for jar_file in jar_files:
            if self.verbose:
                print(f"🔍 Taranıyor: {jar_file.name}")
            
            result = self.scan_jar(str(jar_file))
            results.append(result)
        
        return results
    
    def get_stats(self) -> Dict:
        """Tarama istatistiklerini döndürür"""
        return {
            'total_scanned': self.scanned_count,
            'total_detected': self.detected_count,
            'clean_count': self.scanned_count - self.detected_count
        }
