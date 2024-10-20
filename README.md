# Parcial 2

**Desarrollado por:**
- Mariana Ruge Vargas

## Descripción
Este repositorio contiene los ejercicios del Parcial del Segundo Corte, desarrollados por separado en ANTLR (Another Tool For Language Recognition) con lenguaje objetivo en Python ('Lenguaje objetivo': se refiere al lenguaje en el que se genera el código del Parser a partir de una gramática definida).

Cada punto se encuentra en su respectiva carpeta.

## Estructura del Repositorio

- **Punto 1**:  Contiene la gramática (.g4) y programa en Python para una calculadora de números complejos (aquellos que tienen parte real e imaginaria), hace las 4 operaciones básicas (suma, resta, multiplica y divide, y genera precedencia con los paréntesis).
- **Punto 2**: Se aplica la función MAP para un objeto iterable (como una lista o una tupla)  dependendiendo de una función definida  y devuelve una colección nueva con los resultados. También se implementa la función FILTER , que es para filtrar los elementos de un iterable de acuerdo a una condición.
- **Punto 3**:  Se define la gramática e implementación del cálculo de la transformada de Fourier, la principal función de esta transformada es descomponer señales en sus componentes de frecuencias (f) en función del tiempo (t). Y corresponde a la siguien fórmula:
[![](https://www.nobbot.com/wp-content/uploads/2021/05/transformada-de-fourier-integral.png)](https://www.nobbot.com/wp-content/uploads/2021/05/transformada-de-fourier-integral.png)

## Requisitos

- **Python 3.x** : Puedes verificar si lo tienes instalado con el siguiente comando.
   ```bash
  python --version
   ```
   En caso de no tenerlo instalado, ejecuta:
   ```bash
  sudo apt install python
   ```
- **ANTLR4 (ANother Tool for Language Recognition) **:  Es un potente generador de analizadores sintácticos para leer, procesar, ejecutar o traducir texto estructurado o archivos binarios. Se utiliza ampliamente para crear lenguajes, herramientas y marcos.
**Para instalarlo:**
1. Instala el JDK (Java Development Kit):

**Version del JDK -> JDK 21**

		sudo apt update
		sudo apt install openjdk-21-jdk

2. Descarga el archivo .jar de esta página: [Descargas ANTLR](https://www.antlr.org/download.html "Descargas ANTLR")
**Versión de ANTLR4 **: 4.13.2

3. Configura la variable de entorno en el archivo fuente de la terminal para ubicar el archivo jar,
		alias antlr4='Ruta al archivo .jar'
por ejemplo:
		alias antlr4='java -jar /usr/local/lib/antlr-4.x-complete.jar'


4. Verifica la instalación:
		 antlr4 --version

- **ANTLR4 Python Runtime**: Es la biblioteca que proporciona las herramientas necesarias para ejecutar analizadores léxicos y sintácticos generados por ANTLR en Python.
**Versión de ANTLR4 Python Runtime **: 4.7.2
Para verificar su instalación puedes usar este comando:
		pip show antlr4-python3-runtime
En caso de no tenerlo instalado, ejecuta:

		pip install  antlr4-python3-runtime

Para mas información sobre ANTLR puedes vistar:
[Github Oficial ANTLR ](https://github.com/antlr/antlr4/blob/master/doc/python-target.md "Github Oficial ANTLR ")


## Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/mariana-ruge/Parcial-2.git
   ```
2. Navegar al directorio.
   ```bash
   cd 'Parcial-2'
   ```
**Verificar con `ls` que las carpetas coincidan con las descritas en la estructura del proyecto**

3. Buscar el punto deseado.
 ```bash
   cd 'Punto-"numero del punto"'
   ```
**En cada punto hay 2 archivos el .g4  y el .py**
4. Para compilar el proyecto y generar los archivos necesarios para el correcto funcionamiento, ejecuta:
 ```bash
   antlr4  -Dlanguage=Python3  -visitor archivo.g4
   ```
Reemplazar el "archivo.g4" con el nombre que se vea en la carpeta del g4 correspondiente.

5. Una vez compilado y generados los archivos, ejecuta con python el programa.
 ```bash
   python 'nombre_del_archivo.py'
   ```
- El **Punto 3** requiere un archivo txt en la entrada,  así que su ejecución será:
 ```bash
   python 'nombre_del_archivo.py' ' entrada.txt'
   ```
Se deberá mostrar la respectiva ejecución de cada uno de los puntos.