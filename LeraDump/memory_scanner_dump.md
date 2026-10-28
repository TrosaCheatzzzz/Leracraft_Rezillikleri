### CODE OBJECT: <module>  (file=scanner\memory_scanner.py, line=1)
# consts:
  STR: "\nRAM Memory Scanner - Java process'lerinde ghost client imzalar²n² arar\n"
  STR: 'MemoryScanner'
# names: ('__doc__', 'ctypes', 'ctypes.wintypes', 'wintypes', 'psutil', 'typing', 'List', 'Dict', 'Optional', 'PROCESS_VM_READ', 'PROCESS_QUERY_INFORMATION', 'MEM_COMMIT', 'PAGE_READONLY', 'PAGE_READWRITE', 'PAGE_EXECUTE_READ', 'PAGE_EXECUTE_READWRITE', 'MemoryScanner')
# varnames: ()
# bytecode:
       0 RESUME                       
       2 LOAD_CONST                   "\nRAM Memory Scanner - Java process'lerinde ghost client imzalar²n² arar\n"
       4 STORE_NAME                   __doc__
       6 LOAD_SMALL_INT               
       8 LOAD_CONST                   None
      10 IMPORT_NAME                  ctypes
      12 STORE_NAME                   ctypes
      14 LOAD_SMALL_INT               
      16 LOAD_CONST                   None
      18 IMPORT_NAME                  ctypes.wintypes
      20 IMPORT_FROM                  wintypes
      22 STORE_NAME                   wintypes
      24 POP_TOP                      
      26 LOAD_SMALL_INT               
      28 LOAD_CONST                   None
      30 IMPORT_NAME                  psutil
      32 STORE_NAME                   psutil
      34 LOAD_SMALL_INT               
      36 LOAD_CONST                   ('List', 'Dict', 'Optional')
      38 IMPORT_NAME                  typing
      40 IMPORT_FROM                  List
      42 STORE_NAME                   List
      44 IMPORT_FROM                  Dict
      46 STORE_NAME                   Dict
      48 IMPORT_FROM                  Optional
      50 STORE_NAME                   Optional
      52 POP_TOP                      
      54 LOAD_SMALL_INT               
      56 STORE_NAME                   PROCESS_VM_READ
      58 LOAD_CONST                   1024
      60 STORE_NAME                   PROCESS_QUERY_INFORMATION
      62 LOAD_CONST                   4096
      64 STORE_NAME                   MEM_COMMIT
      66 LOAD_SMALL_INT               
      68 STORE_NAME                   PAGE_READONLY
      70 LOAD_SMALL_INT               
      72 STORE_NAME                   PAGE_READWRITE
      74 LOAD_SMALL_INT               
      76 STORE_NAME                   PAGE_EXECUTE_READ
      78 LOAD_SMALL_INT               
      80 STORE_NAME                   PAGE_EXECUTE_READWRITE
      82 LOAD_BUILD_CLASS             
      84 PUSH_NULL                    
      86 LOAD_CONST                   <code object MemoryScanner at 0x000001C473D91790, file "scanner\memory_scanner.py", line 20>
      88 MAKE_FUNCTION                
      90 LOAD_CONST                   'MemoryScanner'
      92 CALL                         
     100 STORE_NAME                   MemoryScanner
     102 LOAD_CONST                   None
     104 RETURN_VALUE                 

  ### CODE OBJECT: MemoryScanner  (file=scanner\memory_scanner.py, line=20)
  # consts:
    STR: 'MemoryScanner'
    STR: "Java process'lerini taray²p memory'de ghost client imzalar²n² arar"
  # names: ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', 'SIGNATURES', '__init__', '_check_admin', 'find_java_processes', 'scan_process_memory', 'scan_all', '__static_attributes__', '__classdictcell__')
  # varnames: ()
  # bytecode:
         0 MAKE_CELL                    __classdict__
         2 RESUME                       
         4 LOAD_NAME                    __name__
         6 STORE_NAME                   __module__
         8 LOAD_CONST                   'MemoryScanner'
        10 STORE_NAME                   __qualname__
        12 LOAD_SMALL_INT               
        14 STORE_NAME                   __firstlineno__
        16 LOAD_LOCALS                  
        18 STORE_DEREF                  __classdict__
        20 LOAD_CONST                   "Java process'lerini taray²p memory'de ghost client imzalar²n² arar"
        22 STORE_NAME                   __doc__
        24 BUILD_LIST                   
        26 LOAD_CONST                   (b'Doomsday', b'doomsday', b'DOOMSDAY')
        28 LIST_EXTEND                  
        30 STORE_NAME                   SIGNATURES
        32 LOAD_CONST                   (False,)
        34 LOAD_FAST_BORROW             __classdict__
        36 BUILD_TUPLE                  
        38 LOAD_CONST                   <code object __annotate__ at 0x000001C474000D50, file "scanner\memory_scanner.py", line 31>
        40 MAKE_FUNCTION                
        42 SET_FUNCTION_ATTRIBUTE       closure
        44 LOAD_CONST                   <code object __init__ at 0x000001C474028FF0, file "scanner\memory_scanner.py", line 31>
        46 MAKE_FUNCTION                
        48 SET_FUNCTION_ATTRIBUTE       annotate
        50 SET_FUNCTION_ATTRIBUTE       defaults
        52 STORE_NAME                   __init__
        54 LOAD_FAST_BORROW             __classdict__
        56 BUILD_TUPLE                  
        58 LOAD_CONST                   <code object __annotate__ at 0x000001C4740014D0, file "scanner\memory_scanner.py", line 36>
        60 MAKE_FUNCTION                
        62 SET_FUNCTION_ATTRIBUTE       closure
        64 LOAD_CONST                   <code object _check_admin at 0x000001C4740191B0, file "scanner\memory_scanner.py", line 36>
        66 MAKE_FUNCTION                
        68 SET_FUNCTION_ATTRIBUTE       annotate
        70 STORE_NAME                   _check_admin
        72 LOAD_FAST_BORROW             __classdict__
        74 BUILD_TUPLE                  
        76 LOAD_CONST                   <code object __annotate__ at 0x000001C473FFB130, file "scanner\memory_scanner.py", line 43>
        78 MAKE_FUNCTION                
        80 SET_FUNCTION_ATTRIBUTE       closure
        82 LOAD_CONST                   <code object find_java_processes at 0x000001C473BA8D60, file "scanner\memory_scanner.py", line 43>
        84 MAKE_FUNCTION                
        86 SET_FUNCTION_ATTRIBUTE       annotate
        88 STORE_NAME                   find_java_processes
        90 LOAD_FAST_BORROW             __classdict__
        92 BUILD_TUPLE                  
        94 LOAD_CONST                   <code object __annotate__ at 0x000001C473FFAD30, file "scanner\memory_scanner.py", line 65>
        96 MAKE_FUNCTION                
        98 SET_FUNCTION_ATTRIBUTE       closure
       100 LOAD_CONST                   <code object scan_process_memory at 0x000001C474196FF0, file "scanner\memory_scanner.py", line 65>
       102 MAKE_FUNCTION                
       104 SET_FUNCTION_ATTRIBUTE       annotate
       106 STORE_NAME                   scan_process_memory
       108 LOAD_FAST_BORROW             __classdict__
       110 BUILD_TUPLE                  
       112 LOAD_CONST                   <code object __annotate__ at 0x000001C473FFAC30, file "scanner\memory_scanner.py", line 147>
       114 MAKE_FUNCTION                
       116 SET_FUNCTION_ATTRIBUTE       closure
       118 LOAD_CONST                   <code object scan_all at 0x000001C4740BEAC0, file "scanner\memory_scanner.py", line 147>
       120 MAKE_FUNCTION                
       122 SET_FUNCTION_ATTRIBUTE       annotate
       124 STORE_NAME                   scan_all
       126 LOAD_CONST                   ('is_admin', 'kernel32', 'verbose')
       128 STORE_NAME                   __static_attributes__
       130 LOAD_FAST_BORROW             __classdict__
       132 STORE_NAME                   __classdictcell__
       134 LOAD_CONST                   None
       136 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\memory_scanner.py, line=31)
    # consts:
      STR: 'verbose'
    # names: ('bool',)
    # varnames: ('format',)
    # bytecode:
           0 COPY_FREE_VARS               
           2 RESUME                       
           4 LOAD_FAST_BORROW             format
           6 LOAD_SMALL_INT               
           8 COMPARE_OP                   >
          12 POP_JUMP_IF_FALSE            to L1
          16 NOT_TAKEN                    
          18 LOAD_COMMON_CONSTANT         NotImplementedError
          20 RAISE_VARARGS                
          22 LOAD_CONST                   'verbose'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    bool
          28 BUILD_MAP                    
          30 RETURN_VALUE                 

    ### CODE OBJECT: __init__  (file=scanner\memory_scanner.py, line=31)
    # consts:
    # names: ('verbose', 'ctypes', 'windll', 'kernel32', '_check_admin', 'is_admin')
    # varnames: ('self', 'verbose')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW_LOAD_FAST_BORROW verbose, self
           4 STORE_ATTR                   verbose
          14 LOAD_GLOBAL                  ctypes
          24 LOAD_ATTR                    windll
          44 LOAD_ATTR                    kernel32
          64 LOAD_FAST_BORROW             self
          66 STORE_ATTR                   kernel32
          76 LOAD_FAST_BORROW             self
          78 LOAD_ATTR                    _check_admin + NULL|self
          98 CALL                         
         106 LOAD_FAST_BORROW             self
         108 STORE_ATTR                   is_admin
         118 LOAD_CONST                   None
         120 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\memory_scanner.py, line=36)
    # consts:
      STR: 'return'
    # names: ('bool',)
    # varnames: ('format',)
    # bytecode:
           0 COPY_FREE_VARS               
           2 RESUME                       
           4 LOAD_FAST_BORROW             format
           6 LOAD_SMALL_INT               
           8 COMPARE_OP                   >
          12 POP_JUMP_IF_FALSE            to L1
          16 NOT_TAKEN                    
          18 LOAD_COMMON_CONSTANT         NotImplementedError
          20 RAISE_VARARGS                
          22 LOAD_CONST                   'return'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    bool
          28 BUILD_MAP                    
          30 RETURN_VALUE                 

    ### CODE OBJECT: _check_admin  (file=scanner\memory_scanner.py, line=36)
    # consts:
      STR: 'Admin yetkisi kontrol³'
    # names: ('ctypes', 'windll', 'shell32', 'IsUserAnAdmin')
    # varnames: ('self',)
    # bytecode:
           0 RESUME                       
           2 NOP                          
           4 LOAD_GLOBAL                  ctypes
          14 LOAD_ATTR                    windll
          34 LOAD_ATTR                    shell32
          54 LOAD_ATTR                    IsUserAnAdmin + NULL|self
          74 CALL                         
          82 LOAD_SMALL_INT               
          84 COMPARE_OP                   !=
          88 RETURN_VALUE                 
          90 PUSH_EXC_INFO                
          92 POP_TOP                      
          94 POP_EXCEPT                   
          96 LOAD_CONST                   False
          98 RETURN_VALUE                 
         100 COPY                         
         102 POP_EXCEPT                   
         104 RERAISE                      

    ### CODE OBJECT: __annotate__  (file=scanner\memory_scanner.py, line=43)
    # consts:
      STR: 'return'
    # names: ('List', 'Dict')
    # varnames: ('format',)
    # bytecode:
           0 COPY_FREE_VARS               
           2 RESUME                       
           4 LOAD_FAST_BORROW             format
           6 LOAD_SMALL_INT               
           8 COMPARE_OP                   >
          12 POP_JUMP_IF_FALSE            to L1
          16 NOT_TAKEN                    
          18 LOAD_COMMON_CONSTANT         NotImplementedError
          20 RAISE_VARARGS                
          22 LOAD_CONST                   'return'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    List
          28 LOAD_DEREF                   __classdict__
          30 LOAD_FROM_DICT_OR_GLOBALS    Dict
          32 BINARY_OP                    []
          44 BUILD_MAP                    
          46 RETURN_VALUE                 

    ### CODE OBJECT: find_java_processes  (file=scanner\memory_scanner.py, line=43)
    # consts:
      STR: "Ãal²■an Java process'lerini bul"
      STR: 'pid'
      STR: 'name'
      STR: 'create_time'
      STR: 'java'
      STR: 'javaw'
      STR: 'Process enumeration error: '
    # names: ('psutil', 'process_iter', 'info', 'lower', 'append', 'NoSuchProcess', 'AccessDenied', 'Exception', 'verbose', 'print')
    # varnames: ('self', 'java_processes', 'proc', 'name', 'e')
    # bytecode:
           0 RESUME                       
           2 BUILD_LIST                   
           4 STORE_FAST                   java_processes
           6 NOP                          
           8 LOAD_GLOBAL                  psutil
          18 LOAD_ATTR                    process_iter
          38 PUSH_NULL                    
          40 BUILD_LIST                   
          42 LOAD_CONST                   ('pid', 'name', 'create_time')
          44 LIST_EXTEND                  
          46 CALL                         
          54 GET_ITER                     
          56 FOR_ITER                     to L4
          60 STORE_FAST                   proc
          62 NOP                          
          64 LOAD_FAST_BORROW             proc
          66 LOAD_ATTR                    info
          86 LOAD_CONST                   'name'
          88 BINARY_OP                    []
         100 LOAD_ATTR                    lower + NULL|self
         120 CALL                         
         128 STORE_FAST                   name
         130 LOAD_CONST                   'java'
         132 LOAD_FAST_BORROW             name
         134 CONTAINS_OP                  in
         138 POP_JUMP_IF_TRUE             to L2
         142 NOT_TAKEN                    
         144 LOAD_CONST                   'javaw'
         146 LOAD_FAST_BORROW             name
         148 CONTAINS_OP                  in
         152 POP_JUMP_IF_FALSE            to L3
         156 NOT_TAKEN                    
         158 LOAD_FAST_BORROW             java_processes
         160 LOAD_ATTR                    append + NULL|self
         180 LOAD_CONST                   'pid'
         182 LOAD_FAST_BORROW             proc
         184 LOAD_ATTR                    info
         204 LOAD_CONST                   'pid'
         206 BINARY_OP                    []
         218 LOAD_CONST                   'name'
         220 LOAD_FAST_BORROW             proc
         222 LOAD_ATTR                    info
         242 LOAD_CONST                   'name'
         244 BINARY_OP                    []
         256 LOAD_CONST                   'create_time'
         258 LOAD_FAST_BORROW             proc
         260 LOAD_ATTR                    info
         280 LOAD_CONST                   'create_time'
         282 BINARY_OP                    []
         294 BUILD_MAP                    
         296 CALL                         
         304 POP_TOP                      
         306 JUMP_BACKWARD                to L1
         310 JUMP_BACKWARD                to L1
         314 END_FOR                      
         316 POP_ITER                     
         318 LOAD_FAST_BORROW             java_processes
         320 RETURN_VALUE                 
         322 PUSH_EXC_INFO                
         324 LOAD_GLOBAL                  psutil
         334 LOAD_ATTR                    NoSuchProcess
         354 LOAD_GLOBAL                  psutil
         364 LOAD_ATTR                    AccessDenied
         384 BUILD_TUPLE                  
         386 CHECK_EXC_MATCH              
         388 POP_JUMP_IF_FALSE            to L5
         392 NOT_TAKEN                    
         394 POP_TOP                      
         396 POP_EXCEPT                   
         398 JUMP_BACKWARD                to L1
         402 RERAISE                      
         404 COPY                         
         406 POP_EXCEPT                   
         408 RERAISE                      
         410 PUSH_EXC_INFO                
         412 LOAD_GLOBAL                  Exception
         422 CHECK_EXC_MATCH              
         424 POP_JUMP_IF_FALSE            to L7
         428 NOT_TAKEN                    
         430 STORE_FAST                   e
         432 LOAD_FAST                    self
         434 LOAD_ATTR                    verbose
         454 TO_BOOL                      
         462 POP_JUMP_IF_FALSE            to L6
         466 NOT_TAKEN                    
         468 LOAD_GLOBAL                  print + NULL
         478 LOAD_CONST                   'Process enumeration error: '
         480 LOAD_FAST                    e
         482 FORMAT_SIMPLE                
         484 BUILD_STRING                 
         486 CALL                         
         494 POP_TOP                      
         496 POP_EXCEPT                   
         498 LOAD_CONST                   None
         500 STORE_FAST                   e
         502 DELETE_FAST                  e
         504 LOAD_FAST                    java_processes
         506 RETURN_VALUE                 
         508 LOAD_CONST                   None
         510 STORE_FAST                   e
         512 DELETE_FAST                  e
         514 RERAISE                      
         516 RERAISE                      
         518 COPY                         
         520 POP_EXCEPT                   
         522 RERAISE                      

    ### CODE OBJECT: __annotate__  (file=scanner\memory_scanner.py, line=65)
    # consts:
      STR: 'pid'
      STR: 'return'
    # names: ('int', 'Dict')
    # varnames: ('format',)
    # bytecode:
           0 COPY_FREE_VARS               
           2 RESUME                       
           4 LOAD_FAST_BORROW             format
           6 LOAD_SMALL_INT               
           8 COMPARE_OP                   >
          12 POP_JUMP_IF_FALSE            to L1
          16 NOT_TAKEN                    
          18 LOAD_COMMON_CONSTANT         NotImplementedError
          20 RAISE_VARARGS                
          22 LOAD_CONST                   'pid'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    int
          28 LOAD_CONST                   'return'
          30 LOAD_DEREF                   __classdict__
          32 LOAD_FROM_DICT_OR_GLOBALS    Dict
          34 BUILD_MAP                    
          36 RETURN_VALUE                 

    ### CODE OBJECT: scan_process_memory  (file=scanner\memory_scanner.py, line=65)
    # consts:
      STR: "Bir process'in memory'sini tara"
      STR: 'pid'
      STR: 'scanned'
      STR: 'detections'
      STR: 'error'
      STR: 'Admin yetkisi gerekli'
      STR: 'Process a²lamad²'
      STR: 'signature'
      STR: 'utf-8'
      STR: 'ignore'
      STR: 'address'
    # names: ('is_admin', 'kernel32', 'OpenProcess', 'PROCESS_VM_READ', 'PROCESS_QUERY_INFORMATION', 'wintypes', 'MEMORY_BASIC_INFORMATION', 'VirtualQueryEx', 'ctypes', 'c_void_p', 'byref', 'sizeof', 'State', 'MEM_COMMIT', 'Protect', 'PAGE_READONLY', 'PAGE_READWRITE', 'PAGE_EXECUTE_READ', 'PAGE_EXECUTE_READWRITE', 'RegionSize', 'c_char', 'c_size_t', 'ReadProcessMemory', 'bytes', 'value', 'SIGNATURES', 'append', 'decode', 'hex', 'CloseHandle', 'Exception', 'str')
    # varnames: ('self', 'pid', 'result', 'handle', 'address', 'max_address', 'chunk_size', 'mbi', 'buffer', 'bytes_read', 'data', 'signature', 'e')
    # bytecode:
           0 RESUME                       
           2 LOAD_CONST                   'pid'
           4 LOAD_FAST_BORROW             pid
           6 LOAD_CONST                   'scanned'
           8 LOAD_CONST                   False
          10 LOAD_CONST                   'detections'
          12 BUILD_LIST                   
          14 LOAD_CONST                   'error'
          16 LOAD_CONST                   None
          18 BUILD_MAP                    
          20 STORE_FAST                   result
          22 LOAD_FAST_BORROW             self
          24 LOAD_ATTR                    is_admin
          44 TO_BOOL                      
          52 POP_JUMP_IF_TRUE             to L1
          56 NOT_TAKEN                    
          58 LOAD_CONST                   'Admin yetkisi gerekli'
          60 LOAD_FAST_BORROW             result
          62 LOAD_CONST                   'error'
          64 STORE_SUBSCR                 
          68 LOAD_FAST_BORROW             result
          70 RETURN_VALUE                 
          72 NOP                          
          74 LOAD_FAST_BORROW             self
          76 LOAD_ATTR                    kernel32
          96 LOAD_ATTR                    OpenProcess + NULL|self
         116 LOAD_GLOBAL                  PROCESS_VM_READ
         126 LOAD_GLOBAL                  PROCESS_QUERY_INFORMATION
         136 BINARY_OP                    |
         148 LOAD_CONST                   False
         150 LOAD_FAST_BORROW             pid
         152 CALL                         
         160 STORE_FAST                   handle
         162 LOAD_FAST_BORROW             handle
         164 TO_BOOL                      
         172 POP_JUMP_IF_TRUE             to L2
         176 NOT_TAKEN                    
         178 LOAD_CONST                   'Process a²lamad²'
         180 LOAD_FAST_BORROW             result
         182 LOAD_CONST                   'error'
         184 STORE_SUBSCR                 
         188 LOAD_FAST_BORROW             result
         190 RETURN_VALUE                 
         192 NOP                          
         194 LOAD_SMALL_INT               
         196 STORE_FAST                   address
         198 LOAD_CONST                   140737488289792
         200 STORE_FAST                   max_address
         202 LOAD_CONST                   10485760
         204 STORE_FAST                   chunk_size
         206 LOAD_FAST_BORROW_LOAD_FAST_BORROW address, max_address
         208 COMPARE_OP                   bool(<)
         212 EXTENDED_ARG                 
         214 POP_JUMP_IF_FALSE            to L9
         218 NOT_TAKEN                    
         220 LOAD_GLOBAL                  wintypes
         230 LOAD_ATTR                    MEMORY_BASIC_INFORMATION
         250 PUSH_NULL                    
         252 CALL                         
         260 STORE_FAST                   mbi
         262 LOAD_FAST_BORROW             self
         264 LOAD_ATTR                    kernel32
         284 LOAD_ATTR                    VirtualQueryEx + NULL|self
         304 LOAD_FAST_BORROW             handle
         306 LOAD_GLOBAL                  ctypes
         316 LOAD_ATTR                    c_void_p
         336 PUSH_NULL                    
         338 LOAD_FAST_BORROW             address
         340 CALL                         
         348 LOAD_GLOBAL                  ctypes
         358 LOAD_ATTR                    byref
         378 PUSH_NULL                    
         380 LOAD_FAST_BORROW             mbi
         382 CALL                         
         390 LOAD_GLOBAL                  ctypes
         400 LOAD_ATTR                    sizeof
         420 PUSH_NULL                    
         422 LOAD_FAST_BORROW             mbi
         424 CALL                         
         432 CALL                         
         440 LOAD_SMALL_INT               
         442 COMPARE_OP                   bool(==)
         446 POP_JUMP_IF_FALSE            to L4
         450 NOT_TAKEN                    
         452 EXTENDED_ARG                 
         454 JUMP_FORWARD                 to L9
         456 LOAD_FAST_BORROW             mbi
         458 LOAD_ATTR                    State
         478 LOAD_GLOBAL                  MEM_COMMIT
         488 COMPARE_OP                   bool(==)
         492 EXTENDED_ARG                 
         494 POP_JUMP_IF_FALSE            to L8
         498 NOT_TAKEN                    
         500 LOAD_FAST_BORROW             mbi
         502 LOAD_ATTR                    Protect
         522 LOAD_GLOBAL                  PAGE_READONLY
         532 LOAD_GLOBAL                  PAGE_READWRITE
         542 LOAD_GLOBAL                  PAGE_EXECUTE_READ
         552 LOAD_GLOBAL                  PAGE_EXECUTE_READWRITE
         562 BUILD_TUPLE                  
         564 CONTAINS_OP                  in
         568 EXTENDED_ARG                 
         570 POP_JUMP_IF_FALSE            to L8
         574 NOT_TAKEN                    
         576 LOAD_FAST_BORROW             mbi
         578 LOAD_ATTR                    RegionSize
         598 LOAD_CONST                   104857600
         600 COMPARE_OP                   bool(<)
         604 POP_JUMP_IF_FALSE            to L8
         608 NOT_TAKEN                    
         610 NOP                          
         612 LOAD_GLOBAL                  ctypes
         622 LOAD_ATTR                    c_char
         642 LOAD_FAST_BORROW             mbi
         644 LOAD_ATTR                    RegionSize
         664 BINARY_OP                    *
         676 PUSH_NULL                    
         678 CALL                         
         686 STORE_FAST                   buffer
         688 LOAD_GLOBAL                  ctypes
         698 LOAD_ATTR                    c_size_t
         718 PUSH_NULL                    
         720 LOAD_SMALL_INT               
         722 CALL                         
         730 STORE_FAST                   bytes_read
         732 LOAD_FAST_BORROW             self
         734 LOAD_ATTR                    kernel32
         754 LOAD_ATTR                    ReadProcessMemory + NULL|self
         774 LOAD_FAST_BORROW             handle
         776 LOAD_GLOBAL                  ctypes
         786 LOAD_ATTR                    c_void_p
         806 PUSH_NULL                    
         808 LOAD_FAST_BORROW             address
         810 CALL                         
         818 LOAD_FAST_BORROW             buffer
         820 LOAD_FAST_BORROW             mbi
         822 LOAD_ATTR                    RegionSize
         842 LOAD_GLOBAL                  ctypes
         852 LOAD_ATTR                    byref
         872 PUSH_NULL                    
         874 LOAD_FAST_BORROW             bytes_read
         876 CALL                         
         884 CALL                         
         892 TO_BOOL                      
         900 POP_JUMP_IF_FALSE            to L8
         904 NOT_TAKEN                    
         906 LOAD_GLOBAL                  bytes + NULL
         916 LOAD_FAST_BORROW             buffer
         918 LOAD_CONST                   None
         920 LOAD_FAST_BORROW             bytes_read
         922 LOAD_ATTR                    value
         942 BINARY_SLICE                 
         944 CALL                         
         952 STORE_FAST                   data
         954 LOAD_FAST_BORROW             self
         956 LOAD_ATTR                    SIGNATURES
         976 GET_ITER                     
         978 FOR_ITER                     to L7
         982 STORE_FAST                   signature
         984 LOAD_FAST_BORROW_LOAD_FAST_BORROW signature, data
         986 CONTAINS_OP                  in
         990 POP_JUMP_IF_TRUE             to L6
         994 NOT_TAKEN                    
         996 JUMP_BACKWARD                to L5
        1000 LOAD_FAST_BORROW             result
        1002 LOAD_CONST                   'detections'
        1004 BINARY_OP                    []
        1016 LOAD_ATTR                    append + NULL|self
        1036 LOAD_CONST                   'signature'
        1038 LOAD_FAST_BORROW             signature
        1040 LOAD_ATTR                    decode + NULL|self
        1060 LOAD_CONST                   'utf-8'
        1062 LOAD_CONST                   'ignore'
        1064 LOAD_CONST                   ('errors',)
        1066 CALL_KW                      
        1074 LOAD_CONST                   'address'
        1076 LOAD_GLOBAL                  hex + NULL
        1086 LOAD_FAST_BORROW             address
        1088 CALL                         
        1096 BUILD_MAP                    
        1098 CALL                         
        1106 POP_TOP                      
        1108 JUMP_BACKWARD                to L5
        1112 END_FOR                      
        1114 POP_ITER                     
        1116 LOAD_FAST_BORROW_LOAD_FAST_BORROW address, mbi
        1118 LOAD_ATTR                    RegionSize
        1138 BINARY_OP                    +=
        1150 STORE_FAST                   address
        1152 EXTENDED_ARG                 
        1154 JUMP_BACKWARD                to L3
        1158 LOAD_CONST                   True
        1160 LOAD_FAST_BORROW             result
        1162 LOAD_CONST                   'scanned'
        1164 STORE_SUBSCR                 
        1168 LOAD_FAST_BORROW             self
        1170 LOAD_ATTR                    kernel32
        1190 LOAD_ATTR                    CloseHandle + NULL|self
        1210 LOAD_FAST_BORROW             handle
        1212 CALL                         
        1220 POP_TOP                      
        1222 LOAD_FAST_BORROW             result
        1224 RETURN_VALUE                 
        1226 PUSH_EXC_INFO                
        1228 POP_TOP                      
        1230 POP_EXCEPT                   
        1232 JUMP_BACKWARD_NO_INTERRUPT   to L8
        1234 COPY                         
        1236 POP_EXCEPT                   
        1238 RERAISE                      
        1240 PUSH_EXC_INFO                
        1242 LOAD_FAST                    self
        1244 LOAD_ATTR                    kernel32
        1264 LOAD_ATTR                    CloseHandle + NULL|self
        1284 LOAD_FAST                    handle
        1286 CALL                         
        1294 POP_TOP                      
        1296 RERAISE                      
        1298 COPY                         
        1300 POP_EXCEPT                   
        1302 RERAISE                      
        1304 PUSH_EXC_INFO                
        1306 LOAD_GLOBAL                  Exception
        1316 CHECK_EXC_MATCH              
        1318 POP_JUMP_IF_FALSE            to L10
        1322 NOT_TAKEN                    
        1324 STORE_FAST                   e
        1326 LOAD_GLOBAL                  str + NULL
        1336 LOAD_FAST                    e
        1338 CALL                         
        1346 LOAD_FAST                    result
        1348 LOAD_CONST                   'error'
        1350 STORE_SUBSCR                 
        1354 POP_EXCEPT                   
        1356 LOAD_CONST                   None
        1358 STORE_FAST                   e
        1360 DELETE_FAST                  e
        1362 LOAD_FAST                    result
        1364 RETURN_VALUE                 
        1366 LOAD_CONST                   None
        1368 STORE_FAST                   e
        1370 DELETE_FAST                  e
        1372 RERAISE                      
        1374 RERAISE                      
        1376 COPY                         
        1378 POP_EXCEPT                   
        1380 RERAISE                      

    ### CODE OBJECT: __annotate__  (file=scanner\memory_scanner.py, line=147)
    # consts:
      STR: 'return'
    # names: ('List', 'Dict')
    # varnames: ('format',)
    # bytecode:
           0 COPY_FREE_VARS               
           2 RESUME                       
           4 LOAD_FAST_BORROW             format
           6 LOAD_SMALL_INT               
           8 COMPARE_OP                   >
          12 POP_JUMP_IF_FALSE            to L1
          16 NOT_TAKEN                    
          18 LOAD_COMMON_CONSTANT         NotImplementedError
          20 RAISE_VARARGS                
          22 LOAD_CONST                   'return'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    List
          28 LOAD_DEREF                   __classdict__
          30 LOAD_FROM_DICT_OR_GLOBALS    Dict
          32 BINARY_OP                    []
          44 BUILD_MAP                    
          46 RETURN_VALUE                 

    ### CODE OBJECT: scan_all  (file=scanner\memory_scanner.py, line=147)
    # consts:
      STR: "T³m Java process'lerini tara"
      STR: 'error'
      STR: 'Bu ÷zellik iin admin yetkisi ile al²■t²rman²z gerekiyor!'
      STR: 'processes'
      STR: 'Taran²yor: PID '
      STR: 'pid'
      STR: ' - '
      STR: 'name'
    # names: ('is_admin', 'find_java_processes', 'verbose', 'print', 'scan_process_memory', 'append')
    # varnames: ('self', 'processes', 'results', 'proc', 'scan_result')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW             self
           4 LOAD_ATTR                    is_admin
          24 TO_BOOL                      
          32 POP_JUMP_IF_TRUE             to L1
          36 NOT_TAKEN                    
          38 LOAD_CONST                   'error'
          40 LOAD_CONST                   'Bu ÷zellik iin admin yetkisi ile al²■t²rman²z gerekiyor!'
          42 LOAD_CONST                   'processes'
          44 BUILD_LIST                   
          46 BUILD_MAP                    
          48 BUILD_LIST                   
          50 RETURN_VALUE                 
          52 LOAD_FAST_BORROW             self
          54 LOAD_ATTR                    find_java_processes + NULL|self
          74 CALL                         
          82 STORE_FAST                   processes
          84 BUILD_LIST                   
          86 STORE_FAST                   results
          88 LOAD_FAST_BORROW             processes
          90 GET_ITER                     
          92 FOR_ITER                     to L4
          96 STORE_FAST                   proc
          98 LOAD_FAST_BORROW             self
         100 LOAD_ATTR                    verbose
         120 TO_BOOL                      
         128 POP_JUMP_IF_FALSE            to L3
         132 NOT_TAKEN                    
         134 LOAD_GLOBAL                  print + NULL
         144 LOAD_CONST                   'Taran²yor: PID '
         146 LOAD_FAST_BORROW             proc
         148 LOAD_CONST                   'pid'
         150 BINARY_OP                    []
         162 FORMAT_SIMPLE                
         164 LOAD_CONST                   ' - '
         166 LOAD_FAST_BORROW             proc
         168 LOAD_CONST                   'name'
         170 BINARY_OP                    []
         182 FORMAT_SIMPLE                
         184 BUILD_STRING                 
         186 CALL                         
         194 POP_TOP                      
         196 LOAD_FAST_BORROW             self
         198 LOAD_ATTR                    scan_process_memory + NULL|self
         218 LOAD_FAST_BORROW             proc
         220 LOAD_CONST                   'pid'
         222 BINARY_OP                    []
         234 CALL                         
         242 STORE_FAST                   scan_result
         244 LOAD_FAST_BORROW             proc
         246 LOAD_CONST                   'name'
         248 BINARY_OP                    []
         260 LOAD_FAST_BORROW             scan_result
         262 LOAD_CONST                   'name'
         264 STORE_SUBSCR                 
         268 LOAD_FAST_BORROW             results
         270 LOAD_ATTR                    append + NULL|self
         290 LOAD_FAST_BORROW             scan_result
         292 CALL                         
         300 POP_TOP                      
         302 JUMP_BACKWARD                to L2
         306 END_FOR                      
         308 POP_ITER                     
         310 LOAD_FAST_BORROW             results
         312 RETURN_VALUE                 
