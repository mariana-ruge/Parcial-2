grammar gramatica3;

// Regla inicial
tf: transformadaInversa | transformadaDirecta;

// Definición de la transformada de Fourier directa
transformadaDirecta: 'F' LBRACKET 'f' '(' T ')' RBRACKET '=' INTEGRAL f '(' T ')' EXP '^' '(' '-' J W T ')' 'd' T;

// Definición de la transformada de Fourier inversa
transformadaInversa: 'F^-1' LBRACKET 'F' '(' W ')' RBRACKET '=' '1' '/' '(' '2' PI ')' INTEGRAL f '(' W ')' EXP '^' '(' J W T ')' 'd' W;

// Definición de funciones y terminales
f: 'f';

// Terminales para operaciones y constantes
LBRACKET: '[';
RBRACKET: ']';
INTEGRAL: '∫';
FUNCION: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;
PI: 'pi';
J: 'j';
W: 'w';
T: [tT];
MAS: '+';
MENOS: '-';
MULT: '*';
DIV: '/';
EXP: 'e';
ESPACIO: [ \t\r\n]+ -> skip;

// Reglas para manejar expresiones matemáticas comunes
expresionMatematica: expresionMatematica MAS expresionMatematica
                   | expresionMatematica MENOS expresionMatematica
                   | expresionMatematica MULT expresionMatematica
                   | expresionMatematica DIV expresionMatematica
                   | FUNCION '(' expresionMatematica ')'
                   | NUMERO
                   | T
                   | W;
