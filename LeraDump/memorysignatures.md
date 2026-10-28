=== MemoryScanner class body bytecode (SIGNATURES burada) ===
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
    20 LOAD_CONST                   "Java process'lerini tarayıp memory'de ghost client imzalarını arar"
    22 STORE_NAME                   __doc__
    24 BUILD_LIST                   
    26 LOAD_CONST                   (b'Doomsday', b'doomsday', b'DOOMSDAY')
    28 LIST_EXTEND                  
    30 STORE_NAME                   SIGNATURES
    32 LOAD_CONST                   (False,)
    34 LOAD_FAST_BORROW             __classdict__
    36 BUILD_TUPLE                  
    38 LOAD_CONST                   <code object __annotate__ at 0x0000016FAD610D50, file "scanner\memory_scanner.py", line 31>
    40 MAKE_FUNCTION                
    42 SET_FUNCTION_ATTRIBUTE       closure
    44 LOAD_CONST                   <code object __init__ at 0x0000016FAD638AB0, file "scanner\memory_scanner.py", line 31>
    46 MAKE_FUNCTION                
    48 SET_FUNCTION_ATTRIBUTE       annotate
    50 SET_FUNCTION_ATTRIBUTE       defaults
    52 STORE_NAME                   __init__
    54 LOAD_FAST_BORROW             __classdict__
    56 BUILD_TUPLE                  
    58 LOAD_CONST                   <code object __annotate__ at 0x0000016FAD6114D0, file "scanner\memory_scanner.py", line 36>
    60 MAKE_FUNCTION                
    62 SET_FUNCTION_ATTRIBUTE       closure
    64 LOAD_CONST                   <code object _check_admin at 0x0000016FAD6291B0, file "scanner\memory_scanner.py", line 36>
    66 MAKE_FUNCTION                
    68 SET_FUNCTION_ATTRIBUTE       annotate
    70 STORE_NAME                   _check_admin
    72 LOAD_FAST_BORROW             __classdict__
    74 BUILD_TUPLE                  
    76 LOAD_CONST                   <code object __annotate__ at 0x0000016FAD608030, file "scanner\memory_scanner.py", line 43>
    78 MAKE_FUNCTION                
    80 SET_FUNCTION_ATTRIBUTE       closure
    82 LOAD_CONST                   <code object find_java_processes at 0x0000016FAD73A320, file "scanner\memory_scanner.py", line 43>
    84 MAKE_FUNCTION                
    86 SET_FUNCTION_ATTRIBUTE       annotate
    88 STORE_NAME                   find_java_processes
    90 LOAD_FAST_BORROW             __classdict__
    92 BUILD_TUPLE                  
    94 LOAD_CONST                   <code object __annotate__ at 0x0000016FAD60B030, file "scanner\memory_scanner.py", line 65>
    96 MAKE_FUNCTION                
    98 SET_FUNCTION_ATTRIBUTE       closure
   100 LOAD_CONST                   <code object scan_process_memory at 0x0000016FAD767FA0, file "scanner\memory_scanner.py", line 65>
   102 MAKE_FUNCTION                
   104 SET_FUNCTION_ATTRIBUTE       annotate
   106 STORE_NAME                   scan_process_memory
   108 LOAD_FAST_BORROW             __classdict__
   110 BUILD_TUPLE                  
   112 LOAD_CONST                   <code object __annotate__ at 0x0000016FAD60AF30, file "scanner\memory_scanner.py", line 147>
   114 MAKE_FUNCTION                
   116 SET_FUNCTION_ATTRIBUTE       closure
   118 LOAD_CONST                   <code object scan_all at 0x0000016FAD735810, file "scanner\memory_scanner.py", line 147>
   120 MAKE_FUNCTION                
   122 SET_FUNCTION_ATTRIBUTE       annotate
   124 STORE_NAME                   scan_all
   126 LOAD_CONST                   ('is_admin', 'kernel32', 'verbose')
   128 STORE_NAME                   __static_attributes__
   130 LOAD_FAST_BORROW             __classdict__
   132 STORE_NAME                   __classdictcell__
   134 LOAD_CONST                   None
   136 RETURN_VALUE                 

=== scan_process_memory: str consts ===
  "Bir process'in memory'sini tara"
  'pid'
  'scanned'
  'detections'
  'error'
  'Admin yetkisi gerekli'
  'Process açılamadı'
  'signature'
  'utf-8'
  'ignore'
  'address'

=== scan_process_memory: bytecode ===
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
   178 LOAD_CONST                   'Process açılamadı'
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
