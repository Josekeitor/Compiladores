grammar activity;

program : expression+ | statement+;

expression: 
    expression op=ADD expression #suma
    | expression op=EQUAL expression #asignacion
    | expression op=GREATER_THAN expression #comparacion
    | Number                  #numero
    | Letter                  #letra
    ;

statement: 
    'if (' expression ') then' statement ('else' statement)? #if
    |  'print(' expression ')' #print
    ;

Number: [0-9]+;

Letter: [a-zA-Z]+;

ADD: '+';
EQUAL: '=';
GREATER_THAN: '>';

WS : [ \t\n\r]+ -> skip;
