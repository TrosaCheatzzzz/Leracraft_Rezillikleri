"""
LeraScanner - Komut satırı arayüzü
Minecraft Ghost Client Detector
"""

import argparse
import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

from scanner.jar_scanner import JarScanner
from scanner.downloader import JarDownloader
from scanner.system_scanner import SystemScanner

# Windows için colorama başlat
init(autoreset=True)


class CLI:
    """Komut satırı arayüzü"""
    
    BANNER = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              {Fore.RED}🔍 LeraScanner v1.0.0{Fore.CYAN}                      ║
║         {Fore.WHITE}Minecraft Ghost Client Detector{Fore.CYAN}                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    
    def __init__(self):
        self.parser = self._create_parser()
    
    def _create_parser(self):
        """Argument parser oluştur"""
        parser = argparse.ArgumentParser(
            description='Minecraft Ghost Client Detector - URL yapıştır, tara!',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
🎯 HIZLI KULLANIM:
  Sadece GitHub linkini yapıştır, geri kalanı otomatik!
  
  lera-scanner https://github.com/rushc1k/suspicious-mod
  
  → Repo'daki tüm JAR'ları bulur
  → Bilgisayarındaki tüm JAR'ları tarar (.minecraft, Downloads vb.)
  → Ghost client varsa yakalar!

📖 DİĞER KULANIMLAR:
  lera-scanner -f client.jar              # Tek dosya tara
  lera-scanner -d ./mods                   # Dizin tara
  lera-scanner --scan-system               # Sadece bilgisayarı tara
  lera-scanner --scan-system --quick       # Hızlı tarama (sadece Minecraft)
            """
        )
        
        # Ana argüman - URL veya yol
        parser.add_argument(
            'target',
            nargs='?',
            type=str,
            help='GitHub URL, JAR dosyası veya dizin'
        )
        
        parser.add_argument(
            '-f', '--file',
            type=str,
            help='Taranacak JAR dosyası veya URL (DEPRECATED: Artık direkt yazın)'
        )
        
        parser.add_argument(
            '-d', '--directory',
            type=str,
            help='Taranacak dizin'
        )
        
        parser.add_argument(
            '-r', '--recursive',
            action='store_true',
            help='Alt dizinleri de tara'
        )
        
        parser.add_argument(
            '--scan-system',
            action='store_true',
            help='Bilgisayar çapında tarama yap (.minecraft, Downloads vb.)'
        )
        
        parser.add_argument(
            '--quick',
            action='store_true',
            help='Hızlı tarama (sadece Minecraft klasörleri)'
        )
        
        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='Detaylı çıktı göster'
        )
        
        parser.add_argument(
            '--no-color',
            action='store_true',
            help='Renkleri kapat'
        )
        
        return parser
    
    def print_banner(self):
        """Banner yazdır"""
        print(self.BANNER)
    
    def print_result(self, result):
        """Tek bir tarama sonucunu yazdır"""
        if result.get('error'):
            print(f"{Fore.RED}❌ HATA: {result['error']}{Style.RESET_ALL}")
            return
        
        filename = result['filename']
        
        if result['is_suspicious']:
            print(f"\n{Fore.RED}{'='*60}")
            print(f"⚠️  GHOST CLIENT TESPİT EDİLDİ!")
            print(f"{'='*60}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}📦 Dosya: {Fore.WHITE}{filename}")
            print(f"{Fore.YELLOW}📍 Yol: {Fore.WHITE}{result['path']}")
            
            # Tespit edilen client isimlerini topla (tekrarsız)
            detected_clients = set()
            for found in result['found_files']:
                detected_clients.add(found['description'])
            
            print(f"\n{Fore.RED}🚨 Tespit edilen client(ler): {Fore.WHITE}{', '.join(detected_clients)}{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Bulunan dosyalar:{Style.RESET_ALL}")
            
            for found in result['found_files']:
                print(f"  {Fore.RED}├─ {found['name']}{Style.RESET_ALL}")
                print(f"  {Fore.WHITE}│  Tam yol: {found['full_path']}{Style.RESET_ALL}")
                print()
            
            print(f"{Fore.RED}{'='*60}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.GREEN}✓ Temiz: {Fore.WHITE}{filename}{Style.RESET_ALL}")
    
    def print_summary(self, stats):
        """Özet istatistikleri yazdır"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"📊 TARAMA ÖZETİ")
        print(f"{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Toplam taranan dosya: {Fore.CYAN}{stats['total_scanned']}{Style.RESET_ALL}")
        print(f"{Fore.RED}Şüpheli dosya sayısı: {stats['total_detected']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Temiz dosya sayısı: {stats['clean_count']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        if stats['total_detected'] > 0:
            print(f"{Fore.RED}⚠️  UYARI: Ghost client tespit edildi!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Bu dosyalar hile içeriyor.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Lütfen bu JAR dosyalarını derhal kaldırın.{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.GREEN}✅ Tüm dosyalar temiz görünüyor!{Style.RESET_ALL}\n")
    
    def run(self):
        """CLI'yi çalıştır"""
        args = self.parser.parse_args()
        
        # Renkleri kapat
        if args.no_color:
            init(strip=True, convert=False)
        
        self.print_banner()
        
        # Scanner oluştur
        scanner = JarScanner(verbose=args.verbose)
        all_results = []
        
        try:
            # Hangi modu kullanacağız?
            target = args.target or args.file
            
            # MOD 1: Sistem taraması
            if args.scan_system or (not target and not args.directory):
                print(f"{Fore.CYAN}🔍 BİLGİSAYAR ÇAPINDA TARAMA BAŞLIYOR...{Style.RESET_ALL}\n")
                
                if args.quick:
                    print(f"{Fore.YELLOW}⚡ Hızlı mod: Sadece Minecraft klasörleri{Style.RESET_ALL}\n")
                    jar_files = SystemScanner.get_minecraft_instances()
                    
                    for location in jar_files:
                        results = scanner.scan_directory(location, recursive=True)
                        all_results.extend(results)
                else:
                    print(f"{Fore.YELLOW}📂 Yaygın lokasyonlar taranıyor...{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}   (.minecraft, Downloads, Desktop, Launchers){Style.RESET_ALL}\n")
                    
                    jar_files = SystemScanner.scan_system(verbose=args.verbose)
                    
                    if not jar_files:
                        print(f"{Fore.YELLOW}⚠ Hiç JAR dosyası bulunamadı{Style.RESET_ALL}")
                        sys.exit(0)
                    
                    print(f"\n{Fore.CYAN}📦 {len(jar_files)} JAR dosyası bulundu, taranıyor...{Style.RESET_ALL}\n")
                    
                    for jar_file in jar_files:
                        if args.verbose:
                            print(f"🔍 {jar_file}")
                        result = scanner.scan_jar(jar_file)
                        all_results.append(result)
                        if not args.verbose and result['is_suspicious']:
                            self.print_result(result)
            
            # MOD 2: GitHub repo URL'i
            elif target and JarDownloader.is_url(target) and JarDownloader.is_github_repo(target):
                print(f"{Fore.CYAN}🌐 GITHUB REPO TESPİT EDİLDİ!{Style.RESET_ALL}")
                print(f"{Fore.WHITE}   {target}{Style.RESET_ALL}\n")
                
                print(f"{Fore.YELLOW}📦 Repo'daki JAR dosyaları aranıyor...{Style.RESET_ALL}\n")
                
                jar_urls = JarDownloader.find_jars_in_github_repo(target, verbose=args.verbose)
                
                if not jar_urls:
                    print(f"{Fore.YELLOW}⚠ Repo'da JAR dosyası bulunamadı{Style.RESET_ALL}\n")
                else:
                    print(f"\n{Fore.GREEN}✓ {len(jar_urls)} JAR dosyası bulundu!{Style.RESET_ALL}\n")
                    print(f"{Fore.CYAN}🔍 JAR'lar indiriliyor ve taranıyor...{Style.RESET_ALL}\n")
                    
                    for i, url in enumerate(jar_urls, 1):
                        print(f"{Fore.WHITE}[{i}/{len(jar_urls)}] {os.path.basename(url)}{Style.RESET_ALL}")
                        temp_file = None
                        try:
                            temp_file = JarDownloader.download_jar(url, verbose=args.verbose)
                            result = scanner.scan_jar(temp_file)
                            result['filename'] = os.path.basename(url)  # Güzel isim
                            all_results.append(result)
                            
                            if result['is_suspicious']:
                                self.print_result(result)
                            elif not args.verbose:
                                print(f"{Fore.GREEN}  ✓ Temiz{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}  ❌ Hata: {e}{Style.RESET_ALL}")
                        finally:
                            if temp_file:
                                JarDownloader.cleanup(temp_file)
                        print()
                
                # Repo taraması sonrası bilgisayarı da tara
                print(f"\n{Fore.CYAN}{'='*60}")
                print(f"🖥️  BİLGİSAYARINIZDAKİ JAR'LAR DA TARANACAK...")
                print(f"{'='*60}{Style.RESET_ALL}\n")
                
                jar_files = SystemScanner.scan_system(verbose=args.verbose)
                
                if jar_files:
                    print(f"\n{Fore.CYAN}📦 {len(jar_files)} JAR dosyası bulundu, taranıyor...{Style.RESET_ALL}\n")
                    
                    for jar_file in jar_files:
                        result = scanner.scan_jar(jar_file)
                        all_results.append(result)
                        if result['is_suspicious']:
                            self.print_result(result)
            
            # MOD 3: Direkt JAR dosyası URL'i
            elif target and JarDownloader.is_url(target):
                print(f"{Fore.CYAN}🌐 URL'den indiriliyor: {target}{Style.RESET_ALL}\n")
                temp_file = None
                try:
                    temp_file = JarDownloader.download_jar(target, verbose=args.verbose)
                    print(f"{Fore.GREEN}✓ İndirme tamamlandı{Style.RESET_ALL}\n")
                    print(f"{Fore.CYAN}🔍 Dosya taranıyor...{Style.RESET_ALL}\n")
                    result = scanner.scan_jar(temp_file)
                    all_results.append(result)
                    self.print_result(result)
                finally:
                    if temp_file:
                        JarDownloader.cleanup(temp_file)
            
            # MOD 4: Lokal dosya
            elif target and os.path.isfile(target):
                print(f"{Fore.CYAN}🔍 Dosya taranıyor: {target}{Style.RESET_ALL}\n")
                result = scanner.scan_jar(target)
                all_results.append(result)
                self.print_result(result)
            
            # MOD 5: Lokal dizin
            elif target and os.path.isdir(target) or args.directory:
                directory = target or args.directory
                print(f"{Fore.CYAN}🔍 Dizin taranıyor: {directory}{Style.RESET_ALL}")
                if args.recursive:
                    print(f"{Fore.YELLOW}📁 Alt dizinler dahil{Style.RESET_ALL}")
                
                results = scanner.scan_directory(directory, recursive=args.recursive)
                all_results.extend(results)
                
                for result in results:
                    self.print_result(result)
            
            else:
                print(f"{Fore.RED}❌ Hata: Geçersiz hedef veya dosya/dizin bulunamadı{Style.RESET_ALL}\n")
                self.parser.print_help()
                sys.exit(1)
            
            # Özet yazdır
            stats = scanner.get_stats()
            self.print_summary(stats)
            
            # Exit code: şüpheli dosya varsa 1
            sys.exit(1 if stats['total_detected'] > 0 else 0)
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}⚠️  Tarama kullanıcı tarafından iptal edildi{Style.RESET_ALL}")
            sys.exit(130)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Beklenmeyen hata: {e}{Style.RESET_ALL}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)


def main():
    """Ana giriş noktası"""
    cli = CLI()
    cli.run()


if __name__ == '__main__':
    main()
