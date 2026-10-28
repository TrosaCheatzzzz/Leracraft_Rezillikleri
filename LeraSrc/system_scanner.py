"""
Sistem çapında JAR tarama modülü
TÜM BİLGİSAYARI tarar - her disk, her klasör
"""

import os
from pathlib import Path
from typing import List
import string


class SystemScanner:
    """Bilgisayar çapında JAR dosyalarını bulan sınıf"""
    
    @staticmethod
    def get_all_drives() -> List[str]:
        """Tüm disk sürücülerini bul (C:, D:, E: vb.)"""
        drives = []
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drives.append(drive)
        return drives
    
    @staticmethod
    def scan_system(verbose: bool = False) -> List[str]:
        """
        TÜM BİLGİSAYARI tarar - her disk, her klasör
        
        Returns:
            JAR dosyalarının yolları
        """
        jar_files = []
        
        # Tüm diskleri al
        drives = SystemScanner.get_all_drives()
        
        if verbose:
            print(f"  → {len(drives)} disk bulundu: {', '.join(drives)}")
            print(f"  → JAR dosyaları aranıyor...")
        
        # Atlayılacak sistem klasörleri (erişim hatası veya gereksiz)
        skip_folders = {
            'Windows', 'Program Files', 'Program Files (x86)',
            'ProgramData', '$Recycle.Bin', 'System Volume Information',
            'Recovery', 'Intel', 'AMD', 'NVIDIA', 'PerfLogs',
            'AppData\\Local\\Temp', 'Temp', 'tmp'
        }
        
        total_drives = len(drives)
        
        for drive_index, drive in enumerate(drives, 1):
            if verbose:
                from colorama import Fore, Style
                print(f"\n  {Fore.YELLOW}→ [{drive_index}/{total_drives}] {drive} taranıyor...{Style.RESET_ALL}")
            
            try:
                # Her diski recursive tara
                for root, dirs, files in os.walk(drive):
                    # Sistem klasörlerini atla
                    skip_this = False
                    for skip in skip_folders:
                        if skip.lower() in root.lower():
                            skip_this = True
                            break
                    
                    if skip_this:
                        dirs[:] = []  # Alt klasörlere girme
                        continue
                    
                    # JAR dosyalarını bul
                    for file in files:
                        if file.lower().endswith('.jar'):
                            full_path = os.path.join(root, file)
                            jar_files.append(full_path)
                            
                            if verbose and len(jar_files) % 5 == 0:
                                print(f"    {Fore.GREEN}• {len(jar_files)} JAR bulundu...{Style.RESET_ALL}", end='\r', flush=True)
            
            except PermissionError:
                if verbose:
                    print(f"    ⚠ Bazı klasörlere erişim reddedildi")
            except Exception as e:
                if verbose:
                    print(f"    ⚠ Hata: {e}")
        
        if verbose:
            from colorama import Fore, Style
            print(f"\n  {Fore.GREEN}✓ Arama tamamlandı - {len(jar_files)} JAR bulundu{Style.RESET_ALL}")
        
        return jar_files
    
    @staticmethod
    def get_common_locations() -> List[str]:
        """
        Yaygın Minecraft lokasyonları (hızlı tarama için)
        Deprecated - artık tüm sistem taranıyor
        """
        return []
    
    @staticmethod
    def get_minecraft_instances() -> List[str]:
        """
        Minecraft instance dizinleri
        Deprecated - artık tüm sistem taranıyor
        """
        return []
