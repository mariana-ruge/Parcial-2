from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor

# Clase visitante para procesar el árbol de la gramática
class VisitanteNumerosComplejos(gramaticaVisitor):

    # Método para visitar una expresión de suma o resta
    def visitSumaResta(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        operador = ctx.getChild(1).getText()
        if operador == '+':
            return izquierda + derecha
        elif operador == '-':
            return izquierda - derecha

    # Método para visitar una expresión entre paréntesis
    def visitExpresionParentesis(self, ctx):
        return self.visit(ctx.expresion())

    # Método para visitar un término único (que puede ser un número real o complejo)
    def visitTerminoUnico(self, ctx):
        return self.visit(ctx.termino())

    # Método para visitar un número complejo con suma (a + bi)
    def visitNumeroComplejoSuma(self, ctx):
        parte_real = int(ctx.INT(0).getText())
        parte_imaginaria = int(ctx.INT(1).getText())
        return complex(parte_real, parte_imaginaria)

    # Método para visitar un número complejo con resta (a - bi)
    def visitNumeroComplejoResta(self, ctx):
        parte_real = int(ctx.INT(0).getText())
        parte_imaginaria = -int(ctx.INT(1).getText())
        return complex(parte_real, parte_imaginaria)

    # Método para visitar un número real simple
    def visitNumeroReal(self, ctx):
        return int(ctx.INT().getText())

    # Método para visitar cualquier otro nodo (respaldo en caso de no encontrar un visit específico)
    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            child_result = self.visit(node.getChild(i))
            if result is None:
                result = child_result
        return result

# Función principal para ejecutar el programa
def main():
    # Lee la expresión introducida por el usuario
    entrada = InputStream(input("Introduce la expresión: "))

    # Crea el lexer para analizar la entrada
    lexer = gramaticaLexer(entrada)

    # Tokeniza la entrada
    tokens = CommonTokenStream(lexer)

    # Crea el parser para procesar los tokens
    parser = gramaticaParser(tokens)

    # Genera el árbol de la expresión
    arbol = parser.inicio()

    # Crea un visitante para recorrer el árbol
    visitante = VisitanteNumerosComplejos()

    # Visita el árbol y calcula el resultado
    resultado = visitante.visit(arbol)

    # Imprime el resultado
    print(f"Resultado: {resultado}")

# Punto de entrada del programa
if __name__ == '__main__':
    main()
