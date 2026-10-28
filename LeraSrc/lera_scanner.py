import zipfile
import os
from pathlib import Path
from typing import List, Dict, Tuple


class GhostClientSignature:
    SIGNATURES = {
        0: 'Doomsday Client',
        1: 'l.png',
    }

    def __init__(self):
        self.signatures = self.SIGNATURES

    def check_filename_anywhere(self, filename: str) -> bool:
        return any(sig.lower() in filename.lower() for sig in self.signatures.values())

    def check_filename_exact(self, filename: str) -> bool:
        return any(sig.lower() == filename.lower() for sig in self.signatures.values())

    def check_filepath(self, filepath: str) -> Tuple[bool, str]:
        parts = filepath.replace('/', '\\').split('\\')
        for part in parts:
            if self.check_filename_exact(part):
                return True, part
        return False, ''


class JarScanner:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.signature = GhostClientSignature()

    def scan_jar(self, jar_path: str) -> Dict:
        result = {
            'path': jar_path,
            'filename': os.path.basename(jar_path),
            'is_suspicious': False,
            'found_files': [],
            'all_files_scanned': 0,
            'error': None,
        }

        try:
            with zipfile.ZipFile(jar_path, 'r') as jar:
                for name in jar.namelist():
                    result['all_files_scanned'] += 1

                    match, matched = self.signature.check_filepath(name)
                    if match:
                        result['found_files'].append(matched)
                        result['is_suspicious'] = True

                    base = os.path.basename(name)
                    if self.signature.check_filename_anywhere(base):
                        if base not in result['found_files']:
                            result['found_files'].append(base)
                        result['is_suspicious'] = True

        except zipfile.BadZipFile:
            result['error'] = 'Geçerli bir JAR/ZIP dosyası değil'
        except Exception as e:
            result['error'] = str(e)

        return result


import os
import ctypes
import ctypes.wintypes


class MemoryScanner:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.signature = GhostClientSignature()

    def is_admin(self) -> bool:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False

    def get_java_processes(self) -> List[Dict]:
        try:
            import psutil
        except ImportError:
            return []

        processes = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'create_time']):
                try:
                    name = (proc.info['name'] or '').lower()
                    if 'java' in name:
                        processes.append(proc.info)
                except Exception:
                    continue
        except Exception as e:
            if self.verbose:
                print(f'Process enumeration error: {e}')
        return processes

    def scan_process_memory(self, pid: int) -> Dict:
        result = {'pid': pid, 'scanned': 0, 'detections': [], 'error': None}

        if not self.is_admin():
            result['error'] = 'Admin yetkisi gerekli'
            return result

        PROCESS_VM_READ = 0x0010
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_VM_READ, False, pid)
        if not handle:
            result['error'] = 'Process açılamadı'
            return result

        try:
            for sig_name in self.signature.signatures.values():
                sig_bytes = sig_name.encode('utf-8', 'ignore')
                result['scanned'] += len(sig_bytes)
        finally:
            ctypes.windll.kernel32.CloseHandle(handle)

        return result

    def scan_all(self) -> List[Dict]:
        if not self.is_admin():
            print('Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!')
            return []

        results = []
        for proc in self.get_java_processes():
            if self.verbose:
                print(f'Taranıyor: PID {proc["pid"]} - {proc["name"]}')
            results.append(self.scan_process_memory(proc['pid']))
        return results


import os
import glob


class PrefetchScanner:

    PREFETCH_DIR = r'C:\Windows\Prefetch'

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.signature = GhostClientSignature()

    def is_admin(self) -> bool:
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False

    def can_access_prefetch(self) -> bool:
        try:
            os.listdir(self.PREFETCH_DIR)
            return True
        except Exception:
            return False

    def find_jar_references(self) -> List[Dict]:
        if not self.is_admin():
            print('Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!')
            return []

        if not self.can_access_prefetch():
            print(f'Prefetch klasörüne erişim yok: {self.PREFETCH_DIR}')
            return []

        results = []
        for pf_file in glob.glob(os.path.join(self.PREFETCH_DIR, '*.pf')):
            try:
                with open(pf_file, 'rb') as f:
                    data = f.read()
                refs = []
                for sig in self.signature.signatures.values():
                    if sig.encode('utf-16-le', 'ignore') in data or \
                       sig.encode('ascii', 'ignore') in data:
                        refs.append(sig)
                if refs:
                    results.append({'prefetch': os.path.basename(pf_file), 'refs': refs})
            except Exception:
                continue
        return results


import os
import string


class SystemScanner:

    def get_all_drives(self) -> List[str]:
        drives = []
        for letter in string.ascii_uppercase:
            path = f'{letter}:\\'
            if os.path.exists(path):
                drives.append(path)
        return drives

    def scan_all(self, verbose: bool = False) -> List[str]:
        jars = []
        for drive in self.get_all_drives():
            for root, dirs, files in os.walk(drive, onerror=lambda e: None):
                for file in files:
                    if file.lower().endswith('.jar'):
                        jars.append(os.path.join(root, file))
                        if verbose:
                            print(f'Bulundu: {os.path.join(root, file)}')
        return jars


def run_direct_scan():
    print('\nLeraScanner - Direct Auto Scan')
    print('Menü yok, direkt çalışır, sadece sonuçları gösterir\n')

    try:
        sys_scanner = SystemScanner()
        jars = sys_scanner.scan_all()

        jar_scanner = JarScanner()
        suspicious = []
        for jar in jars:
            res = jar_scanner.scan_jar(jar)
            if res['is_suspicious']:
                suspicious.append(res)

        mem = MemoryScanner()
        mem_results = mem.scan_all()

        prefetch = PrefetchScanner()
        pf_results = prefetch.find_jar_references()

        print(f'\nTaranan JAR sayısı: {len(jars)}')
        print(f'Şüpheli JAR sayısı: {len(suspicious)}')
        for s in suspicious:
            print(f'  ! {s["path"]}  -> {s["found_files"]}')

    except KeyboardInterrupt:
        print('\nTarama iptal edildi')


if __name__ == '__main__':
    run_direct_scan()
