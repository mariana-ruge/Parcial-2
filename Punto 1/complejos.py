import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from complejosLexer import complejosLexer
from complejosParser import complejosParser

class CalculadoraComplejos(ParseTreeVisitor):
    """
    Clase que define la lógica para evaluar expresiones de números complejos.
    Extiende de ParseTreeVisitor para recorrer el árbol de análisis generado por el parser.
    """

    # Visita la expresión principal y realiza las operaciones aritméticas entre números complejos
    def visitExpresion(self, ctx):
        # Inicia el resultado con el primer término
        resultado = self.visit(ctx.termino(0))
        # Itera sobre los siguientes términos y aplica las operaciones de suma o resta
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(2 * (i - 1) + 1).getText()
            if operador == '+':
                resultado += self.visit(ctx.termino(i))
            elif operador == '-':
                resultado -= self.visit(ctx.termino(i))
        return resultado

    # Visita un término y realiza las operaciones de multiplicación o división
    def visitTermino(self, ctx):
        # Inicia el resultado con el primer factor
        resultado = self.visit(ctx.factor(0))
        # Itera sobre los siguientes factores y aplica las operaciones de multiplicación o división
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(2 * (i - 1) + 1).getText()
            if operador == '*':
                resultado *= self.visit(ctx.factor(i))
            elif operador == '/':
                divisor = self.visit(ctx.factor(i))
                if divisor == 0:
                    raise ZeroDivisionError("Error: División por cero no permitida.")
                resultado /= divisor
        return resultado

    # Visita un factor y delega al número complejo o a la expresión entre paréntesis
    def visitFactor(self, ctx):
        if ctx.getChildCount() == 3:  # Si el factor es una expresión entre paréntesis
            return self.visit(ctx.expresion())
        return self.visit(ctx.numeroComplejo())

    # Visita un número complejo y lo convierte en un objeto complejo de Python
    def visitNumeroComplejo(self, ctx):
        real = int(ctx.REAL(0).getText()) if ctx.REAL(0) else 0
        imaginario = int(ctx.REAL(1).getText()) if ctx.REAL(1) else 0
        # Si el operador es resta, convierte la parte imaginaria en negativa
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '-':
            imaginario = -imaginario
        if ctx.getChildCount() == 1:
            return complex(real, 0)
        return complex(real, imaginario)

class ParserNumerosComplejos:
    """
    Clase encargada de inicializar el lexer y el parser para analizar la expresión.
    """

    def __init__(self, expresion):
        # Inicializa el lexer y el parser con la expresión proporcionada
        input_stream = InputStream(expresion)
        lexer = complejosLexer(input_stream)
        stream = CommonTokenStream(lexer)
        self.parser = complejosParser(stream)

    def parsear(self):
        # Parsea la expresión y retorna el árbol de análisis
        return self.parser.expresion()

def main():
    """
    Función principal que ejecuta el programa, solicita expresiones al usuario,
    las evalúa y muestra el resultado, permitiendo salir con la palabra "salir".
    """
    # Primera vez se solicita ingresar una expresión
    print("Ingrese la expresión de números complejos o escriba 'salir' para terminar:")

    while True:
        # Lee la expresión de números complejos desde la entrada por consola
        expresion = input("> ")

        # Verifica si el usuario quiere salir
        if expresion.lower() == "salir":
            print("Programa terminado.")
            break
        
        try:
            # Crea una instancia del parser y parsea la expresión
            parser = ParserNumerosComplejos(expresion)
            tree = parser.parsear()
            
            # Crea una instancia de la calculadora y evalúa la expresión
            calculadora = CalculadoraComplejos()
            resultado = calculadora.visit(tree)
            
            # Imprime el resultado de la operación
            print(f'Resultado: {resultado}')
        
        except ZeroDivisionError as e:
            # Captura la división por cero y muestra un mensaje de error
            print(e)
        except ValueError as e:
            # Captura errores de conversión de tipos y muestra un mensaje de error
            print(e)
        except Exception as e:
            # Captura cualquier otro error y muestra un mensaje de error
            print(f"Error inesperado: {e}")

if __name__ == '__main__':
    # Ejecuta el programa
    main()
