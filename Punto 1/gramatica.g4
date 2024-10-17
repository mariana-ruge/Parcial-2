// Gramática para operaciones con números complejos
grammar gramatica;

// Regla inicial que define una expresión y compara dos expresiones con un "=" para ver si son iguales
inicio  : expresion EOF;

// Regla que define una expresión, que puede ser una suma, resta o un solo término
expresion
        : expresion ('+' | '-') expresion   # SumaResta
        | '(' expresion ')'                 # ExpresionParentesis
        | termino                           # TerminoUnico
        ;

// Regla que define los términos (números reales o complejos)
termino : INT '+' INT 'i'                 # NumeroComplejoSuma
        | INT '-' INT 'i'                 # NumeroComplejoResta
        | INT                             # NumeroReal
        ;

// Regla para los números enteros
INT     : [0-9]+;

// Regla para ignorar espacios en blanco
ESPACIOS : [ \t\r\n]+ -> skip;

// Tokens para paréntesis
LPAREN  : '(';
RPAREN  : ')';

