// Gramática para ANTLR (NumerosComplejos.g4)

// Define la gramática para la calculadora de números complejos.
grammar complejos;

// Reglas principales
expresion: termino ((SUMA | RESTA) termino)*;
termino: factor ((MULTIPLICA | DIVIDE) factor)*;
factor: PARENTESIS_IZQ expresion PARENTESIS_DER | numeroComplejo;
numeroComplejo: REAL (SUMA | RESTA)? REAL? 'i'?;

// Tokens
SUMA: '+';
RESTA: '-';
MULTIPLICA: '*';
DIVIDE: '/';
PARENTESIS_IZQ: '(';
PARENTESIS_DER: ')';
REAL: [0-9]+;
WS: [ \t\n\r]+ -> skip;
