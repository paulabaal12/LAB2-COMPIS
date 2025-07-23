grammar SimpleLang;

prog: stat+ ;

stat: expr NEWLINE ;

expr: expr op=('*'|'/'|'%'|'^') expr       # MulDivModPow
    | expr op=('+'|'-') expr                # AddSub
    | expr op=('>'|'<') expr                # Compare
    | expr op='&&' expr                     # And
    | INT                                   # Int
    | FLOAT                                 # Float
    | STRING                                # String
    | BOOL                                  # Bool
    | '(' expr ')'                          # Parens
    ;

INT: [0-9]+ ;
FLOAT: [0-9]+'.'[0-9]* ;
STRING: '"' .*? '"' ;
BOOL: 'true' | 'false' ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;
