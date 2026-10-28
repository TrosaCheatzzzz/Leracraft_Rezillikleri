"""
Otomatik Tam Tarama Modülü
Her şeyi otomatik tarar ve detaylı rapor verir
"""

import os
import time
from datetime import datetime
from typing import Dict, List
from colorama import Fore, Style

from scanner.jar_scanner import JarScanner
from scanner.memory_scanner import MemoryScanner
from scanner.prefetch_scanner import PrefetchScanner
from scanner.system_scanner import SystemScanner


class AutoScanner:
    """Otomatik tam tarama sınıfı"""
    
    def __init__(self):
        self.start_time = None
        self.results = {
            'jar_scan': [],
            'memory_scan': [],
            'prefetch_scan': None,
            'detections': []
        }
    
    def print_header(self):
        """Başlık yazdır"""
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.RESET_ALL} {Fore.RED}🔍 LERASCAN NER - OTOM ATİK TAM TARAMA{Style.RESET_ALL} {Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}⚡ TÜM SİSTEM OTOM ATİK OLARAK TARANACAK{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • JAR Dosyaları (Derin Tarama){Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • RAM Memory (Java Processes){Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • Windows Prefetch (Geçmiş){Style.RESET_ALL}\n")
    
    def scan_all_jars(self):
        """Tüm JAR dosyalarını tara"""
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔍 ADIM 1: JAR DOSYALARI TARANIY OR...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        # Sistem taraması
        print(f"{Fore.YELLOW}📂 Sistem lokasyonları aranıyor...{Style.RESET_ALL}")
        jar_files = SystemScanner.scan_system(verbose=False)
        
        if not jar_files:
            print(f"{Fore.YELLOW}⚠ Hiç JAR dosyası bulunamadı{Style.RESET_ALL}\n")
            return
        
        print(f"{Fore.GREEN}✓ {len(jar_files)} JAR dosyası bulundu{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}🔍 Derin tarama başlıyor...{Style.RESET_ALL}\n")
        
        scanner = JarScanner(verbose=False)
        
        for i, jar_file in enumerate(jar_files, 1):
            try:
                # Progress
                progress = f"[{i}/{len(jar_files)}]"
                filename = os.path.basename(jar_file)
                
                # 60 karakterden uzunsa kısalt
                if len(filename) > 50:
                    filename = filename[:47] + "..."
                
                print(f"{Fore.WHITE}{progress} {filename}...", end='', flush=True)
                
                result = scanner.scan_jar(jar_file)
                self.results['jar_scan'].append(result)
                
                if result['is_suspicious']:
                    print(f" {Fore.RED}⚠ GHOST CLIENT!{Style.RESET_ALL}")
                    self.results['detections'].append({
                        'type': 'JAR',
                        'result': result
                    })
                else:
                    print(f" {Fore.GREEN}✓{Style.RESET_ALL}")
            
            except Exception as e:
                print(f" {Fore.RED}✗ Hata{Style.RESET_ALL}")
        
        # Özet
        stats = scanner.get_stats()
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}JAR Tarama Özeti:{Style.RESET_ALL}")
        print(f"  • Toplam: {stats['total_scanned']}")
        print(f"  • {Fore.RED}Ghost Client: {stats['total_detected']}{Style.RESET_ALL}")
        print(f"  • {Fore.GREEN}Temiz: {stats['clean_count']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    
    def scan_memory(self):
        """RAM memory tara"""
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🧠 ADIM 2: RAM MEMORY TARANI YOR...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        scanner = MemoryScanner(verbose=False)
        
        if not scanner.is_admin:
            print(f"{Fore.YELLOW}⚠ Admin yetkisi yok - RAM taraması atlandı{Style.RESET_ALL}\n")
            return
        
        print(f"{Fore.YELLOW}🔍 Java process'leri aranıyor...{Style.RESET_ALL}")
        processes = scanner.find_java_processes()
        
        if not processes:
            print(f"{Fore.YELLOW}⚠ Çalışan Java process bulunamadı{Style.RESET_ALL}\n")
            return
        
        print(f"{Fore.GREEN}✓ {len(processes)} Java process bulundu{Style.RESET_ALL}\n")
        
        for proc in processes:
            print(f"{Fore.WHITE}Process: {proc['name']} (PID: {proc['pid']}){Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}🔍 Memory taranıyor (bu biraz zaman alabilir)...{Style.RESET_ALL}\n")
        
        results = scanner.scan_all()
        self.results['memory_scan'] = results
        
        detected = 0
        for result in results:
            if result.get('scanned') and result.get('detections'):
                detected += 1
                self.results['detections'].append({
                    'type': 'MEMORY',
                    'result': result
                })
        
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Memory Tarama Özeti:{Style.RESET_ALL}")
        print(f"  • Process sayısı: {len(processes)}")
        print(f"  • {Fore.RED}Ghost Client: {detected}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
    
    def scan_prefetch(self):
        """Prefetch analizi"""
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📂 ADIM 3: WINDOWS PREFETCH ANALİZ EDİLİYOR...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        scanner = PrefetchScanner(verbose=False)
        
        if not scanner.is_admin:
            print(f"{Fore.YELLOW}⚠ Admin yetkisi yok - Prefetch analizi atlandı{Style.RESET_ALL}\n")
            return
        
        print(f"{Fore.YELLOW}🔍 Prefetch dosyaları analiz ediliyor...{Style.RESET_ALL}\n")
        
        result = scanner.analyze_jar_history()
        self.results['prefetch_scan'] = result
        
        if result.get('error'):
            print(f"{Fore.YELLOW}⚠ {result['error']}{Style.RESET_ALL}\n")
            return
        
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Prefetch Analizi:{Style.RESET_ALL}")
        print(f"  • Java çalıştırma: {result['total_java_executions']}")
        print(f"  • JAR referansı: {result['total_jar_references']}")
        print(f"  • {Fore.RED}Şüpheli JAR: {len(result['suspicious_jars'])}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        if result['suspicious_jars']:
            for jar in result['suspicious_jars']:
                self.results['detections'].append({
                    'type': 'PREFETCH',
                    'result': jar
                })
    
    def print_detections(self):
        """Tüm tespitleri detaylı göster"""
        if not self.results['detections']:
            print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}✅ TÜM SİSTEM TEMİZ!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
            print(f"{Fore.WHITE}Hiçbir ghost client bulunamadı.{Style.RESET_ALL}\n")
            return
        
        print(f"\n{Fore.RED}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.RED}⚠️  GHOST CLIENT TESPİTLERİ - DETAYLI RAPOR{Style.RESET_ALL}")
        print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}Toplam tespit: {len(self.results['detections'])}{Style.RESET_ALL}\n")
        
        for i, detection in enumerate(self.results['detections'], 1):
            det_type = detection['type']
            result = detection['result']
            
            print(f"{Fore.CYAN}┌─ [{i}] {det_type} TESPİTİ{Style.RESET_ALL}")
            print(f"{Fore.CYAN}│{Style.RESET_ALL}")
            
            if det_type == 'JAR':
                # JAR tespiti - DETAYLI
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.RED}🚨 Ghost Client Bulundu!{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}📦 Dosya:{Style.RESET_ALL} {result['filename']}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}📍 Tam Yol:{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}    {Fore.WHITE}{result['path']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}")
                
                # Client isimleri
                clients = set()
                for found in result['found_files']:
                    clients.add(found['description'])
                
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.RED}🎯 Tespit Edilen Client:{Style.RESET_ALL} {', '.join(clients)}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}📋 Bulunan Kanıtlar:{Style.RESET_ALL}")
                
                for found in result['found_files']:
                    print(f"{Fore.CYAN}│{Style.RESET_ALL}   {Fore.RED}├─{Style.RESET_ALL} {found['actual_name']}")
                    print(f"{Fore.CYAN}│{Style.RESET_ALL}   {Fore.WHITE}│  Lokasyon:{Style.RESET_ALL} {found['location']}")
                    print(f"{Fore.CYAN}│{Style.RESET_ALL}   {Fore.WHITE}│  Tam Yol:{Style.RESET_ALL} {found['full_path']}")
                    print(f"{Fore.CYAN}│{Style.RESET_ALL}   {Fore.WHITE}│{Style.RESET_ALL}")
                
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.WHITE}İçinde {result['all_files_scanned']} dosya tarandı{Style.RESET_ALL}")
            
            elif det_type == 'MEMORY':
                # Memory tespiti
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.RED}🧠 RAM'de Ghost Client Aktif!{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}Process:{Style.RESET_ALL} {result['name']}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}PID:{Style.RESET_ALL} {result['pid']}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.RED}Tespit Sayısı:{Style.RESET_ALL} {len(result.get('detections', []))}")
            
            elif det_type == 'PREFETCH':
                # Prefetch tespiti
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}📂 Geçmişte Şüpheli JAR Çalıştırılmış{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}JAR Yolu:{Style.RESET_ALL} {result['jar_path']}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}Anahtar Kelime:{Style.RESET_ALL} {result['keyword']}")
                print(f"{Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}Prefetch:{Style.RESET_ALL} {result['prefetch']}")
            
            print(f"{Fore.CYAN}└{'─'*68}{Style.RESET_ALL}\n")
    
    def run(self):
        """Tam otomatik tarama başlat"""
        self.start_time = time.time()
        
        self.print_header()
        
        input(f"{Fore.CYAN}Başlatmak için Enter'a basın...{Style.RESET_ALL}\n")
        
        # 1. JAR Tarama
        self.scan_all_jars()
        
        # 2. Memory Tarama
        self.scan_memory()
        
        # 3. Prefetch Analizi
        self.scan_prefetch()
        
        # 4. Sonuçları göster
        self.print_detections()
        
        # Süre
        elapsed = time.time() - self.start_time
        print(f"{Fore.CYAN}⏱️  Toplam süre: {elapsed:.1f} saniye{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Tarama tamamlandı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")
