import os
import sys
from antlr4 import *
from gramatica3Lexer import gramatica3Lexer
from gramatica3Parser import gramatica3Parser

# Clase para visitar y procesar el árbol de análisis sintáctico de la transformada de Fourier
class VisitanteTransformadaFourier(ParseTreeVisitor):
    # Método para procesar la transformada de Fourier directa
    def visitarTransformadaDirecta(self, ctx):
        print("Resultado de la Transformada de Fourier Directa:")
        print(ctx.getText())
        return self.visitChildren(ctx)

    # Método para procesar la transformada de Fourier inversa
    def visitarTransformadaInversa(self, ctx):
        print("Resultado de la Transformada de Fourier Inversa:")
        print(ctx.getText())
        return self.visitChildren(ctx)

# Función principal que ejecuta el análisis del archivo de entrada
def principal(argv):
    # Leer el archivo de entrada que contiene la expresión
    flujo_entrada = FileStream(argv[1], encoding='utf-8')

    # Crear un lexer para analizar los tokens de la gramática
    lexer = gramatica3Lexer(flujo_entrada)
    flujo_tokens = CommonTokenStream(lexer)

    # Crear un parser para analizar la estructura sintáctica de la gramática
    parser = gramatica3Parser(flujo_tokens)
    arbol = parser.tf()

    # Imprimir el árbol generado (para depuración)
    print("\n\nÁrbol de análisis sintáctico:")
    print(arbol.toStringTree(recog=parser))

    # Visitar el árbol y mostrar el resultado de la transformada
    visitante = VisitanteTransformadaFourier()

    # Determinar si la expresión es directa o inversa
    if arbol.getChild(0).getText().startswith("F^-1"):
        visitante.visitarTransformadaInversa(arbol)
    else:
        visitante.visitarTransformadaDirecta(arbol)

# Punto de entrada del script
if __name__ == '__main__':
    principal(sys.argv)
