### CODE OBJECT: <module>  (file=scanner\prefetch_scanner.py, line=1)
# consts:
  STR: "\nWindows Prefetch Scanner - Gemi■te al²■t²r²lan JAR'lar² bul\n"
  STR: 'PrefetchScanner'
# names: ('__doc__', 'os', 'glob', 'struct', 'pathlib', 'Path', 'typing', 'List', 'Dict', 'ctypes', 'PrefetchScanner')
# varnames: ()
# bytecode:
       0 RESUME                       
       2 LOAD_CONST                   "\nWindows Prefetch Scanner - Gemi■te al²■t²r²lan JAR'lar² bul\n"
       4 STORE_NAME                   __doc__
       6 LOAD_SMALL_INT               
       8 LOAD_CONST                   None
      10 IMPORT_NAME                  os
      12 STORE_NAME                   os
      14 LOAD_SMALL_INT               
      16 LOAD_CONST                   None
      18 IMPORT_NAME                  glob
      20 STORE_NAME                   glob
      22 LOAD_SMALL_INT               
      24 LOAD_CONST                   None
      26 IMPORT_NAME                  struct
      28 STORE_NAME                   struct
      30 LOAD_SMALL_INT               
      32 LOAD_CONST                   ('Path',)
      34 IMPORT_NAME                  pathlib
      36 IMPORT_FROM                  Path
      38 STORE_NAME                   Path
      40 POP_TOP                      
      42 LOAD_SMALL_INT               
      44 LOAD_CONST                   ('List', 'Dict')
      46 IMPORT_NAME                  typing
      48 IMPORT_FROM                  List
      50 STORE_NAME                   List
      52 IMPORT_FROM                  Dict
      54 STORE_NAME                   Dict
      56 POP_TOP                      
      58 LOAD_SMALL_INT               
      60 LOAD_CONST                   None
      62 IMPORT_NAME                  ctypes
      64 STORE_NAME                   ctypes
      66 LOAD_BUILD_CLASS             
      68 PUSH_NULL                    
      70 LOAD_CONST                   <code object PrefetchScanner at 0x0000025985A72CC0, file "scanner\prefetch_scanner.py", line 13>
      72 MAKE_FUNCTION                
      74 LOAD_CONST                   'PrefetchScanner'
      76 CALL                         
      84 STORE_NAME                   PrefetchScanner
      86 LOAD_CONST                   None
      88 RETURN_VALUE                 

  ### CODE OBJECT: PrefetchScanner  (file=scanner\prefetch_scanner.py, line=13)
  # consts:
    STR: 'PrefetchScanner'
    STR: 'Windows Prefetch dosyalar²n² analiz eder'
    STR: 'C:\\Windows\\Prefetch'
  # names: ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', 'PREFETCH_PATH', '__init__', '_check_admin', 'can_access_prefetch', 'find_jar_references', '_extract_jar_paths', 'analyze_jar_history', '__static_attributes__', '__classdictcell__')
  # varnames: ()
  # bytecode:
         0 MAKE_CELL                    __classdict__
         2 RESUME                       
         4 LOAD_NAME                    __name__
         6 STORE_NAME                   __module__
         8 LOAD_CONST                   'PrefetchScanner'
        10 STORE_NAME                   __qualname__
        12 LOAD_SMALL_INT               
        14 STORE_NAME                   __firstlineno__
        16 LOAD_LOCALS                  
        18 STORE_DEREF                  __classdict__
        20 LOAD_CONST                   'Windows Prefetch dosyalar²n² analiz eder'
        22 STORE_NAME                   __doc__
        24 LOAD_CONST                   'C:\\Windows\\Prefetch'
        26 STORE_NAME                   PREFETCH_PATH
        28 LOAD_CONST                   (False,)
        30 LOAD_FAST_BORROW             __classdict__
        32 BUILD_TUPLE                  
        34 LOAD_CONST                   <code object __annotate__ at 0x0000025985C60D50, file "scanner\prefetch_scanner.py", line 18>
        36 MAKE_FUNCTION                
        38 SET_FUNCTION_ATTRIBUTE       closure
        40 LOAD_CONST                   <code object __init__ at 0x0000025985CD3CC0, file "scanner\prefetch_scanner.py", line 18>
        42 MAKE_FUNCTION                
        44 SET_FUNCTION_ATTRIBUTE       annotate
        46 SET_FUNCTION_ATTRIBUTE       defaults
        48 STORE_NAME                   __init__
        50 LOAD_FAST_BORROW             __classdict__
        52 BUILD_TUPLE                  
        54 LOAD_CONST                   <code object __annotate__ at 0x0000025985C614D0, file "scanner\prefetch_scanner.py", line 22>
        56 MAKE_FUNCTION                
        58 SET_FUNCTION_ATTRIBUTE       closure
        60 LOAD_CONST                   <code object _check_admin at 0x0000025985C791B0, file "scanner\prefetch_scanner.py", line 22>
        62 MAKE_FUNCTION                
        64 SET_FUNCTION_ATTRIBUTE       annotate
        66 STORE_NAME                   _check_admin
        68 LOAD_FAST_BORROW             __classdict__
        70 BUILD_TUPLE                  
        72 LOAD_CONST                   <code object __annotate__ at 0x0000025985C612F0, file "scanner\prefetch_scanner.py", line 29>
        74 MAKE_FUNCTION                
        76 SET_FUNCTION_ATTRIBUTE       closure
        78 LOAD_CONST                   <code object can_access_prefetch at 0x0000025985A7A3A0, file "scanner\prefetch_scanner.py", line 29>
        80 MAKE_FUNCTION                
        82 SET_FUNCTION_ATTRIBUTE       annotate
        84 STORE_NAME                   can_access_prefetch
        86 LOAD_FAST_BORROW             __classdict__
        88 BUILD_TUPLE                  
        90 LOAD_CONST                   <code object __annotate__ at 0x0000025985C5AD30, file "scanner\prefetch_scanner.py", line 36>
        92 MAKE_FUNCTION                
        94 SET_FUNCTION_ATTRIBUTE       closure
        96 LOAD_CONST                   <code object find_jar_references at 0x0000025985D85F10, file "scanner\prefetch_scanner.py", line 36>
        98 MAKE_FUNCTION                
       100 SET_FUNCTION_ATTRIBUTE       annotate
       102 STORE_NAME                   find_jar_references
       104 LOAD_FAST_BORROW             __classdict__
       106 BUILD_TUPLE                  
       108 LOAD_CONST                   <code object __annotate__ at 0x0000025985CD3DD0, file "scanner\prefetch_scanner.py", line 88>
       110 MAKE_FUNCTION                
       112 SET_FUNCTION_ATTRIBUTE       closure
       114 LOAD_CONST                   <code object _extract_jar_paths at 0x0000025985A423D0, file "scanner\prefetch_scanner.py", line 88>
       116 MAKE_FUNCTION                
       118 SET_FUNCTION_ATTRIBUTE       annotate
       120 STORE_NAME                   _extract_jar_paths
       122 LOAD_FAST_BORROW             __classdict__
       124 BUILD_TUPLE                  
       126 LOAD_CONST                   <code object __annotate__ at 0x0000025985C63C30, file "scanner\prefetch_scanner.py", line 103>
       128 MAKE_FUNCTION                
       130 SET_FUNCTION_ATTRIBUTE       closure
       132 LOAD_CONST                   <code object analyze_jar_history at 0x0000025985DE0D50, file "scanner\prefetch_scanner.py", line 103>
       134 MAKE_FUNCTION                
       136 SET_FUNCTION_ATTRIBUTE       annotate
       138 STORE_NAME                   analyze_jar_history
       140 LOAD_CONST                   ('is_admin', 'verbose')
       142 STORE_NAME                   __static_attributes__
       144 LOAD_FAST_BORROW             __classdict__
       146 STORE_NAME                   __classdictcell__
       148 LOAD_CONST                   None
       150 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\prefetch_scanner.py, line=18)
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

    ### CODE OBJECT: __init__  (file=scanner\prefetch_scanner.py, line=18)
    # consts:
    # names: ('verbose', '_check_admin', 'is_admin')
    # varnames: ('self', 'verbose')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW_LOAD_FAST_BORROW verbose, self
           4 STORE_ATTR                   verbose
          14 LOAD_FAST_BORROW             self
          16 LOAD_ATTR                    _check_admin + NULL|self
          36 CALL                         
          44 LOAD_FAST_BORROW             self
          46 STORE_ATTR                   is_admin
          56 LOAD_CONST                   None
          58 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\prefetch_scanner.py, line=22)
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

    ### CODE OBJECT: _check_admin  (file=scanner\prefetch_scanner.py, line=22)
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

    ### CODE OBJECT: __annotate__  (file=scanner\prefetch_scanner.py, line=29)
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

    ### CODE OBJECT: can_access_prefetch  (file=scanner\prefetch_scanner.py, line=29)
    # consts:
      STR: 'Prefetch klas÷r³ne eri■im kontrol³'
    # names: ('os', 'path', 'exists', 'PREFETCH_PATH', 'access', 'R_OK')
    # varnames: ('self',)
    # bytecode:
           0 RESUME                       
           2 NOP                          
           4 LOAD_GLOBAL                  os
          14 LOAD_ATTR                    path
          34 LOAD_ATTR                    exists + NULL|self
          54 LOAD_FAST_BORROW             self
          56 LOAD_ATTR                    PREFETCH_PATH
          76 CALL                         
          84 COPY                         
          86 TO_BOOL                      
          94 POP_JUMP_IF_FALSE            to L1
          98 NOT_TAKEN                    
         100 POP_TOP                      
         102 LOAD_GLOBAL                  os
         112 LOAD_ATTR                    access
         132 PUSH_NULL                    
         134 LOAD_FAST_BORROW             self
         136 LOAD_ATTR                    PREFETCH_PATH
         156 LOAD_GLOBAL                  os
         166 LOAD_ATTR                    R_OK
         186 CALL                         
         194 RETURN_VALUE                 
         196 PUSH_EXC_INFO                
         198 POP_TOP                      
         200 POP_EXCEPT                   
         202 LOAD_CONST                   False
         204 RETURN_VALUE                 
         206 COPY                         
         208 POP_EXCEPT                   
         210 RERAISE                      

    ### CODE OBJECT: __annotate__  (file=scanner\prefetch_scanner.py, line=36)
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

    ### CODE OBJECT: find_jar_references  (file=scanner\prefetch_scanner.py, line=36)
    # consts:
      STR: 'Prefetch dosyalar²nda JAR referanslar²n² bul'
      STR: 'error'
      STR: 'Bu ÷zellik iin admin yetkisi ile al²■t²rman²z gerekiyor!'
      STR: 'Prefetch klas÷r³ne eri■im yok: '
      STR: '*.pf'
