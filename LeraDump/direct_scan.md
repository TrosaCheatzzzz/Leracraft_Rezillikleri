# direct_scan

_Kaynak: scanner\direct_scan.py - 178 satir_

```python
"""
LeraScanner - Direct Auto Scan
Menü yok, direkt çalışır, sadece sonuçları gösterir
"""

import os
import sys
import time
from datetime import datetime
from colorama import init, Fore, Style

from scanner.jar_scanner import JarScanner
from scanner.memory_scanner import MemoryScanner
from scanner.prefetch_scanner import PrefetchScanner
from scanner.system_scanner import SystemScanner

init(autoreset=True)


def print_banner():
    """Banner"""
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.RED}🔍 LERASCANNER - Minecraft Ghost Client Detector{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")


def print_status(message):
    """Status mesajı"""
    print(f"{Fore.YELLOW}⏳ {message}...{Style.RESET_ALL}")


def main():
    """Ana fonksiyon - direkt tarama"""
    start_time = time.time()
    
    print_banner()
    print(f"{Fore.WHITE}Sistem otomatik olarak taranıyor...{Style.RESET_ALL}\n")
    
    all_detections = []
    
    # 1. JAR TARAMA
    print_status("JAR dosyaları aranıyor")
    try:
        jar_files = SystemScanner.scan_system(verbose=True)
        
        if jar_files:
            total_jars = len(jar_files)
            print(f"\n{Fore.GREEN}✓ {total_jars} JAR dosyası bulundu{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Taranıyor...{Style.RESET_ALL}\n")
            
            scanner = JarScanner(verbose=False)
            
            for i, jar_file in enumerate(jar_files, 1):
                # Progress bar
                percentage = (i / total_jars) * 100
                bar_length = 50
                filled = int(bar_length * i / total_jars)
                bar = '█' * filled + '░' * (bar_length - filled)
                
                # Filename (kısa göster)
                filename = os.path.basename(jar_file)
                if len(filename) > 40:
                    filename = filename[:37] + "..."
                
                # Progress göster
                print(f"\r{Fore.CYAN}[{bar}] {percentage:.1f}% ({i}/{total_jars}) {Fore.WHITE}{filename}{Style.RESET_ALL}", end='', flush=True)
                
                result = scanner.scan_jar(jar_file)
                if result['is_suspicious']:
                    all_detections.append(('JAR', result))
            
            print()  # Yeni satır
            print(f"{Fore.GREEN}✓ JAR tarama tamamlandı{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.YELLOW}⚠ JAR dosyası bulunamadı{Style.RESET_ALL}\n")
            
    except Exception as e:
        print(f"\n{Fore.RED}✗ JAR tarama hatası: {e}{Style.RESET_ALL}\n")
    
    # 2. RAM TARAMA
    print_status("RAM memory taranıyor")
    try:
        mem_scanner = MemoryScanner(verbose=False)
        if mem_scanner.is_admin:
            processes = mem_scanner.find_java_processes()
            
            if processes:
                print(f"{Fore.GREEN}✓ {len(processes)} Java process bulundu{Style.RESET_ALL}\n")
                
                for i, proc in enumerate(processes, 1):
                    print(f"{Fore.CYAN}[{i}/{len(processes)}] Process: {proc['name']} (PID: {proc['pid']})...{Style.RESET_ALL}", end='', flush=True)
                    
                    result = mem_scanner.scan_process_memory(proc['pid'])
                    result['name'] = proc['name']
                    
                    if result.get('scanned') and result.get('detections'):
                        all_detections.append(('MEMORY', result))
                        print(f" {Fore.RED}⚠ GHOST CLIENT!{Style.RESET_ALL}")
                    else:
                        print(f" {Fore.GREEN}✓{Style.RESET_ALL}")
                
                print(f"\n{Fore.GREEN}✓ RAM tarama tamamlandı{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.YELLOW}⚠ Çalışan Java process bulunamadı{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.YELLOW}⚠ RAM tarama atlandı (admin gerekli){Style.RESET_ALL}\n")
    except Exception as e:
        print(f"\n{Fore.RED}✗ RAM tarama hatası: {e}{Style.RESET_ALL}\n")
    
    # 3. PREFETCH TARAMA
    print_status("Prefetch analiz ediliyor")
    try:
        pf_scanner = PrefetchScanner(verbose=False)
        if pf_scanner.is_admin:
            print(f"{Fore.CYAN}Windows Prefetch dosyaları analiz ediliyor...{Style.RESET_ALL}\n")
            
            result = pf_scanner.analyze_jar_history()
            
            if not result.get('error') and result.get('suspicious_jars'):
                for jar in result['suspicious_jars']:
                    all_detections.append(('PREFETCH', jar))
            
            print(f"{Fore.GREEN}✓ Prefetch analizi tamamlandı{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.YELLOW}⚠ Prefetch analizi atlandı (admin gerekli){Style.RESET_ALL}\n")
    except Exception as e:
        print(f"\n{Fore.RED}✗ Prefetch analizi hatası: {e}{Style.RESET_ALL}\n")
    
    # SONUÇLAR
    elapsed = time.time() - start_time
    
    print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}TARAMA TAMAMLANDI{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    
    print(f"{Fore.WHITE}Süre: {elapsed:.1f} saniye{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")
    
    if not all_detections:
        print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ SİSTEM TEMİZ{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
        print(f"{Fore.WHITE}Hiçbir ghost client tespit edilmedi.{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.RED}⚠️  GHOST CLIENT TESPİT EDİLDİ!{Style.RESET_ALL}")
        print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Toplam tespit: {len(all_detections)}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}BULUNAN CLIENT:{Style.RESET_ALL}\n")
        
        for i, (det_type, result) in enumerate(all_detections, 1):
            print(f"{Fore.WHITE}[{i}] {det_type} TESPİTİ:{Style.RESET_ALL}")
            
            if det_type == 'JAR':
                print(f"   {Fore.RED}📦 Client: Doomsday Client{Style.RESET_ALL}")
                print(f"   {Fore.WHITE}Dosya Yolu: {result['path']}{Style.RESET_ALL}")
            
            elif det_type == 'MEMORY':
                print(f"   {Fore.RED}🧠 Client: Doomsday Client (RAM'de Aktif){Style.RESET_ALL}")
                print(f"   {Fore.WHITE}Process: {result['name']} (PID: {result['pid']}){Style.RESET_ALL}")
            
            elif det_type == 'PREFETCH':
                print(f"   {Fore.RED}📂 Client: Doomsday Client (Geçmişte Çalıştırılmış){Style.RESET_ALL}")
                print(f"   {Fore.WHITE}Dosya Yolu: {result['jar_path']}{Style.RESET_ALL}")
            
            print()
    
    input(f"{Fore.CYAN}Çıkmak için Enter'a basın...{Style.RESET_ALL}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Tarama iptal edildi{Style.RESET_ALL}")
        sys.exit(0)
```
