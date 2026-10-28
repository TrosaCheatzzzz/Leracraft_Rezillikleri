### CODE OBJECT: <module>  (file=scanner\direct_scan.py, line=1)
# consts:
  STR: '\nLeraScanner - Direct Auto Scan\nMen³ yok, direkt al²■²r, sadece sonular² g÷sterir\n'
  STR: '__main__'
  STR: '\n'
  STR: 'Tarama iptal edildi'
# names: ('__doc__', 'os', 'sys', 'time', 'datetime', 'colorama', 'init', 'Fore', 'Style', 'scanner.jar_scanner', 'JarScanner', 'scanner.memory_scanner', 'MemoryScanner', 'scanner.prefetch_scanner', 'PrefetchScanner', 'scanner.system_scanner', 'SystemScanner', 'print_banner', 'print_status', 'main', '__name__', 'KeyboardInterrupt', 'print', 'YELLOW', 'RESET_ALL', 'exit')
# varnames: ()
# bytecode:
       0 RESUME                       
       2 LOAD_CONST                   '\nLeraScanner - Direct Auto Scan\nMen³ yok, direkt al²■²r, sadece sonular² g÷sterir\n'
       4 STORE_NAME                   __doc__
       6 LOAD_SMALL_INT               
       8 LOAD_CONST                   None
      10 IMPORT_NAME                  os
      12 STORE_NAME                   os
      14 LOAD_SMALL_INT               
      16 LOAD_CONST                   None
      18 IMPORT_NAME                  sys
      20 STORE_NAME                   sys
      22 LOAD_SMALL_INT               
      24 LOAD_CONST                   None
      26 IMPORT_NAME                  time
      28 STORE_NAME                   time
      30 LOAD_SMALL_INT               
      32 LOAD_CONST                   ('datetime',)
      34 IMPORT_NAME                  datetime
      36 IMPORT_FROM                  datetime
      38 STORE_NAME                   datetime
      40 POP_TOP                      
      42 LOAD_SMALL_INT               
      44 LOAD_CONST                   ('init', 'Fore', 'Style')
      46 IMPORT_NAME                  colorama
      48 IMPORT_FROM                  init
      50 STORE_NAME                   init
      52 IMPORT_FROM                  Fore
      54 STORE_NAME                   Fore
      56 IMPORT_FROM                  Style
      58 STORE_NAME                   Style
      60 POP_TOP                      
      62 LOAD_SMALL_INT               
      64 LOAD_CONST                   ('JarScanner',)
      66 IMPORT_NAME                  scanner.jar_scanner
      68 IMPORT_FROM                  JarScanner
      70 STORE_NAME                   JarScanner
      72 POP_TOP                      
      74 LOAD_SMALL_INT               
      76 LOAD_CONST                   ('MemoryScanner',)
      78 IMPORT_NAME                  scanner.memory_scanner
      80 IMPORT_FROM                  MemoryScanner
      82 STORE_NAME                   MemoryScanner
      84 POP_TOP                      
      86 LOAD_SMALL_INT               
      88 LOAD_CONST                   ('PrefetchScanner',)
      90 IMPORT_NAME                  scanner.prefetch_scanner
      92 IMPORT_FROM                  PrefetchScanner
      94 STORE_NAME                   PrefetchScanner
      96 POP_TOP                      
      98 LOAD_SMALL_INT               
     100 LOAD_CONST                   ('SystemScanner',)
     102 IMPORT_NAME                  scanner.system_scanner
     104 IMPORT_FROM                  SystemScanner
     106 STORE_NAME                   SystemScanner
     108 POP_TOP                      
     110 LOAD_NAME                    init
     112 PUSH_NULL                    
     114 LOAD_CONST                   True
     116 LOAD_CONST                   ('autoreset',)
     118 CALL_KW                      
     126 POP_TOP                      
     128 LOAD_CONST                   <code object print_banner at 0x0000016335CF6310, file "scanner\direct_scan.py", line 20>
     130 MAKE_FUNCTION                
     132 STORE_NAME                   print_banner
     134 LOAD_CONST                   <code object print_status at 0x0000016335F89070, file "scanner\direct_scan.py", line 27>
     136 MAKE_FUNCTION                
     138 STORE_NAME                   print_status
     140 LOAD_CONST                   <code object main at 0x000001633617F520, file "scanner\direct_scan.py", line 32>
     142 MAKE_FUNCTION                
     144 STORE_NAME                   main
     146 LOAD_NAME                    __name__
     148 LOAD_CONST                   '__main__'
     150 COMPARE_OP                   bool(==)
     154 POP_JUMP_IF_FALSE            to L1
     158 NOT_TAKEN                    
     160 NOP                          
     162 LOAD_NAME                    main
     164 PUSH_NULL                    
     166 CALL                         
     174 POP_TOP                      
     176 LOAD_CONST                   None
     178 RETURN_VALUE                 
     180 LOAD_CONST                   None
     182 RETURN_VALUE                 
     184 PUSH_EXC_INFO                
     186 LOAD_NAME                    KeyboardInterrupt
     188 CHECK_EXC_MATCH              
     190 POP_JUMP_IF_FALSE            to L2
     194 NOT_TAKEN                    
     196 POP_TOP                      
     198 LOAD_NAME                    print
     200 PUSH_NULL                    
     202 LOAD_CONST                   '\n'
     204 LOAD_NAME                    Fore
     206 LOAD_ATTR                    YELLOW
     226 FORMAT_SIMPLE                
     228 LOAD_CONST                   'Tarama iptal edildi'
     230 LOAD_NAME                    Style
     232 LOAD_ATTR                    RESET_ALL
     252 FORMAT_SIMPLE                
     254 BUILD_STRING                 
     256 CALL                         
     264 POP_TOP                      
     266 LOAD_NAME                    sys
     268 LOAD_ATTR                    exit
     288 PUSH_NULL                    
     290 LOAD_SMALL_INT               
     292 CALL                         
     300 POP_TOP                      
     302 POP_EXCEPT                   
     304 LOAD_CONST                   None
     306 RETURN_VALUE                 
     308 RERAISE                      
     310 COPY                         
     312 POP_EXCEPT                   
     314 RERAISE                      

  ### CODE OBJECT: print_banner  (file=scanner\direct_scan.py, line=20)
  # consts:
    STR: 'Banner'
    STR: '\n'
