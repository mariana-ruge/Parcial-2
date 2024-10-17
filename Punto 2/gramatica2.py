from antlr4 import *
from gramatica2Lexer import gramatica2Lexer
from gramatica2Parser import gramatica2Parser
from gramatica2Visitor import gramatica2Visitor

# Definición de funciones para MAP y FILTER
def doble(x):
    return x * 2

def es_par(x):
    return x % 2 == 0

# Diccionario de funciones disponibles
funciones_disponibles = {
    "doble": doble,
    "es_par": es_par,
}

# Clase visitante para procesar el árbol de la gramática
class VisitanteMapFilter(gramatica2Visitor):

    # Método para visitar la operación MAP
    def visitOperacionMap(self, ctx):
        print("Visitando operación MAP...")
        funcion = ctx.funcion().getText()
        iterable = self.visit(ctx.iterable())

        print(f"Función obtenida: {funcion}")
        print(f"Iterable obtenido: {iterable}")

        # Verificar si la función está en el diccionario
        if funcion not in funciones_disponibles:
            print(f"Error: La función '{funcion}' no está definida.")
            return None

        # Verificar si el iterable es válido
        if iterable is None or not isinstance(iterable, list):
            print("Error: El iterable no fue obtenido correctamente.")
            return None

        # Aplicar la función sobre cada elemento del iterable
        resultado = []
        for x in iterable:
            print(f"Aplicando función '{funcion}' a: {x}")
            resultado.append(funciones_disponibles[funcion](x))
            print(f"Resultado parcial: {resultado}")

        return resultado

    # Método para visitar la operación FILTER
    def visitOperacionFilter(self, ctx):
        print("Visitando operación FILTER...")
        condicion = ctx.condicion().getText()
        iterable = self.visit(ctx.iterable())

        print(f"Condición obtenida: {condicion}")
        print(f"Iterable obtenido: {iterable}")

        # Verificar si la condición está en el diccionario
        if condicion not in funciones_disponibles:
            print(f"Error: La condición '{condicion}' no está definida.")
            return None

        # Verificar si el iterable es válido
        if iterable is None or not isinstance(iterable, list):
            print("Error: El iterable no fue obtenido correctamente.")
            return None

        # Filtrar los elementos del iterable según la condición
        resultado = []
        for x in iterable:
            if funciones_disponibles[condicion](x):
                resultado.append(x)
                print(f"Elemento {x} cumple la condición '{condicion}'")

        return resultado

    # Método para visitar una lista
    def visitLista(self, ctx):
        print("Visitando lista...")
        elementos = self.visit(ctx.elementos())
        print(f"Elementos obtenidos: {elementos}")
        return elementos

    # Método para visitar una tupla
    def visitTupla(self, ctx):
        print("Visitando tupla...")
        elementos = self.visit(ctx.elementos())
        print(f"Elementos obtenidos: {elementos}")
        return elementos

    # Método para visitar múltiples elementos dentro de una lista o tupla
    def visitMultiplesElementos(self, ctx):
        print("Visitando múltiples elementos...")
        elementos = [int(e.getText()) for e in ctx.elemento()]
        print(f"Elementos procesados: {elementos}")
        return elementos

    # Método para visitar cuando no hay elementos
    def visitSinElementos(self, ctx):
        print("Visitando sin elementos...")
        return []

# Función principal para ejecutar el programa
def main():
    try:
        # Lee la expresión introducida por el usuario
        entrada = InputStream(input("Introduce la operación MAP o FILTER: "))

        # Crea el lexer para analizar la entrada
        lexer = gramatica2Lexer(entrada)

        # Tokeniza la entrada
        tokens = CommonTokenStream(lexer)

        # Crea el parser para procesar los tokens
        parser = gramatica2Parser(tokens)

        # Genera el árbol de la expresión
        arbol = parser.inicio()
        if arbol is None:
            print("No se pudo generar el árbol de análisis sintáctico.")
            return

        print("Árbol de análisis generado correctamente.")

        # Crea un visitante para recorrer el árbol
        visitante = VisitanteMapFilter()

        # Visita el árbol y calcula el resultado
        resultado = visitante.visit(arbol)

        # Imprime el resultado si existe
        if resultado is not None:
            print(f"Resultado: {resultado}")
        else:
            print("No se pudo calcular el resultado.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Punto de entrada del programa
if __name__ == '__main__':
    main()
