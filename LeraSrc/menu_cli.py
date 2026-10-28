"""
LeraScanner - Ana Menü CLI
Console-based menü sistemi
"""

import os
import sys
import time
from colorama import init, Fore, Style
from scanner.jar_scanner import JarScanner
from scanner.memory_scanner import MemoryScanner
from scanner.prefetch_scanner import PrefetchScanner
from scanner.system_scanner import SystemScanner
from scanner.auto_scanner import AutoScanner

# Windows için colorama başlat
init(autoreset=True)


class MenuCLI:
    """Ana menü arayüzü"""
    
    BANNER = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              {Fore.RED}🔍 LeraScanner v2.0.0{Fore.CYAN}                      ║
║         {Fore.WHITE}Minecraft Ghost Client Detector{Fore.CYAN}                 ║
║              {Fore.YELLOW}Advanced Forensic Scanner{Fore.CYAN}                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    
    def __init__(self):
        self.running = True
    
    def clear_screen(self):
        """Ekranı temizle"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Banner yazdır"""
        print(self.BANNER)
    
    def print_menu(self):
        """Ana menüyü yazdır"""
        print(f"{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                      {Fore.WHITE}ANA MENÜ{Fore.CYAN}                           ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╠═══════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.RED}[0]{Fore.WHITE} 🔥 OTOMATİK TAM TARAMA (ÖNERİLEN){Fore.CYAN}                  ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}[1]{Fore.WHITE} JAR Dosyası Tara{Fore.CYAN}                                  ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}[2]{Fore.WHITE} Sistem Çapında JAR Tara{Fore.CYAN}                          ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}[3]{Fore.WHITE} RAM Memory Tarama (Java Processes){Fore.CYAN}                ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}[4]{Fore.WHITE} Windows Prefetch Analizi{Fore.CYAN}                          ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}[5]{Fore.WHITE} Hakkında{Fore.CYAN}                                          ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}[9]{Fore.WHITE} Çıkış{Fore.CYAN}                                             ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    def auto_scan(self):
        """Otomatik tam tarama"""
        self.clear_screen()
        auto_scanner = AutoScanner()
        auto_scanner.run()
        input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def scan_jar_file(self):
        """JAR dosyası tara"""
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}🔍 JAR DOSYASI TARAMA{Style.RESET_ALL}\n")
        
        jar_path = input(f"{Fore.CYAN}JAR dosyasının yolunu girin: {Style.RESET_ALL}").strip('"')
        
        if not os.path.exists(jar_path):
            print(f"\n{Fore.RED}❌ Dosya bulunamadı!{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.CYAN}🔍 Taranıyor: {os.path.basename(jar_path)}{Style.RESET_ALL}\n")
        
        scanner = JarScanner(verbose=True)
        result = scanner.scan_jar(jar_path)
        
        print()
        if result['is_suspicious']:
            print(f"{Fore.RED}{'='*60}{Style.RESET_ALL}")
            print(f"{Fore.RED}⚠️  GHOST CLIENT TESPİT EDİLDİ!{Style.RESET_ALL}")
            print(f"{Fore.RED}{'='*60}{Style.RESET_ALL}")
            
            detected_clients = set()
            for found in result['found_files']:
                detected_clients.add(found['description'])
            
            print(f"\n{Fore.RED}🚨 Tespit edilen: {', '.join(detected_clients)}{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Bulunan dosyalar:{Style.RESET_ALL}")
            for found in result['found_files']:
                print(f"  {Fore.RED}├─ {found['name']}{Style.RESET_ALL}")
                print(f"  {Fore.WHITE}│  Yol: {found['full_path']}{Style.RESET_ALL}")
            print()
        else:
            print(f"{Fore.GREEN}✅ TEMİZ - Ghost client bulunamadı{Style.RESET_ALL}\n")
        
        input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def scan_system(self):
        """Sistem çapında JAR tara"""
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}🖥️  SİSTEM ÇAPINDA TARAMA{Style.RESET_ALL}\n")
        
        print(f"{Fore.WHITE}Taranacak lokasyonlar:{Style.RESET_ALL}")
        print(f"  • .minecraft/mods")
        print(f"  • Downloads")
        print(f"  • Desktop")
        print(f"  • CurseForge, MultiMC, PrismLauncher\n")
        
        input(f"{Fore.CYAN}Başlatmak için Enter'a basın...{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}🔍 Sistem taranıyor...{Style.RESET_ALL}\n")
        
        jar_files = SystemScanner.scan_system(verbose=True)
        
        if not jar_files:
            print(f"\n{Fore.YELLOW}⚠ Hiç JAR dosyası bulunamadı{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.CYAN}📦 {len(jar_files)} JAR bulundu, taranıyor...{Style.RESET_ALL}\n")
            
            scanner = JarScanner(verbose=False)
            detected = 0
            
            for jar_file in jar_files:
                result = scanner.scan_jar(jar_file)
                if result['is_suspicious']:
                    detected += 1
                    print(f"{Fore.RED}⚠ GHOST CLIENT: {result['filename']}{Style.RESET_ALL}")
                    print(f"   Yol: {result['path']}\n")
            
            print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Toplam: {len(jar_files)} | Ghost Client: {Fore.RED}{detected}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def scan_memory(self):
        """RAM memory tara"""
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}🧠 RAM MEMORY TARAMA{Style.RESET_ALL}\n")
        
        scanner = MemoryScanner(verbose=True)
        
        if not scanner.is_admin:
            print(f"{Fore.RED}❌ UYARI: Admin yetkisi gerekli!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Programı 'Yönetici olarak çalıştır' ile açın.{Style.RESET_ALL}\n")
            input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}🔍 Java process'leri aranıyor...{Style.RESET_ALL}\n")
        
        processes = scanner.find_java_processes()
        
        if not processes:
            print(f"{Fore.YELLOW}⚠ Çalışan Java process bulunamadı{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Minecraft açık değil veya Java process'i yok.{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.GREEN}✓ {len(processes)} Java process bulundu{Style.RESET_ALL}\n")
            
            for proc in processes:
                print(f"{Fore.CYAN}Process: {proc['name']} (PID: {proc['pid']}){Style.RESET_ALL}")
            
            print(f"\n{Fore.YELLOW}⚠ UYARI: Memory tarama biraz zaman alabilir...{Style.RESET_ALL}\n")
            input(f"{Fore.CYAN}Başlatmak için Enter'a basın...{Style.RESET_ALL}")
            
            print(f"\n{Fore.CYAN}🔍 Memory taranıyor...{Style.RESET_ALL}\n")
            
            results = scanner.scan_all()
            
            detected = False
            for result in results:
                if result.get('scanned') and result.get('detections'):
                    detected = True
                    print(f"{Fore.RED}⚠️  GHOST CLIENT TESPİT EDİLDİ!{Style.RESET_ALL}")
                    print(f"   Process: {result['name']} (PID: {result['pid']})")
                    print(f"   Tespit sayısı: {len(result['detections'])}\n")
            
            if not detected:
                print(f"{Fore.GREEN}✅ TEMİZ - Memory'de ghost client bulunamadı{Style.RESET_ALL}\n")
        
        input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def scan_prefetch(self):
        """Prefetch analizi"""
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.YELLOW}📂 WINDOWS PREFETCH ANALİZİ{Style.RESET_ALL}\n")
        
        scanner = PrefetchScanner(verbose=True)
        
        if not scanner.is_admin:
            print(f"{Fore.RED}❌ UYARI: Admin yetkisi gerekli!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Programı 'Yönetici olarak çalıştır' ile açın.{Style.RESET_ALL}\n")
            input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
            return
        
        print(f"{Fore.WHITE}Windows Prefetch dosyaları Java geçmişini içerir.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Bu özellik geçmişte çalıştırılan JAR'ları bulur.{Style.RESET_ALL}\n")
        
        input(f"{Fore.CYAN}Başlatmak için Enter'a basın...{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}🔍 Prefetch dosyaları analiz ediliyor...{Style.RESET_ALL}\n")
        
        result = scanner.analyze_jar_history()
        
        if result.get('error'):
            print(f"{Fore.RED}❌ {result['error']}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Java çalıştırma sayısı: {result['total_java_executions']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Bulunan JAR referansı: {result['total_jar_references']}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
            
            if result['suspicious_jars']:
                print(f"{Fore.RED}⚠️  ŞÜPHELİ JAR'LAR BULUNDU:{Style.RESET_ALL}\n")
                for jar in result['suspicious_jars']:
                    print(f"{Fore.YELLOW}• {jar['jar_path']}{Style.RESET_ALL}")
                    print(f"  Anahtar kelime: {jar['keyword']}")
                    print(f"  Prefetch: {jar['prefetch']}\n")
            else:
                print(f"{Fore.GREEN}✅ Şüpheli JAR bulunamadı{Style.RESET_ALL}\n")
        
        input(f"\n{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def show_about(self):
        """Hakkında"""
        self.clear_screen()
        self.print_banner()
        print(f"{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                      {Fore.WHITE}HAKKINDA{Fore.CYAN}                           ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╠═══════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.WHITE}LeraScanner v2.0.0{Fore.CYAN}                                     ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.YELLOW}Minecraft Ghost Client Detector{Fore.CYAN}                       ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                                                           ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.WHITE}Özellikler:{Fore.CYAN}                                            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}✓{Fore.WHITE} JAR Dosyası Analizi{Fore.CYAN}                                ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}✓{Fore.WHITE} Sistem Çapında Tarama{Fore.CYAN}                              ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}✓{Fore.WHITE} RAM Memory Forensics{Fore.CYAN}                               ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.GREEN}✓{Fore.WHITE} Windows Prefetch Analizi{Fore.CYAN}                           ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║                                                           ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.WHITE}GitHub: {Fore.YELLOW}github.com/rushc1k/lerascanner{Fore.CYAN}             ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  {Fore.WHITE}Made by: {Fore.YELLOW}rushc1k{Fore.CYAN}                                     ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        input(f"{Fore.YELLOW}Devam etmek için Enter'a basın...{Style.RESET_ALL}")
    
    def run(self):
        """Ana döngü"""
        while self.running:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{Fore.CYAN}Seçiminiz: {Style.RESET_ALL}").strip()
            
            if choice == '0':
                self.auto_scan()
            elif choice == '1':
                self.scan_jar_file()
            elif choice == '2':
                self.scan_system()
            elif choice == '3':
                self.scan_memory()
            elif choice == '4':
                self.scan_prefetch()
            elif choice == '5':
                self.show_about()
            elif choice == '9':
                print(f"\n{Fore.YELLOW}👋 Çıkılıyor...{Style.RESET_ALL}")
                self.running = False
            else:
                print(f"\n{Fore.RED}❌ Geçersiz seçim!{Style.RESET_ALL}")
                time.sleep(1)


def main():
    """Ana giriş noktası"""
    try:
        menu = MenuCLI()
        menu.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Çıkılıyor...{Style.RESET_ALL}")
        sys.exit(0)


if __name__ == '__main__':
    main()
