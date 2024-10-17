// Gramática para operaciones de MAP y FILTER
grammar gramatica2;

// Regla inicial
inicio  : operacion EOF;

// Definición de las operaciones MAP y FILTER
operacion 
        : 'MAP' '(' funcion ',' iterable ')'   # OperacionMap
        | 'FILTER' '(' condicion ',' iterable ')' # OperacionFilter
        ;

// Definición de una función para MAP
funcion : IDENTIFICADOR;

// Definición de una condición para FILTER
condicion : IDENTIFICADOR;

// Definición de un objeto iterable (lista o tupla)
iterable : '[' elementos ']'           # Lista
         | '(' elementos ')'           # Tupla
         ;

// Definición de los elementos dentro de la lista o tupla
elementos : elemento (',' elemento)*   # MultiplesElementos
          |                            # SinElementos
          ;

elemento : INT;

// Tokens
IDENTIFICADOR : [a-zA-Z_][a-zA-Z0-9_]*;
INT           : [0-9]+;
ESPACIOS      : [ \t\r\n]+ -> skip;
