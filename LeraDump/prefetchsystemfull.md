
==============================================================================
### DOSYA: prefetch_scanner.pyc
==============================================================================

### <module>  (line 1)
  [STR]
    "\nWindows Prefetch Scanner - Geçmişte çalıştırılan JAR'ları bul\n"
    'PrefetchScanner'
  [names] ('__doc__', 'os', 'glob', 'struct', 'pathlib', 'Path', 'typing', 'List', 'Dict', 'ctypes', 'PrefetchScanner')
  [bytecode]
        0 RESUME                     
        2 LOAD_CONST                 "\nWindows Prefetch Scanner - Geçmişte çalıştırılan JAR'ları bul\n"
        4 STORE_NAME                 __doc__
        6 LOAD_SMALL_INT             
        8 LOAD_CONST                 None
       10 IMPORT_NAME                os
       12 STORE_NAME                 os
       14 LOAD_SMALL_INT             
       16 LOAD_CONST                 None
       18 IMPORT_NAME                glob
       20 STORE_NAME                 glob
       22 LOAD_SMALL_INT             
       24 LOAD_CONST                 None
       26 IMPORT_NAME                struct
       28 STORE_NAME                 struct
       30 LOAD_SMALL_INT             
       32 LOAD_CONST                 ('Path',)
       34 IMPORT_NAME                pathlib
       36 IMPORT_FROM                Path
       38 STORE_NAME                 Path
       40 POP_TOP                    
       42 LOAD_SMALL_INT             
       44 LOAD_CONST                 ('List', 'Dict')
       46 IMPORT_NAME                typing
       48 IMPORT_FROM                List
       50 STORE_NAME                 List
       52 IMPORT_FROM                Dict
       54 STORE_NAME                 Dict
       56 POP_TOP                    
       58 LOAD_SMALL_INT             
       60 LOAD_CONST                 None
       62 IMPORT_NAME                ctypes
       64 STORE_NAME                 ctypes
       66 LOAD_BUILD_CLASS           
       68 PUSH_NULL                  
       70 LOAD_CONST                 <code object PrefetchScanner at 0x0000029D05AA2CC0, file "scanner\prefetch_scanner.py", line 13>
       72 MAKE_FUNCTION              
       74 LOAD_CONST                 'PrefetchScanner'
       76 CALL                       
       84 STORE_NAME                 PrefetchScanner
       86 LOAD_CONST                 None
       88 RETURN_VALUE               

  ### PrefetchScanner  (line 13)
    [STR]
      'PrefetchScanner'
      'Windows Prefetch dosyalarını analiz eder'
      'C:\\Windows\\Prefetch'
    [names] ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', 'PREFETCH_PATH', '__init__', '_check_admin', 'can_access_prefetch', 'find_jar_references', '_extract_jar_paths', 'analyze_jar_history', '__static_attributes__', '__classdictcell__')
    [bytecode]
          0 MAKE_CELL                  __classdict__
          2 RESUME                     
          4 LOAD_NAME                  __name__
          6 STORE_NAME                 __module__
          8 LOAD_CONST                 'PrefetchScanner'
         10 STORE_NAME                 __qualname__
         12 LOAD_SMALL_INT             
         14 STORE_NAME                 __firstlineno__
         16 LOAD_LOCALS                
         18 STORE_DEREF                __classdict__
         20 LOAD_CONST                 'Windows Prefetch dosyalarını analiz eder'
         22 STORE_NAME                 __doc__
         24 LOAD_CONST                 'C:\\Windows\\Prefetch'
         26 STORE_NAME                 PREFETCH_PATH
         28 LOAD_CONST                 (False,)
         30 LOAD_FAST_BORROW           __classdict__
         32 BUILD_TUPLE                
         34 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CF0D50, file "scanner\prefetch_scanner.py", line 18>
         36 MAKE_FUNCTION              
         38 SET_FUNCTION_ATTRIBUTE     closure
         40 LOAD_CONST                 <code object __init__ at 0x0000029D05CDF220, file "scanner\prefetch_scanner.py", line 18>
         42 MAKE_FUNCTION              
         44 SET_FUNCTION_ATTRIBUTE     annotate
         46 SET_FUNCTION_ATTRIBUTE     defaults
         48 STORE_NAME                 __init__
         50 LOAD_FAST_BORROW           __classdict__
         52 BUILD_TUPLE                
         54 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CF14D0, file "scanner\prefetch_scanner.py", line 22>
         56 MAKE_FUNCTION              
         58 SET_FUNCTION_ATTRIBUTE     closure
         60 LOAD_CONST                 <code object _check_admin at 0x0000029D05D091B0, file "scanner\prefetch_scanner.py", line 22>
         62 MAKE_FUNCTION              
         64 SET_FUNCTION_ATTRIBUTE     annotate
         66 STORE_NAME                 _check_admin
         68 LOAD_FAST_BORROW           __classdict__
         70 BUILD_TUPLE                
         72 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CF13E0, file "scanner\prefetch_scanner.py", line 29>
         74 MAKE_FUNCTION              
         76 SET_FUNCTION_ATTRIBUTE     closure
         78 LOAD_CONST                 <code object can_access_prefetch at 0x0000029D05AAA3A0, file "scanner\prefetch_scanner.py", line 29>
         80 MAKE_FUNCTION              
         82 SET_FUNCTION_ATTRIBUTE     annotate
         84 STORE_NAME                 can_access_prefetch
         86 LOAD_FAST_BORROW           __classdict__
         88 BUILD_TUPLE                
         90 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CEB030, file "scanner\prefetch_scanner.py", line 36>
         92 MAKE_FUNCTION              
         94 SET_FUNCTION_ATTRIBUTE     closure
         96 LOAD_CONST                 <code object find_jar_references at 0x0000029D05DAC2A0, file "scanner\prefetch_scanner.py", line 36>
         98 MAKE_FUNCTION              
        100 SET_FUNCTION_ATTRIBUTE     annotate
        102 STORE_NAME                 find_jar_references
        104 LOAD_FAST_BORROW           __classdict__
        106 BUILD_TUPLE                
        108 LOAD_CONST                 <code object __annotate__ at 0x0000029D05D63660, file "scanner\prefetch_scanner.py", line 88>
        110 MAKE_FUNCTION              
        112 SET_FUNCTION_ATTRIBUTE     closure
        114 LOAD_CONST                 <code object _extract_jar_paths at 0x0000029D05A723D0, file "scanner\prefetch_scanner.py", line 88>
        116 MAKE_FUNCTION              
        118 SET_FUNCTION_ATTRIBUTE     annotate
        120 STORE_NAME                 _extract_jar_paths
        122 LOAD_FAST_BORROW           __classdict__
        124 BUILD_TUPLE                
        126 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CF12F0, file "scanner\prefetch_scanner.py", line 103>
        128 MAKE_FUNCTION              
        130 SET_FUNCTION_ATTRIBUTE     closure
        132 LOAD_CONST                 <code object analyze_jar_history at 0x0000029D05DB0C70, file "scanner\prefetch_scanner.py", line 103>
        134 MAKE_FUNCTION              
        136 SET_FUNCTION_ATTRIBUTE     annotate
        138 STORE_NAME                 analyze_jar_history
        140 LOAD_CONST                 ('is_admin', 'verbose')
        142 STORE_NAME                 __static_attributes__
        144 LOAD_FAST_BORROW           __classdict__
        146 STORE_NAME                 __classdictcell__
        148 LOAD_CONST                 None
        150 RETURN_VALUE               

    ### __annotate__  (line 18)
      [STR]
        'verbose'
      [names] ('bool',)
      [varnames] ('format',)

    ### __init__  (line 18)
      [names] ('verbose', '_check_admin', 'is_admin')
      [varnames] ('self', 'verbose')
      [bytecode]
            0 RESUME                     
            2 LOAD_FAST_BORROW_LOAD_FAST_BORROW verbose, self
            4 STORE_ATTR                 verbose
           14 LOAD_FAST_BORROW           self
           16 LOAD_ATTR                  _check_admin + NULL|self
           36 CALL                       
           44 LOAD_FAST_BORROW           self
           46 STORE_ATTR                 is_admin
           56 LOAD_CONST                 None
           58 RETURN_VALUE               

    ### __annotate__  (line 22)
      [STR]
        'return'
      [names] ('bool',)
      [varnames] ('format',)

    ### _check_admin  (line 22)
      [STR]
        'Admin yetkisi kontrolü'
      [names] ('ctypes', 'windll', 'shell32', 'IsUserAnAdmin')
      [varnames] ('self',)
      [bytecode]
            0 RESUME                     
            2 NOP                        
            4 LOAD_GLOBAL                ctypes
           14 LOAD_ATTR                  windll
           34 LOAD_ATTR                  shell32
           54 LOAD_ATTR                  IsUserAnAdmin + NULL|self
           74 CALL                       
           82 LOAD_SMALL_INT             
           84 COMPARE_OP                 !=
           88 RETURN_VALUE               
           90 PUSH_EXC_INFO              
           92 POP_TOP                    
           94 POP_EXCEPT                 
           96 LOAD_CONST                 False
           98 RETURN_VALUE               
          100 COPY                       
          102 POP_EXCEPT                 
          104 RERAISE                    

    ### __annotate__  (line 29)
      [STR]
        'return'
      [names] ('bool',)
      [varnames] ('format',)

    ### can_access_prefetch  (line 29)
      [STR]
        'Prefetch klasörüne erişim kontrolü'
      [names] ('os', 'path', 'exists', 'PREFETCH_PATH', 'access', 'R_OK')
      [varnames] ('self',)
      [bytecode]
            0 RESUME                     
            2 NOP                        
            4 LOAD_GLOBAL                os
           14 LOAD_ATTR                  path
           34 LOAD_ATTR                  exists + NULL|self
           54 LOAD_FAST_BORROW           self
           56 LOAD_ATTR                  PREFETCH_PATH
           76 CALL                       
           84 COPY                       
           86 TO_BOOL                    
           94 POP_JUMP_IF_FALSE          to L1
           98 NOT_TAKEN                  
          100 POP_TOP                    
          102 LOAD_GLOBAL                os
          112 LOAD_ATTR                  access
          132 PUSH_NULL                  
          134 LOAD_FAST_BORROW           self
          136 LOAD_ATTR                  PREFETCH_PATH
          156 LOAD_GLOBAL                os
          166 LOAD_ATTR                  R_OK
          186 CALL                       
          194 RETURN_VALUE               
          196 PUSH_EXC_INFO              
          198 POP_TOP                    
          200 POP_EXCEPT                 
          202 LOAD_CONST                 False
          204 RETURN_VALUE               
          206 COPY                       
          208 POP_EXCEPT                 
          210 RERAISE                    

    ### __annotate__  (line 36)
      [STR]
        'return'
      [names] ('List', 'Dict')
      [varnames] ('format',)

    ### find_jar_references  (line 36)
      [STR]
        'Prefetch dosyalarında JAR referanslarını bul'
        'error'
        'Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!'
        'Prefetch klasörüne erişim yok: '
        '*.pf'
        '  → '
        ' Prefetch dosyası bulundu'
        'rb'
        'utf-16-le'
        'ignore'
        '.jar'
        'JAVA'
        'prefetch_file'
        'found_jars'
        'modified_time'
        '  ⚠ '
        ': '
        'Prefetch taraması başarısız: '
      [names] ('is_admin', 'can_access_prefetch', 'PREFETCH_PATH', 'glob', 'os', 'path', 'join', 'verbose', 'print', 'len', 'open', 'read', 'decode', 'lower', 'basename', 'upper', 'append', '_extract_jar_paths', 'getmtime', 'Exception')
      [varnames] ('self', 'jar_references', 'pf_files', 'pf_file', 'f', 'data', 'data_str', 'pf_name', 'e')
      [bytecode]
            0 RESUME                     
            2 LOAD_FAST_BORROW           self
            4 LOAD_ATTR                  is_admin
           24 TO_BOOL                    
           32 POP_JUMP_IF_TRUE           to L1
           36 NOT_TAKEN                  
           38 LOAD_CONST                 'error'
           40 LOAD_CONST                 'Bu özellik için admin yetkisi ile çalıştırmanız gerekiyor!'
           42 BUILD_MAP                  
           44 BUILD_LIST                 
           46 RETURN_VALUE               
           48 LOAD_FAST_BORROW           self
           50 LOAD_ATTR                  can_access_prefetch + NULL|self
           70 CALL                       
           78 TO_BOOL                    
           86 POP_JUMP_IF_TRUE           to L2
           90 NOT_TAKEN                  
           92 LOAD_CONST                 'error'
           94 LOAD_CONST                 'Prefetch klasörüne erişim yok: '
           96 LOAD_FAST_BORROW           self
           98 LOAD_ATTR                  PREFETCH_PATH
          118 FORMAT_SIMPLE              
          120 BUILD_STRING               
          122 BUILD_MAP                  
          124 BUILD_LIST                 
          126 RETURN_VALUE               
          128 BUILD_LIST                 
          130 STORE_FAST                 jar_references
          132 NOP                        
          134 LOAD_GLOBAL                glob
          144 LOAD_ATTR                  glob
          164 PUSH_NULL                  
          166 LOAD_GLOBAL                os
          176 LOAD_ATTR                  path
          196 LOAD_ATTR                  join + NULL|self
          216 LOAD_FAST_BORROW           self
          218 LOAD_ATTR                  PREFETCH_PATH
          238 LOAD_CONST                 '*.pf'
          240 CALL                       
          248 CALL                       
          256 STORE_FAST                 pf_files
          258 LOAD_FAST_BORROW           self
          260 LOAD_ATTR                  verbose
          280 TO_BOOL                    
          288 POP_JUMP_IF_FALSE          to L3
          292 NOT_TAKEN                  
          294 LOAD_GLOBAL                print + NULL
          304 LOAD_CONST                 '  → '
          306 LOAD_GLOBAL                len + NULL
          316 LOAD_FAST_BORROW           pf_files
          318 CALL                       
          326 FORMAT_SIMPLE              
          328 LOAD_CONST                 ' Prefetch dosyası bulundu'
          330 BUILD_STRING               
          332 CALL                       
          340 POP_TOP                    
          342 LOAD_FAST_BORROW           pf_files
          344 GET_ITER                   
          346 FOR_ITER                   to L8
          350 STORE_FAST                 pf_file
          352 NOP                        
          354 LOAD_GLOBAL                open + NULL
          364 LOAD_FAST_BORROW           pf_file
          366 LOAD_CONST                 'rb'
          368 CALL                       
          376 COPY                       
          378 LOAD_SPECIAL               __exit__
          380 SWAP                       
          382 SWAP                       
          384 LOAD_SPECIAL               __enter__
          386 CALL                       
          394 STORE_FAST                 f
          396 LOAD_FAST_BORROW           f
          398 LOAD_ATTR                  read + NULL|self
          418 CALL                       
          426 STORE_FAST                 data
          428 LOAD_CONST                 None
          430 LOAD_CONST                 None
          432 LOAD_CONST                 None
          434 CALL                       
          442 POP_TOP                    
          444 LOAD_FAST_CHECK            data
          446 LOAD_ATTR                  decode + NULL|self
          466 LOAD_CONST                 'utf-16-le'
          468 LOAD_CONST                 'ignore'
          470 LOAD_CONST                 ('errors',)
          472 CALL_KW                    
          480 STORE_FAST                 data_str
          482 LOAD_CONST                 '.jar'
          484 LOAD_FAST_BORROW           data_str
          486 LOAD_ATTR                  lower + NULL|self
          506 CALL                       
          514 CONTAINS_OP                in
          518 POP_JUMP_IF_FALSE          to L7
          522 NOT_TAKEN                  
          524 LOAD_GLOBAL                os
          534 LOAD_ATTR                  path
          554 LOAD_ATTR                  basename + NULL|self
          574 LOAD_FAST_BORROW           pf_file
          576 CALL                       
          584 STORE_FAST                 pf_name
          586 LOAD_CONST                 'JAVA'
          588 LOAD_FAST_BORROW           pf_name
          590 LOAD_ATTR                  upper + NULL|self
          610 CALL                       
          618 CONTAINS_OP                in
          622 POP_JUMP_IF_FALSE          to L6
          626 NOT_TAKEN                  
          628 LOAD_FAST_BORROW           jar_references
          630 LOAD_ATTR                  append + NULL|self
          650 LOAD_CONST                 'prefetch_file'
          652 LOAD_FAST_BORROW           pf_name
          654 LOAD_CONST                 'found_jars'
          656 LOAD_FAST_BORROW           self
          658 LOAD_ATTR                  _extract_jar_paths + NULL|self
          678 LOAD_FAST_BORROW           data_str
          680 CALL                       
          688 LOAD_CONST                 'modified_time'
          690 LOAD_GLOBAL                os
          700 LOAD_ATTR                  path
          720 LOAD_ATTR                  getmtime + NULL|self
          740 LOAD_FAST_BORROW           pf_file
          742 CALL                       
          750 BUILD_MAP                  
          752 CALL                       
          760 POP_TOP                    
          762 JUMP_BACKWARD              to L4
          766 JUMP_BACKWARD              to L4
          770 JUMP_BACKWARD              to L4
          774 END_FOR                    
          776 POP_ITER                   
          778 LOAD_FAST_BORROW           jar_references
          780 RETURN_VALUE               
          782 PUSH_EXC_INFO              
          784 WITH_EXCEPT_START          
          786 TO_BOOL                    
          794 POP_JUMP_IF_TRUE           to L9
          798 NOT_TAKEN                  
          800 RERAISE                    
          802 POP_TOP                    
          804 POP_EXCEPT                 
          806 POP_TOP                    
          808 POP_TOP                    
          810 POP_TOP                    
          812 JUMP_BACKWARD_NO_INTERRUPT to L5
          814 COPY                       
          816 POP_EXCEPT                 
          818 RERAISE                    
          820 PUSH_EXC_INFO              
          822 LOAD_GLOBAL                Exception
          832 CHECK_EXC_MATCH            
          834 POP_JUMP_IF_FALSE          to L11
          838 NOT_TAKEN                  
          840 STORE_FAST                 e
          842 LOAD_FAST                  self
          844 LOAD_ATTR                  verbose
          864 TO_BOOL                    
          872 POP_JUMP_IF_FALSE          to L10
          876 NOT_TAKEN                  
          878 LOAD_GLOBAL                print + NULL
          888 LOAD_CONST                 '  ⚠ '
          890 LOAD_GLOBAL                os
          900 LOAD_ATTR                  path
          920 LOAD_ATTR                  basename + NULL|self
          940 LOAD_FAST                  pf_file
          942 CALL                       
          950 FORMAT_SIMPLE              
          952 LOAD_CONST                 ': '
          954 LOAD_FAST                  e
          956 FORMAT_SIMPLE              
          958 BUILD_STRING               
          960 CALL                       
          968 POP_TOP                    
          970 POP_EXCEPT                 
          972 LOAD_CONST                 None
          974 STORE_FAST                 e
          976 DELETE_FAST                e
          978 EXTENDED_ARG               
          980 JUMP_BACKWARD              to L4
          984 POP_EXCEPT                 
          986 LOAD_CONST                 None
          988 STORE_FAST                 e
          990 DELETE_FAST                e
          992 EXTENDED_ARG               
          994 JUMP_BACKWARD              to L4
          998 LOAD_CONST                 None
         1000 STORE_FAST                 e
         1002 DELETE_FAST                e
         1004 RERAISE                    
         1006 RERAISE                    
         1008 COPY                       
         1010 POP_EXCEPT                 
         1012 RERAISE                    
         1014 PUSH_EXC_INFO              
         1016 LOAD_GLOBAL                Exception
         1026 CHECK_EXC_MATCH            
         1028 POP_JUMP_IF_FALSE          to L12
         1032 NOT_TAKEN                  
         1034 STORE_FAST                 e
         1036 LOAD_CONST                 'error'
         1038 LOAD_CONST                 'Prefetch taraması başarısız: '
         1040 LOAD_FAST                  e
         1042 FORMAT_SIMPLE              
         1044 BUILD_STRING               
         1046 BUILD_MAP                  
         1048 BUILD_LIST                 
         1050 SWAP                       
         1052 POP_EXCEPT                 
         1054 LOAD_CONST                 None
         1056 STORE_FAST                 e
         1058 DELETE_FAST                e
         1060 RETURN_VALUE               
         1062 LOAD_CONST                 None
         1064 STORE_FAST                 e
         1066 DELETE_FAST                e
         1068 RERAISE                    
         1070 RERAISE                    
         1072 COPY                       
         1074 POP_EXCEPT                 
         1076 RERAISE                    

    ### __annotate__  (line 88)
      [STR]
        'data'
        'return'
      [names] ('str', 'List')
      [varnames] ('format',)

    ### _extract_jar_paths  (line 88)
      [STR]
        "String'den JAR yollarını çıkar"
        '.jar'
        '\x00'
      [names] ('split', 'lower', 'replace', 'strip', 'len', 'append')
      [varnames] ('self', 'data', 'jar_paths', 'words', 'word', 'cleaned')
      [bytecode]
            0 RESUME                     
            2 BUILD_LIST                 
            4 STORE_FAST                 jar_paths
            6 LOAD_FAST_BORROW           data
            8 LOAD_ATTR                  split + NULL|self
           28 CALL                       
           36 STORE_FAST                 words
           38 LOAD_FAST_BORROW           words
           40 GET_ITER                   
           42 FOR_ITER                   to L5
           46 STORE_FAST                 word
           48 LOAD_CONST                 '.jar'
           50 LOAD_FAST_BORROW           word
           52 LOAD_ATTR                  lower + NULL|self
           72 CALL                       
           80 CONTAINS_OP                in
           84 POP_JUMP_IF_TRUE           to L2
           88 NOT_TAKEN                  
           90 JUMP_BACKWARD              to L1
           94 LOAD_FAST_BORROW           word
           96 LOAD_ATTR                  replace + NULL|self
          116 LOAD_CONST                 '\x00'
          118 LOAD_CONST                 ''
          120 CALL                       
          128 LOAD_ATTR                  strip + NULL|self
          148 CALL                       
          156 STORE_FAST                 cleaned
          158 LOAD_GLOBAL                len + NULL
          168 LOAD_FAST_BORROW           cleaned
          170 CALL                       
          178 LOAD_SMALL_INT             
          180 COMPARE_OP                 bool(>)
          184 POP_JUMP_IF_TRUE           to L3
          188 NOT_TAKEN                  
          190 JUMP_BACKWARD              to L1
          194 LOAD_FAST_BORROW_LOAD_FAST_BORROW cleaned, jar_paths
          196 CONTAINS_OP                not in
          200 POP_JUMP_IF_TRUE           to L4
          204 NOT_TAKEN                  
          206 JUMP_BACKWARD              to L1
          210 LOAD_FAST_BORROW           jar_paths
          212 LOAD_ATTR                  append + NULL|self
          232 LOAD_FAST_BORROW           cleaned
          234 CALL                       
          242 POP_TOP                    
          244 JUMP_BACKWARD              to L1
          248 END_FOR                    
          250 POP_ITER                   
          252 LOAD_FAST_BORROW           jar_paths
          254 LOAD_CONST                 slice(None, 10, None)
          256 BINARY_OP                  []
          268 RETURN_VALUE               

    ### __annotate__  (line 103)
      [STR]
        'return'
      [names] ('Dict',)
      [varnames] ('format',)

    ### analyze_jar_history  (line 103)
      [STR]
        'JAR geçmişini analiz et'
        'error'
        'total_java_executions'
        'total_jar_references'
        'suspicious_jars'
        'found_jars'
        'jar_path'
        'keyword'
        'prefetch'
        'prefetch_file'
        'last_execution'
        'modified_time'
      [names] ('find_jar_references', 'get', 'lower', 'append', 'len')
      [varnames] ('self', 'jar_refs', 'suspicious_keywords', 'suspicious_jars', 'total_jar_count', 'ref', 'jar', 'jar_lower', 'keyword')
      [bytecode]
            0 RESUME                     
            2 LOAD_FAST_BORROW           self
            4 LOAD_ATTR                  find_jar_references + NULL|self
           24 CALL                       
           32 STORE_FAST                 jar_refs
           34 LOAD_FAST_BORROW           jar_refs
           36 TO_BOOL                    
           44 POP_JUMP_IF_FALSE          to L1
           48 NOT_TAKEN                  
           50 LOAD_CONST                 'error'
           52 LOAD_FAST_BORROW           jar_refs
           54 LOAD_SMALL_INT             
           56 BINARY_OP                  []
           68 CONTAINS_OP                in
           72 POP_JUMP_IF_FALSE          to L3
           76 NOT_TAKEN                  
           78 LOAD_CONST                 'total_java_executions'
           80 LOAD_SMALL_INT             
           82 LOAD_CONST                 'total_jar_references'
           84 LOAD_SMALL_INT             
           86 LOAD_CONST                 'suspicious_jars'
           88 BUILD_LIST                 
           90 LOAD_CONST                 'error'
           92 LOAD_FAST_BORROW           jar_refs
           94 TO_BOOL                    
          102 POP_JUMP_IF_FALSE          to L2
          106 NOT_TAKEN                  
          108 LOAD_FAST_BORROW           jar_refs
          110 LOAD_SMALL_INT             
          112 BINARY_OP                  []
          124 LOAD_ATTR                  get + NULL|self
          144 LOAD_CONST                 'error'
          146 CALL                       
          154 BUILD_MAP                  
          156 RETURN_VALUE               
          158 LOAD_CONST                 None
          160 BUILD_MAP                  
          162 RETURN_VALUE               
          164 BUILD_LIST                 
          166 LOAD_CONST                 ('doomsday', 'ghost', 'client', 'cheat', 'hack', 'vape', 'liquidbounce', 'wurst', 'meteor')
          168 LIST_EXTEND                
          170 STORE_FAST                 suspicious_keywords
          172 BUILD_LIST                 
          174 STORE_FAST                 suspicious_jars
          176 LOAD_SMALL_INT             
          178 STORE_FAST                 total_jar_count
          180 LOAD_FAST_BORROW           jar_refs
          182 GET_ITER                   
          184 FOR_ITER                   to L10
          188 STORE_FAST                 ref
          190 LOAD_FAST_BORROW           ref
          192 LOAD_ATTR                  get + NULL|self
          212 LOAD_CONST                 'found_jars'
          214 BUILD_LIST                 
          216 CALL                       
          224 GET_ITER                   
          226 FOR_ITER                   to L9
          230 STORE_FAST                 jar
          232 LOAD_FAST_BORROW           total_jar_count
          234 LOAD_SMALL_INT             
          236 BINARY_OP                  +=
          248 STORE_FAST                 total_jar_count
          250 LOAD_FAST_BORROW           jar
          252 LOAD_ATTR                  lower + NULL|self
          272 CALL                       
          280 STORE_FAST                 jar_lower
          282 LOAD_FAST_BORROW           suspicious_keywords
          284 GET_ITER                   
          286 FOR_ITER                   to L8
          290 STORE_FAST                 keyword
          292 LOAD_FAST_BORROW_LOAD_FAST_BORROW keyword, jar_lower
          294 CONTAINS_OP                in
          298 POP_JUMP_IF_TRUE           to L7
          302 NOT_TAKEN                  
          304 JUMP_BACKWARD              to L6
          308 LOAD_FAST_BORROW           suspicious_jars
          310 LOAD_ATTR                  append + NULL|self
          330 LOAD_CONST                 'jar_path'
          332 LOAD_FAST_BORROW           jar
          334 LOAD_CONST                 'keyword'
          336 LOAD_FAST_BORROW           keyword
          338 LOAD_CONST                 'prefetch'
          340 LOAD_FAST_BORROW           ref
          342 LOAD_CONST                 'prefetch_file'
          344 BINARY_OP                  []
          356 LOAD_CONST                 'last_execution'
          358 LOAD_FAST_BORROW           ref
          360 LOAD_CONST                 'modified_time'
          362 BINARY_OP                  []
          374 BUILD_MAP                  
          376 CALL                       
          384 POP_TOP                    
          386 POP_TOP                    
          388 JUMP_BACKWARD              to L5
          392 END_FOR                    
          394 POP_ITER                   
          396 JUMP_BACKWARD              to L5
          400 END_FOR                    
          402 POP_ITER                   
          404 JUMP_BACKWARD              to L4
          408 END_FOR                    
          410 POP_ITER                   
          412 LOAD_CONST                 'total_java_executions'
          414 LOAD_GLOBAL                len + NULL
          424 LOAD_FAST_BORROW           jar_refs
          426 CALL                       
          434 LOAD_CONST                 'total_jar_references'
          436 LOAD_FAST_BORROW           total_jar_count
          438 LOAD_CONST                 'suspicious_jars'
          440 LOAD_FAST_BORROW           suspicious_jars
          442 BUILD_MAP                  
          444 RETURN_VALUE               

==============================================================================
### DOSYA: system_scanner.pyc
==============================================================================

### <module>  (line 1)
  [STR]
    '\nSistem çapında JAR tarama modülü\nTÜM BİLGİSAYARI tarar - her disk, her klasör\n'
    'SystemScanner'
  [names] ('__doc__', 'os', 'pathlib', 'Path', 'typing', 'List', 'string', 'SystemScanner')
  [bytecode]
        0 RESUME                     
        2 LOAD_CONST                 '\nSistem çapında JAR tarama modülü\nTÜM BİLGİSAYARI tarar - her disk, her klasör\n'
        4 STORE_NAME                 __doc__
        6 LOAD_SMALL_INT             
        8 LOAD_CONST                 None
       10 IMPORT_NAME                os
       12 STORE_NAME                 os
       14 LOAD_SMALL_INT             
       16 LOAD_CONST                 ('Path',)
       18 IMPORT_NAME                pathlib
       20 IMPORT_FROM                Path
       22 STORE_NAME                 Path
       24 POP_TOP                    
       26 LOAD_SMALL_INT             
       28 LOAD_CONST                 ('List',)
       30 IMPORT_NAME                typing
       32 IMPORT_FROM                List
       34 STORE_NAME                 List
       36 POP_TOP                    
       38 LOAD_SMALL_INT             
       40 LOAD_CONST                 None
       42 IMPORT_NAME                string
       44 STORE_NAME                 string
       46 LOAD_BUILD_CLASS           
       48 PUSH_NULL                  
       50 LOAD_CONST                 <code object SystemScanner at 0x0000029D05AA3280, file "scanner\system_scanner.py", line 12>
       52 MAKE_FUNCTION              
       54 LOAD_CONST                 'SystemScanner'
       56 CALL                       
       64 STORE_NAME                 SystemScanner
       66 LOAD_CONST                 None
       68 RETURN_VALUE               

  ### SystemScanner  (line 12)
    [STR]
      'SystemScanner'
      'Bilgisayar çapında JAR dosyalarını bulan sınıf'
    [names] ('__name__', '__module__', '__qualname__', '__firstlineno__', '__doc__', 'staticmethod', 'get_all_drives', 'scan_system', 'get_common_locations', 'get_minecraft_instances', '__static_attributes__', '__classdictcell__')
    [bytecode]
          0 MAKE_CELL                  __classdict__
          2 RESUME                     
          4 LOAD_NAME                  __name__
          6 STORE_NAME                 __module__
          8 LOAD_CONST                 'SystemScanner'
         10 STORE_NAME                 __qualname__
         12 LOAD_SMALL_INT             
         14 STORE_NAME                 __firstlineno__
         16 LOAD_LOCALS                
         18 STORE_DEREF                __classdict__
         20 LOAD_CONST                 'Bilgisayar çapında JAR dosyalarını bulan sınıf'
         22 STORE_NAME                 __doc__
         24 LOAD_NAME                  staticmethod
         26 LOAD_FAST_BORROW           __classdict__
         28 BUILD_TUPLE                
         30 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CEAF30, file "scanner\system_scanner.py", line 16>
         32 MAKE_FUNCTION              
         34 SET_FUNCTION_ATTRIBUTE     closure
         36 LOAD_CONST                 <code object get_all_drives at 0x0000029D06094CB0, file "scanner\system_scanner.py", line 15>
         38 MAKE_FUNCTION              
         40 SET_FUNCTION_ATTRIBUTE     annotate
         42 CALL                       
         50 STORE_NAME                 get_all_drives
         52 LOAD_NAME                  staticmethod
         54 LOAD_CONST                 (False,)
         56 LOAD_FAST_BORROW           __classdict__
         58 BUILD_TUPLE                
         60 LOAD_CONST                 <code object __annotate__ at 0x0000029D05D63550, file "scanner\system_scanner.py", line 26>
         62 MAKE_FUNCTION              
         64 SET_FUNCTION_ATTRIBUTE     closure
         66 LOAD_CONST                 <code object scan_system at 0x0000029D05E8E590, file "scanner\system_scanner.py", line 25>
         68 MAKE_FUNCTION              
         70 SET_FUNCTION_ATTRIBUTE     annotate
         72 SET_FUNCTION_ATTRIBUTE     defaults
         74 CALL                       
         82 STORE_NAME                 scan_system
         84 LOAD_NAME                  staticmethod
         86 LOAD_FAST_BORROW           __classdict__
         88 BUILD_TUPLE                
         90 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CEA530, file "scanner\system_scanner.py", line 94>
         92 MAKE_FUNCTION              
         94 SET_FUNCTION_ATTRIBUTE     closure
         96 LOAD_CONST                 <code object get_common_locations at 0x0000029D060982D0, file "scanner\system_scanner.py", line 93>
         98 MAKE_FUNCTION              
        100 SET_FUNCTION_ATTRIBUTE     annotate
        102 CALL                       
        110 STORE_NAME                 get_common_locations
        112 LOAD_NAME                  staticmethod
        114 LOAD_FAST_BORROW           __classdict__
        116 BUILD_TUPLE                
        118 LOAD_CONST                 <code object __annotate__ at 0x0000029D05CEB330, file "scanner\system_scanner.py", line 102>
        120 MAKE_FUNCTION              
        122 SET_FUNCTION_ATTRIBUTE     closure
        124 LOAD_CONST                 <code object get_minecraft_instances at 0x0000029D06098570, file "scanner\system_scanner.py", line 101>
        126 MAKE_FUNCTION              
        128 SET_FUNCTION_ATTRIBUTE     annotate
        130 CALL                       
        138 STORE_NAME                 get_minecraft_instances
        140 LOAD_CONST                 ()
        142 STORE_NAME                 __static_attributes__
        144 LOAD_FAST_BORROW           __classdict__
        146 STORE_NAME                 __classdictcell__
        148 LOAD_CONST                 None
        150 RETURN_VALUE               

    ### __annotate__  (line 16)
      [STR]
        'return'
      [names] ('List', 'str')
      [varnames] ('format',)

    ### get_all_drives  (line 15)
      [STR]
        'Tüm disk sürücülerini bul (C:, D:, E: vb.)'
        ':\\'
      [names] ('string', 'ascii_uppercase', 'os', 'path', 'exists', 'append')
      [varnames] ('drives', 'letter', 'drive')
      [bytecode]
            0 RESUME                     
            2 BUILD_LIST                 
            4 STORE_FAST                 drives
            6 LOAD_GLOBAL                string
           16 LOAD_ATTR                  ascii_uppercase
           36 GET_ITER                   
           38 FOR_ITER                   to L3
           42 STORE_FAST                 letter
           44 LOAD_FAST_BORROW           letter
           46 FORMAT_SIMPLE              
           48 LOAD_CONST                 ':\\'
           50 BUILD_STRING               
           52 STORE_FAST                 drive
           54 LOAD_GLOBAL                os
           64 LOAD_ATTR                  path
           84 LOAD_ATTR                  exists + NULL|self
          104 LOAD_FAST_BORROW           drive
          106 CALL                       
          114 TO_BOOL                    
          122 POP_JUMP_IF_TRUE           to L2
          126 NOT_TAKEN                  
          128 JUMP_BACKWARD              to L1
          132 LOAD_FAST_BORROW           drives
          134 LOAD_ATTR                  append + NULL|self
          154 LOAD_FAST_BORROW           drive
          156 CALL                       
          164 POP_TOP                    
          166 JUMP_BACKWARD              to L1
          170 END_FOR                    
          172 POP_ITER                   
          174 LOAD_FAST_BORROW           drives
          176 RETURN_VALUE               

    ### __annotate__  (line 26)
      [STR]
        'verbose'
        'return'
      [names] ('bool', 'List', 'str')
      [varnames] ('format',)

    ### scan_system  (line 25)
      [STR]
        '\nTÜM BİLGİSAYARI tarar - her disk, her klasör\n\nReturns:\n    JAR dosyalarının yolları\n'
        '  → '
        ' disk bulundu: '
        ', '
        '  → JAR dosyaları aranıyor...'
        '→ ['
        '/'
        '] '
        ' taranıyor...'
        '.jar'
        '• '
        ' JAR bulundu...'
        '    ⚠ Bazı klasörlere erişim reddedildi'
        '    ⚠ Hata: '
        '✓ Arama tamamlandı - '
        ' JAR bulundu'
      [names] ('SystemScanner', 'get_all_drives', 'print', 'len', 'join', 'enumerate', 'colorama', 'Fore', 'Style', 'YELLOW', 'RESET_ALL', 'os', 'walk', 'lower', 'endswith', 'path', 'append', 'GREEN', 'PermissionError', 'Exception')
      [varnames] ('verbose', 'jar_files', 'drives', 'skip_folders', 'total_drives', 'drive_index', 'drive', 'Fore', 'Style', 'root', 'dirs', 'files', 'skip_this', 'skip', 'file', 'full_path', 'e')
      [bytecode]
            0 RESUME                     
            2 BUILD_LIST                 
            4 STORE_FAST                 jar_files
            6 LOAD_GLOBAL                SystemScanner
           16 LOAD_ATTR                  get_all_drives + NULL|self
           36 CALL                       
           44 STORE_FAST                 drives
           46 LOAD_FAST_BORROW           verbose
           48 TO_BOOL                    
           56 POP_JUMP_IF_FALSE          to L1
           60 NOT_TAKEN                  
           62 LOAD_GLOBAL                print + NULL
           72 LOAD_CONST                 '  → '
           74 LOAD_GLOBAL                len + NULL
           84 LOAD_FAST_BORROW           drives
           86 CALL                       
           94 FORMAT_SIMPLE              
           96 LOAD_CONST                 ' disk bulundu: '
           98 LOAD_CONST                 ', '
          100 LOAD_ATTR                  join + NULL|self
          120 LOAD_FAST_BORROW           drives
          122 CALL                       
          130 FORMAT_SIMPLE              
          132 BUILD_STRING               
          134 CALL                       
          142 POP_TOP                    
          144 LOAD_GLOBAL                print + NULL
          154 LOAD_CONST                 '  → JAR dosyaları aranıyor...'
          156 CALL                       
          164 POP_TOP                    
          166 BUILD_SET                  
          168 LOAD_CONST                 frozenset({'AppData\\Local\\Temp', 'AMD', '$Recycle.Bin', 'Program Files', 'Recovery', 'System Volume Information', 'Program Files (x86)', 'Temp', 'NVIDIA', 'tmp', 'Windows', 'Intel', 'ProgramData', 'PerfLogs'})
          170 SET_UPDATE                 
          172 STORE_FAST                 skip_folders
          174 LOAD_GLOBAL                len + NULL
          184 LOAD_FAST_BORROW           drives
          186 CALL                       
          194 STORE_FAST                 total_drives
          196 LOAD_GLOBAL                enumerate + NULL
          206 LOAD_FAST_BORROW           drives
          208 LOAD_SMALL_INT             
          210 CALL                       
          218 GET_ITER                   
          220 EXTENDED_ARG               
          222 FOR_ITER                   to L16
          226 UNPACK_SEQUENCE            
          230 STORE_FAST_STORE_FAST      drive_index, drive
          232 LOAD_FAST_BORROW           verbose
          234 TO_BOOL                    
          242 POP_JUMP_IF_FALSE          to L3
          246 NOT_TAKEN                  
          248 LOAD_SMALL_INT             
          250 LOAD_CONST                 ('Fore', 'Style')
          252 IMPORT_NAME                colorama
          254 IMPORT_FROM                Fore
          256 STORE_FAST                 Fore
          258 IMPORT_FROM                Style
          260 STORE_FAST                 Style
          262 POP_TOP                    
          264 LOAD_GLOBAL                print + NULL
          274 LOAD_CONST                 '\n  '
          276 LOAD_FAST_BORROW           Fore
          278 LOAD_ATTR                  YELLOW
          298 FORMAT_SIMPLE              
          300 LOAD_CONST                 '→ ['
          302 LOAD_FAST_BORROW           drive_index
          304 FORMAT_SIMPLE              
          306 LOAD_CONST                 '/'
          308 LOAD_FAST_BORROW           total_drives
          310 FORMAT_SIMPLE              
          312 LOAD_CONST                 '] '
          314 LOAD_FAST_BORROW           drive
          316 FORMAT_SIMPLE              
          318 LOAD_CONST                 ' taranıyor...'
          320 LOAD_FAST_BORROW           Style
          322 LOAD_ATTR                  RESET_ALL
          342 FORMAT_SIMPLE              
          344 BUILD_STRING               
          346 CALL                       
          354 POP_TOP                    
          356 NOP                        
          358 LOAD_GLOBAL                os
          368 LOAD_ATTR                  walk
          388 PUSH_NULL                  
          390 LOAD_FAST_BORROW           drive
          392 CALL                       
          400 GET_ITER                   
          402 FOR_ITER                   to L15
          406 UNPACK_SEQUENCE            
          410 STORE_FAST_STORE_FAST      root, dirs
          412 STORE_FAST                 files
          414 LOAD_CONST                 False
          416 STORE_FAST                 skip_this
          418 LOAD_FAST_BORROW           skip_folders
          420 GET_ITER                   
          422 FOR_ITER                   to L7
          426 STORE_FAST                 skip
          428 LOAD_FAST_BORROW           skip
          430 LOAD_ATTR                  lower + NULL|self
          450 CALL                       
          458 LOAD_FAST_BORROW           root
          460 LOAD_ATTR                  lower + NULL|self
          480 CALL                       
          488 CONTAINS_OP                in
          492 POP_JUMP_IF_TRUE           to L6
          496 NOT_TAKEN                  
          498 JUMP_BACKWARD              to L5
          502 LOAD_CONST                 True
          504 STORE_FAST                 skip_this
          506 POP_TOP                    
          508 JUMP_FORWARD               to L8
          510 END_FOR                    
          512 POP_ITER                   
          514 LOAD_FAST_BORROW           skip_this
          516 TO_BOOL                    
          524 POP_JUMP_IF_FALSE          to L9
          528 NOT_TAKEN                  
          530 BUILD_LIST                 
          532 LOAD_FAST_BORROW           dirs
          534 LOAD_CONST                 slice(None, None, None)
          536 STORE_SUBSCR               
          540 JUMP_BACKWARD              to L4
          544 LOAD_FAST_BORROW           files
          546 GET_ITER                   
          548 FOR_ITER                   to L14
          552 STORE_FAST                 file
          554 LOAD_FAST_BORROW           file
          556 LOAD_ATTR                  lower + NULL|self
          576 CALL                       
          584 LOAD_ATTR                  endswith + NULL|self
          604 LOAD_CONST                 '.jar'
          606 CALL                       
          614 TO_BOOL                    
          622 POP_JUMP_IF_TRUE           to L11
          626 NOT_TAKEN                  
          628 JUMP_BACKWARD              to L10
          632 LOAD_GLOBAL                os
          642 LOAD_ATTR                  path
          662 LOAD_ATTR                  join + NULL|self
          682 LOAD_FAST_BORROW_LOAD_FAST_BORROW root, file
          684 CALL                       
          692 STORE_FAST                 full_path
          694 LOAD_FAST_BORROW           jar_files
          696 LOAD_ATTR                  append + NULL|self
          716 LOAD_FAST_BORROW           full_path
          718 CALL                       
          726 POP_TOP                    
          728 LOAD_FAST_BORROW           verbose
          730 TO_BOOL                    
          738 POP_JUMP_IF_TRUE           to L12
          742 NOT_TAKEN                  
          744 JUMP_BACKWARD              to L10
          748 LOAD_GLOBAL                len + NULL
          758 LOAD_FAST_BORROW           jar_files
          760 CALL                       
          768 LOAD_SMALL_INT             
          770 BINARY_OP                  %
          782 LOAD_SMALL_INT             
          784 COMPARE_OP                 bool(==)
          788 POP_JUMP_IF_TRUE           to L13
          792 NOT_TAKEN                  
          794 JUMP_BACKWARD              to L10
          798 LOAD_GLOBAL                print + NULL
          808 LOAD_CONST                 '    '
          810 LOAD_FAST_CHECK            Fore
          812 LOAD_ATTR                  GREEN
          832 FORMAT_SIMPLE              
          834 LOAD_CONST                 '• '
          836 LOAD_GLOBAL                len + NULL
          846 LOAD_FAST_BORROW           jar_files
          848 CALL                       
          856 FORMAT_SIMPLE              
          858 LOAD_CONST                 ' JAR bulundu...'
          860 LOAD_FAST_CHECK            Style
          862 LOAD_ATTR                  RESET_ALL
          882 FORMAT_SIMPLE              
          884 BUILD_STRING               
          886 LOAD_CONST                 '\r'
          888 LOAD_CONST                 True
          890 LOAD_CONST                 ('end', 'flush')
          892 CALL_KW                    
          900 POP_TOP                    
          902 JUMP_BACKWARD              to L10
          906 END_FOR                    
          908 POP_ITER                   
          910 EXTENDED_ARG               
          912 JUMP_BACKWARD              to L4
          916 END_FOR                    
          918 POP_ITER                   
          920 EXTENDED_ARG               
          922 JUMP_BACKWARD              to L2
          926 END_FOR                    
          928 POP_ITER                   
          930 LOAD_FAST_BORROW           verbose
          932 TO_BOOL                    
          940 POP_JUMP_IF_FALSE          to L17
          944 NOT_TAKEN                  
          946 LOAD_SMALL_INT             
          948 LOAD_CONST                 ('Fore', 'Style')
          950 IMPORT_NAME                colorama
          952 IMPORT_FROM                Fore
          954 STORE_FAST                 Fore
          956 IMPORT_FROM                Style
          958 STORE_FAST                 Style
          960 POP_TOP                    
          962 LOAD_GLOBAL                print + NULL
          972 LOAD_CONST                 '\n  '
          974 LOAD_FAST_BORROW           Fore
          976 LOAD_ATTR                  GREEN
          996 FORMAT_SIMPLE              
          998 LOAD_CONST                 '✓ Arama tamamlandı - '
         1000 LOAD_GLOBAL                len + NULL
         1010 LOAD_FAST_BORROW           jar_files
         1012 CALL                       
         1020 FORMAT_SIMPLE              
         1022 LOAD_CONST                 ' JAR bulundu'
         1024 LOAD_FAST_BORROW           Style
         1026 LOAD_ATTR                  RESET_ALL
         1046 FORMAT_SIMPLE              
         1048 BUILD_STRING               
         1050 CALL                       
         1058 POP_TOP                    
         1060 LOAD_FAST_BORROW           jar_files
         1062 RETURN_VALUE               
         1064 PUSH_EXC_INFO              
         1066 LOAD_GLOBAL                PermissionError
         1076 CHECK_EXC_MATCH            
         1078 POP_JUMP_IF_FALSE          to L19
         1082 NOT_TAKEN                  
         1084 POP_TOP                    
         1086 LOAD_FAST                  verbose
         1088 TO_BOOL                    
         1096 POP_JUMP_IF_FALSE          to L18
         1100 NOT_TAKEN                  
         1102 LOAD_GLOBAL                print + NULL
         1112 LOAD_CONST                 '    ⚠ Bazı klasörlere erişim reddedildi'
         1114 CALL                       
         1122 POP_TOP                    
         1124 POP_EXCEPT                 
         1126 EXTENDED_ARG               
         1128 JUMP_BACKWARD              to L2
         1132 POP_EXCEPT                 
         1134 EXTENDED_ARG               
         1136 JUMP_BACKWARD              to L2
         1140 LOAD_GLOBAL                Exception
         1150 CHECK_EXC_MATCH            
         1152 POP_JUMP_IF_FALSE          to L21
         1156 NOT_TAKEN                  
         1158 STORE_FAST                 e
         1160 LOAD_FAST                  verbose
         1162 TO_BOOL                    
         1170 POP_JUMP_IF_FALSE          to L20
         1174 NOT_TAKEN                  
         1176 LOAD_GLOBAL                print + NULL
         1186 LOAD_CONST                 '    ⚠ Hata: '
         1188 LOAD_FAST                  e
         1190 FORMAT_SIMPLE              
         1192 BUILD_STRING               
         1194 CALL                       
         1202 POP_TOP                    
         1204 POP_EXCEPT                 
         1206 LOAD_CONST                 None
         1208 STORE_FAST                 e
         1210 DELETE_FAST                e
         1212 EXTENDED_ARG               
         1214 JUMP_BACKWARD              to L2
         1218 POP_EXCEPT                 
         1220 LOAD_CONST                 None
         1222 STORE_FAST                 e
         1224 DELETE_FAST                e
         1226 EXTENDED_ARG               
         1228 JUMP_BACKWARD              to L2
         1232 LOAD_CONST                 None
         1234 STORE_FAST                 e
         1236 DELETE_FAST                e
         1238 RERAISE                    
         1240 RERAISE                    
         1242 COPY                       
         1244 POP_EXCEPT                 
         1246 RERAISE                    

    ### __annotate__  (line 94)
      [STR]
        'return'
      [names] ('List', 'str')
      [varnames] ('format',)

    ### get_common_locations  (line 93)
      [STR]
        '\nYaygın Minecraft lokasyonları (hızlı tarama için)\nDeprecated - artık tüm sistem taranıyor\n'
      [bytecode]
            0 RESUME                     
            2 BUILD_LIST                 
            4 RETURN_VALUE               

    ### __annotate__  (line 102)
      [STR]
        'return'
      [names] ('List', 'str')
      [varnames] ('format',)

    ### get_minecraft_instances  (line 101)
      [STR]
        '\nMinecraft instance dizinleri\nDeprecated - artık tüm sistem taranıyor\n'
      [bytecode]
            0 RESUME                     
            2 BUILD_LIST                 
            4 RETURN_VALUE               
