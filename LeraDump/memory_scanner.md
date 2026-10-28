# memory_scanner

_Kaynak: scanner\memory_scanner.py - 167 satir_

```python
"""
RAM Memory Scanner - Java process'lerinde ghost client imzalarını arar
"""

import ctypes
import ctypes.wintypes as wintypes
import psutil
from typing import List, Dict, Optional

# Windows API sabitleri
PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400
MEM_COMMIT = 0x1000
PAGE_READONLY = 0x02
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READ = 0x20
PAGE_EXECUTE_READWRITE = 0x40


class MemoryScanner:
    """Java process'lerini tarayıp memory'de ghost client imzalarını arar"""
    
    # Ghost client imzaları (obfuscated strings)
    SIGNATURES = [
        b'Doomsday',
        b'doomsday',
        b'DOOMSDAY',
        # Daha fazla imza eklenebilir
    ]
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.kernel32 = ctypes.windll.kernel32
        self.is_admin = self._check_admin()
    
    def _check_admin(self) -> bool:
        """Admin yetkisi kontrolü"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    
    def find_java_processes(self) -> List[Dict]:
        """Çalışan Java process'lerini bul"""
        java_processes = []
        
        try:
            for proc in psutil.process_iter(['pid', 'name', 'create_time']):
                try:
                    name = proc.info['name'].lower()
                    if 'java' in name or 'javaw' in name:
                        java_processes.append({
                            'pid': proc.info['pid'],
                            'name': proc.info['name'],
                            'create_time': proc.info['create_time']
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception as e:
            if self.verbose:
                print(f"Process enumeration error: {e}")
        
        return java_processes
    
    def scan_process_memory(self, pid: int) -> Dict:
        """Bir process'in memory'sini tara"""
        result = {
            'pid': pid,
            'scanned': False,
            'detections': [],
            'error': None
        }
        
        if not self.is_admin:
            result['error'] = 'Admin yetkisi gerekli'
            return result
        
        try:
            # Process handle aç
            handle = self.kernel32.OpenProcess(
                PROCESS_VM_READ | PROCESS_QUERY_INFORMATION,
                False,
                pid
            )
            
            if not handle:
                result['error'] = 'Process açılamadı'
                return result
            
            try:
                # Memory'yi tara
                address = 0
                max_address = 0x7FFFFFFF0000  # 64-bit max user address
                chunk_size = 1024 * 1024 * 10  # 10MB chunks
                
                while address < max_address:
                    # Memory info al
                    mbi = wintypes.MEMORY_BASIC_INFORMATION()
                    if self.kernel32.VirtualQueryEx(
                        handle,
                        ctypes.c_void_p(address),
                        ctypes.byref(mbi),
                        ctypes.sizeof(mbi)
                    ) == 0:
                        break
                    
                    # Sadece commit edilmiş, readable memory'yi oku
                    if (mbi.State == MEM_COMMIT and 
                        mbi.Protect in [PAGE_READONLY, PAGE_READWRITE, PAGE_EXECUTE_READ, PAGE_EXECUTE_READWRITE] and
                        mbi.RegionSize < 100 * 1024 * 1024):  # Max 100MB
                        
                        try:
                            # Memory'yi oku
                            buffer = (ctypes.c_char * mbi.RegionSize)()
                            bytes_read = ctypes.c_size_t(0)
                            
                            if self.kernel32.ReadProcessMemory(
                                handle,
                                ctypes.c_void_p(address),
                                buffer,
                                mbi.RegionSize,
                                ctypes.byref(bytes_read)
                            ):
                                # İmzaları ara
                                data = bytes(buffer[:bytes_read.value])
                                for signature in self.SIGNATURES:
                                    if signature in data:
                                        result['detections'].append({
                                            'signature': signature.decode('utf-8', errors='ignore'),
                                            'address': hex(address)
                                        })
                        except:
                            pass
                    
                    address += mbi.RegionSize
                
                result['scanned'] = True
                
            finally:
                self.kernel32.CloseHandle(handle)
        
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def scan_all(self) -> List[Dict]:
        """Tüm Java process'lerini tara"""
        if not self.is_admin:
            return [{
                'error': 'Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!',
                'processes': []
            }]
        
        processes = self.find_java_processes()
        results = []
        
        for proc in processes:
            if self.verbose:
                print(f"Taranıyor: PID {proc['pid']} - {proc['name']}")
            
            scan_result = self.scan_process_memory(proc['pid'])
            scan_result['name'] = proc['name']
            results.append(scan_result)
        
        return results
```
