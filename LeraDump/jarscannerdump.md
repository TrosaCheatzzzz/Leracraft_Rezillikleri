### CODE OBJECT: <module>  (file=scanner\jar_scanner.py, line=1)
# consts:
  STR: '\nJAR dosyalar²n² analiz eden ana mod³l\nGhost client tespiti iin ÷zel dosyalar² arar\n'
  STR: 'GhostClientSignature'
  STR: 'JarScanner'
# names: ('__doc__', 'zipfile', 'os', 'pathlib', 'Path', 'typing', 'List', 'Dict', 'Tuple', 'GhostClientSignature', 'JarScanner')
# varnames: ()
# bytecode:
       0 RESUME                       
       2 LOAD_CONST                   '\nJAR dosyalar²n² analiz eden ana mod³l\nGhost client tespiti iin ÷zel dosyalar² arar\n'
       4 STORE_NAME                   __doc__
       6 LOAD_SMALL_INT               
       8 LOAD_CONST                   None
      10 IMPORT_NAME                  zipfile
      12 STORE_NAME                   zipfile
      14 LOAD_SMALL_INT               
      16 LOAD_CONST                   None
      18 IMPORT_NAME                  os
      20 STORE_NAME                   os
      22 LOAD_SMALL_INT               
      24 LOAD_CONST                   ('Path',)
      26 IMPORT_NAME                  pathlib
      28 IMPORT_FROM                  Path
      30 STORE_NAME                   Path
      32 POP_TOP                      
      34 LOAD_SMALL_INT               
      36 LOAD_CONST                   ('List', 'Dict', 'Tuple')
      38 IMPORT_NAME                  typing
      40 IMPORT_FROM                  List
      42 STORE_NAME                   List
      44 IMPORT_FROM                  Dict
      46 STORE_NAME                   Dict
      48 IMPORT_FROM                  Tuple
      50 STORE_NAME                   Tuple
      52 POP_TOP                      
      54 LOAD_BUILD_CLASS             
      56 PUSH_NULL                    
      58 LOAD_CONST                   <code object GhostClientSignature at 0x000001D2BDE31E70, file "scanner\jar_scanner.py", line 12>
      60 MAKE_FUNCTION                
      62 LOAD_CONST                   'GhostClientSignature'
      64 CALL                         
      72 STORE_NAME                   GhostClientSignature
      74 LOAD_BUILD_CLASS             
      76 PUSH_NULL                    
      78 LOAD_CONST                   <code object JarScanner at 0x000001D2BE0D8FF0, file "scanner\jar_scanner.py", line 58>
      80 MAKE_FUNCTION                
      82 LOAD_CONST                   'JarScanner'
      84 CALL                         
      92 STORE_NAME                   JarScanner
      94 LOAD_CONST                   None
      96 RETURN_VALUE                 

  ### CODE OBJECT: GhostClientSignature  (file=scanner\jar_scanner.py, line=12)
  # consts:
    STR: 'GhostClientSignature'
    STR: 'Ghost client imzas² - aranan dosyalar'
    STR: '0'
    STR: 'Doomsday Client'
    STR: '1'
    STR: 'l.png'
  # names: ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', 'SUSPICIOUS_FILES', 'staticmethod', 'check_any_match', 'check_file_match', 'check_path_match', '__static_attributes__', '__classdictcell__')
  # varnames: ()
  # bytecode:
         0 MAKE_CELL                    __classdict__
         2 RESUME                       
         4 LOAD_NAME                    __name__
         6 STORE_NAME                   __module__
         8 LOAD_CONST                   'GhostClientSignature'
        10 STORE_NAME                   __qualname__
        12 LOAD_SMALL_INT               
        14 STORE_NAME                   __firstlineno__
        16 LOAD_LOCALS                  
        18 STORE_DEREF                  __classdict__
        20 LOAD_CONST                   'Ghost client imzas² - aranan dosyalar'
        22 STORE_NAME                   __doc__
        24 LOAD_CONST                   '0'
        26 LOAD_CONST                   'Doomsday Client'
        28 LOAD_CONST                   '1'
        30 LOAD_CONST                   'Doomsday Client'
        32 LOAD_CONST                   'l.png'
        34 LOAD_CONST                   'Doomsday Client'
        36 BUILD_MAP                    
        38 STORE_NAME                   SUSPICIOUS_FILES
        40 LOAD_NAME                    staticmethod
        42 LOAD_FAST_BORROW             __classdict__
        44 BUILD_TUPLE                  
        46 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE0AAD30, file "scanner\jar_scanner.py", line 22>
        48 MAKE_FUNCTION                
        50 SET_FUNCTION_ATTRIBUTE       closure
        52 LOAD_CONST                   <code object check_any_match at 0x000001D2BDE5E330, file "scanner\jar_scanner.py", line 21>
        54 MAKE_FUNCTION                
        56 SET_FUNCTION_ATTRIBUTE       annotate
        58 CALL                         
        66 STORE_NAME                   check_any_match
        68 LOAD_NAME                    staticmethod
        70 LOAD_FAST_BORROW             __classdict__
        72 BUILD_TUPLE                  
        74 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE0AB130, file "scanner\jar_scanner.py", line 38>
        76 MAKE_FUNCTION                
        78 SET_FUNCTION_ATTRIBUTE       closure
        80 LOAD_CONST                   <code object check_file_match at 0x000001D2BE0AA530, file "scanner\jar_scanner.py", line 37>
        82 MAKE_FUNCTION                
        84 SET_FUNCTION_ATTRIBUTE       annotate
        86 CALL                         
        94 STORE_NAME                   check_file_match
        96 LOAD_NAME                    staticmethod
        98 LOAD_FAST_BORROW             __classdict__
       100 BUILD_TUPLE                  
       102 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE123DD0, file "scanner\jar_scanner.py", line 43>
       104 MAKE_FUNCTION                
       106 SET_FUNCTION_ATTRIBUTE       closure
       108 LOAD_CONST                   <code object check_path_match at 0x000001D2BDEB2CC0, file "scanner\jar_scanner.py", line 42>
       110 MAKE_FUNCTION                
       112 SET_FUNCTION_ATTRIBUTE       annotate
       114 CALL                         
       122 STORE_NAME                   check_path_match
       124 LOAD_CONST                   ()
       126 STORE_NAME                   __static_attributes__
       128 LOAD_FAST_BORROW             __classdict__
       130 STORE_NAME                   __classdictcell__
       132 LOAD_CONST                   None
       134 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\jar_scanner.py, line=22)
    # consts:
      STR: 'filename'
      STR: 'return'
    # names: ('str', 'bool')
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
          22 LOAD_CONST                   'filename'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    str
          28 LOAD_CONST                   'return'
          30 LOAD_DEREF                   __classdict__
          32 LOAD_FROM_DICT_OR_GLOBALS    bool
          34 BUILD_MAP                    
          36 RETURN_VALUE                 

    ### CODE OBJECT: check_any_match  (file=scanner\jar_scanner.py, line=21)
    # consts:
      STR: '\nDosya ad²n²n herhangi bir e■le■me kontrol³\nHer yerdeki dosyalar² bulur (dizin farketmez)\n'
    # names: ('lower', 'os', 'path', 'basename', 'GhostClientSignature', 'SUSPICIOUS_FILES', 'keys')
    # varnames: ('filename', 'filename_lower', 'basename', 'suspicious_file')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW             filename
           4 LOAD_ATTR                    lower + NULL|self
          24 CALL                         
          32 STORE_FAST                   filename_lower
          34 LOAD_GLOBAL                  os
          44 LOAD_ATTR                    path
          64 LOAD_ATTR                    basename + NULL|self
          84 LOAD_FAST_BORROW             filename_lower
          86 CALL                         
          94 STORE_FAST                   basename
          96 LOAD_GLOBAL                  GhostClientSignature
         106 LOAD_ATTR                    SUSPICIOUS_FILES
         126 LOAD_ATTR                    keys + NULL|self
         146 CALL                         
         154 GET_ITER                     
         156 FOR_ITER                     to L3
         160 STORE_FAST                   suspicious_file
         162 LOAD_FAST_BORROW_LOAD_FAST_BORROW basename, suspicious_file
         164 LOAD_ATTR                    lower + NULL|self
         184 CALL                         
         192 COMPARE_OP                   bool(==)
         196 POP_JUMP_IF_TRUE             to L2
         200 NOT_TAKEN                    
         202 JUMP_BACKWARD                to L1
         206 LOAD_CONST                   True
         208 LOAD_FAST_BORROW             suspicious_file
         210 BUILD_TUPLE                  
         212 SWAP                         
         214 POP_TOP                      
         216 RETURN_VALUE                 
         218 END_FOR                      
         220 POP_ITER                     
         222 LOAD_CONST                   (False, None)
         224 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\jar_scanner.py, line=38)
    # consts:
      STR: 'filename'
      STR: 'return'
    # names: ('str', 'bool')
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
          22 LOAD_CONST                   'filename'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    str
          28 LOAD_CONST                   'return'
          30 LOAD_DEREF                   __classdict__
          32 LOAD_FROM_DICT_OR_GLOBALS    bool
          34 BUILD_MAP                    
          36 RETURN_VALUE                 

    ### CODE OBJECT: check_file_match  (file=scanner\jar_scanner.py, line=37)
    # consts:
      STR: 'Dosya ad²n²n tam e■le■me kontrol³'
    # names: ('GhostClientSignature', 'SUSPICIOUS_FILES')
    # varnames: ('filename',)
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW             filename
           4 LOAD_GLOBAL                  GhostClientSignature
          14 LOAD_ATTR                    SUSPICIOUS_FILES
          34 CONTAINS_OP                  in
          38 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\jar_scanner.py, line=43)
    # consts:
      STR: 'filepath'
      STR: 'return'
    # names: ('str', 'Tuple', 'bool')
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
          22 LOAD_CONST                   'filepath'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    str
          28 LOAD_CONST                   'return'
          30 LOAD_DEREF                   __classdict__
          32 LOAD_FROM_DICT_OR_GLOBALS    Tuple
          34 LOAD_DEREF                   __classdict__
          36 LOAD_FROM_DICT_OR_GLOBALS    bool
          38 LOAD_DEREF                   __classdict__
          40 LOAD_FROM_DICT_OR_GLOBALS    str
          42 BUILD_TUPLE                  
          44 BINARY_OP                    []
          56 BUILD_MAP                    
          58 RETURN_VALUE                 

    ### CODE OBJECT: check_path_match  (file=scanner\jar_scanner.py, line=42)
    # consts:
      STR: '\nTam dosya yolu kontrol³ - dizin iinde de arar\nReturns: (e■le■me_var_m², e■le■en_dosya_ad²)\n'
      STR: '\\'
      STR: '/'
    # names: ('replace', 'split', 'GhostClientSignature', 'SUSPICIOUS_FILES')
    # varnames: ('filepath', 'parts', 'part')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW             filepath
           4 LOAD_ATTR                    replace + NULL|self
          24 LOAD_CONST                   '\\'
          26 LOAD_CONST                   '/'
          28 CALL                         
          36 STORE_FAST                   filepath
          38 LOAD_FAST_BORROW             filepath
          40 LOAD_ATTR                    split + NULL|self
          60 LOAD_CONST                   '/'
          62 CALL                         
          70 STORE_FAST                   parts
          72 LOAD_FAST_BORROW             parts
          74 GET_ITER                     
          76 FOR_ITER                     to L3
          80 STORE_FAST                   part
          82 LOAD_FAST_BORROW             part
          84 LOAD_GLOBAL                  GhostClientSignature
          94 LOAD_ATTR                    SUSPICIOUS_FILES
         114 CONTAINS_OP                  in
         118 POP_JUMP_IF_TRUE             to L2
         122 NOT_TAKEN                    
         124 JUMP_BACKWARD                to L1
         128 LOAD_CONST                   True
         130 LOAD_FAST_BORROW             part
         132 BUILD_TUPLE                  
         134 SWAP                         
         136 POP_TOP                      
         138 RETURN_VALUE                 
         140 END_FOR                      
         142 POP_ITER                     
         144 LOAD_CONST                   (False, '')
         146 RETURN_VALUE                 

  ### CODE OBJECT: JarScanner  (file=scanner\jar_scanner.py, line=58)
  # consts:
    STR: 'JarScanner'
    STR: 'JAR dosyalar²n² analiz eden s²n²f'
  # names: ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', '__init__', 'scan_jar', 'scan_directory', 'get_stats', '__static_attributes__', '__classdictcell__')
  # varnames: ()
  # bytecode:
         0 MAKE_CELL                    __classdict__
         2 RESUME                       
         4 LOAD_NAME                    __name__
         6 STORE_NAME                   __module__
         8 LOAD_CONST                   'JarScanner'
        10 STORE_NAME                   __qualname__
        12 LOAD_SMALL_INT               
        14 STORE_NAME                   __firstlineno__
        16 LOAD_LOCALS                  
        18 STORE_DEREF                  __classdict__
        20 LOAD_CONST                   'JAR dosyalar²n² analiz eden s²n²f'
        22 STORE_NAME                   __doc__
        24 LOAD_CONST                   (False,)
        26 LOAD_FAST_BORROW             __classdict__
        28 BUILD_TUPLE                  
        30 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE0B14D0, file "scanner\jar_scanner.py", line 61>
        32 MAKE_FUNCTION                
        34 SET_FUNCTION_ATTRIBUTE       closure
        36 LOAD_CONST                   <code object __init__ at 0x000001D2BE0AB330, file "scanner\jar_scanner.py", line 61>
        38 MAKE_FUNCTION                
        40 SET_FUNCTION_ATTRIBUTE       annotate
        42 SET_FUNCTION_ATTRIBUTE       defaults
        44 STORE_NAME                   __init__
        46 LOAD_FAST_BORROW             __classdict__
        48 BUILD_TUPLE                  
        50 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE129230, file "scanner\jar_scanner.py", line 66>
        52 MAKE_FUNCTION                
        54 SET_FUNCTION_ATTRIBUTE       closure
        56 LOAD_CONST                   <code object scan_jar at 0x000001D2BE225530, file "scanner\jar_scanner.py", line 66>
        58 MAKE_FUNCTION                
        60 SET_FUNCTION_ATTRIBUTE       annotate
        62 STORE_NAME                   scan_jar
        64 LOAD_CONST                   (True,)
        66 LOAD_FAST_BORROW             __classdict__
        68 BUILD_TUPLE                  
        70 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE474030, file "scanner\jar_scanner.py", line 126>
        72 MAKE_FUNCTION                
        74 SET_FUNCTION_ATTRIBUTE       closure
        76 LOAD_CONST                   <code object scan_directory at 0x000001D2BE22F950, file "scanner\jar_scanner.py", line 126>
        78 MAKE_FUNCTION                
        80 SET_FUNCTION_ATTRIBUTE       annotate
        82 SET_FUNCTION_ATTRIBUTE       defaults
        84 STORE_NAME                   scan_directory
        86 LOAD_FAST_BORROW             __classdict__
        88 BUILD_TUPLE                  
        90 LOAD_CONST                   <code object __annotate__ at 0x000001D2BE0B12F0, file "scanner\jar_scanner.py", line 172>
        92 MAKE_FUNCTION                
        94 SET_FUNCTION_ATTRIBUTE       closure
        96 LOAD_CONST                   <code object get_stats at 0x000001D2BE0C9070, file "scanner\jar_scanner.py", line 172>
        98 MAKE_FUNCTION                
       100 SET_FUNCTION_ATTRIBUTE       annotate
       102 STORE_NAME                   get_stats
       104 LOAD_CONST                   ('detected_count', 'scanned_count', 'verbose')
       106 STORE_NAME                   __static_attributes__
       108 LOAD_FAST_BORROW             __classdict__
       110 STORE_NAME                   __classdictcell__
       112 LOAD_CONST                   None
       114 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\jar_scanner.py, line=61)
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

    ### CODE OBJECT: __init__  (file=scanner\jar_scanner.py, line=61)
    # consts:
    # names: ('verbose', 'scanned_count', 'detected_count')
    # varnames: ('self', 'verbose')
    # bytecode:
           0 RESUME                       
           2 LOAD_FAST_BORROW_LOAD_FAST_BORROW verbose, self
           4 STORE_ATTR                   verbose
          14 LOAD_SMALL_INT               
          16 LOAD_FAST_BORROW             self
          18 STORE_ATTR                   scanned_count
          28 LOAD_SMALL_INT               
          30 LOAD_FAST_BORROW             self
          32 STORE_ATTR                   detected_count
          42 LOAD_CONST                   None
          44 RETURN_VALUE                 

    ### CODE OBJECT: __annotate__  (file=scanner\jar_scanner.py, line=66)
    # consts:
      STR: 'jar_path'
      STR: 'return'
    # names: ('str', 'Dict')
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
          22 LOAD_CONST                   'jar_path'
          24 LOAD_DEREF                   __classdict__
          26 LOAD_FROM_DICT_OR_GLOBALS    str
          28 LOAD_CONST                   'return'
          30 LOAD_DEREF                   __classdict__
          32 LOAD_FROM_DICT_OR_GLOBALS    Dict
          34 BUILD_MAP                    
          36 RETURN_VALUE                 

    ### CODE OBJECT: scan_jar  (file=scanner\jar_scanner.py, line=66)
    # consts:
      STR: '\nBir JAR dosyas²n² tarar - DEEP SCAN\n\nArgs:\n    jar_path: JAR dosyas²n²n yolu\n    \nReturns:\n    Tarama sonucu dictionary\n'
      STR: 'path'
      STR: 'filename'
      STR: 'is_suspicious'
      STR: 'found_files'
      STR: 'all_files_scanned'
      STR: 'error'
      STR: 'Geerli bir JAR/ZIP dosyas² de­il'
      STR: 'r'
