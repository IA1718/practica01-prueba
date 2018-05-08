# -*- coding: utf-8 -*-
# Inteligencia Artificial. Universidad de La Rioja.
# Curso 2017-2018.
# Nombre y apellidos:

#=========================================================
# Práctica 1. Introducción a Python
#=========================================================

##########################################################
# Objetivos
# * Familiarizarnos con el lenguaje Python.
#     - Familiarizarnos con el interprete de Python.
#     - Definir funciones en Python.
#     - Trabajar con los tipos básicos de Python.
# * Familiarizarnos con el IDE PyCharm.
##########################################################

#---------------------------------------------------------
# Pasos previos
#---------------------------------------------------------

# 0. Inicia la máquina virtual de Linux
# 1. Descarga los ficheros practica1.py y testPractica1.py
#    del aula virtual.
# 2. Guardalos en un directorio en el que tengas permiso
#    de escritura.
# 3. Entra a PyCharm.
# 4. Crea un proyecto llamado Practica1 en el directorio
#    donde hayas guardado los fichero de la práctica.
# 5. Abre desde el IDE el fichero practica1.py.
# 6. Desde el IDE de Pycharm abre una terminal:
#    View -> Tool Windows -> Terminal
# 7. Desde la terminal, ve a la carpeta del proyecto.
# 8. En la terminal ejecuta el comando python. Esto
#    inicia el interprete de Python en la terminal.

#---------------------------------------------------------
# Comprobando tus soluciones
#---------------------------------------------------------

# En la práctica se proponen una serie de ejercicios que
# tendrás que ir resolviendo.

# Para saber si las soluciones que vas dando a los distintos
# ejercicios son correctas, puedes ejecutar los tests que se
# proporcionan en el fichero testPractica1. Para ello ejecuta
# desde la línea de comandos la instrucción:
# python testPractica1.py
# Esto mostrará para cada uno de los ejercicios si la
# solución que has dado supera los tests definidos en
# dicho fichero.

# En todas las prácticas se proporcionan una serie de ejercicios
# mínimos (realizando correctamente todos los ejercicios de esta
# parte se obtiene un 8) y unos ejercicios de ampliación.

# Los ejercicios adicionales también se pueden validar utilizando
# el fichero testAdicionalesPractica1. Para ello ejecuta
# desde la línea de comandos la instrucción:
# python testAdicionalesPractica1.py
# Esto mostrará para cada uno de los ejercicios si la
# solución que has dado supera los tests definidos en
# dicho fichero.

#/////////////////////////////////////////////////////////
# Ejercicios mínimos
#/////////////////////////////////////////////////////////

#---------------------------------------------------------
# Ejercicio 1.
#---------------------------------------------------------

# Teclea en el interprete las siguientes instrucciones:
# (50-5*6)/4
# ancho = 20
# alto = 5*9
# area = ancho*alto
# area
# True and 2==3
# exit()

#---------------------------------------------------------
# Ejercicio 2.
#---------------------------------------------------------

# A continuación vemos cómo se define una función, y cómo
# se puede utilizar desde el interprete de Python.

# La siguiente función toma un número y le suma 44.
def mas44(x):
    return x + 44

# Desde el intérprete carga este módulo usando:
# import practica1

# Ahora puedes utilizar la función mas44 desde el interprete
# del siguiente modo:
# practica1.mas44(5)

# Responde a continuación. ¿De qué otros modos se pueden
# cargar los módulos en Python?

#---------------------------------------------------------
# Ejercicio 3.
#---------------------------------------------------------

# Define una función que dados dos números devuelva el
# mayor de ellos. Utiliza la siguiente cabecera.

def maximo(x,y):
    # el pass debe ser reemplazado por la definición de la
    # función.
    pass

# Guarda el fichero y comprueba que la función maximo es
# correcta desde el interprete.

#---------------------------------------------------------
# Ejercicio 4.
#---------------------------------------------------------

# Define una función que dado un string, devuelve un string
# que contiene los dos primeros y los dos últimos caracteres
# del string; es decir, si la función recibe 'primavera',
# la función devolverá 'prra'. Sin embargo, si la longitud
# del string es menor que dos, la función devolverá el
# string vacio.

def principio_fin(s):
    pass

#---------------------------------------------------------
# Ejercicio 5.
#---------------------------------------------------------

# Define una función que dado un string s, devuelve un string
# donde todas las ocurrencias del primer carácter de s han
# sido reemplazadas por '*', exceptuando el primer carácter.
# Ejemplo. 'babble' produce 'ba**le'.
# Pista. s.replace(stra, strb) devuelve una versión de s
# donde todas las ocurrencias de stra han sido cambiadas
# por strb.

def comienzo_fijo(s):
    pass

#---------------------------------------------------------
# Ejercicio 6.
#---------------------------------------------------------

# Define una función que dado un string s, devuelva una
# tupla con dos elementos, donde el primer elemento de la
# tupla es el número de letras del string y el segundo
# elemento es el número de números del string.
def cuenta_letras_numeros(s):
    pass

#---------------------------------------------------------
# Ejercicio 7.
#---------------------------------------------------------

# Define una función que dada una lista de strings devuelva
# el número de strings cuya longitud es mayor que 2 y que
# además cumplen que el primer y último carácter del string
# son el mismo.

def cuenta_strings(palabras):
    pass

#---------------------------------------------------------
# Ejercicio 8.
#---------------------------------------------------------

# Define una función que dada dos listas de igual tamaño
# produce una lista de tuplas combinando los elementos de
# las dos listas. Ejemplo: dadas las listas [1,2,3] y
# ['a','b','c'] produce la lista [(1,'a'), (2,'b'), (3,'c')].
# En caso de que las dos listas no tengan la misma longitud,
# la función devolverá el string 'listas no validas'.

def combina_listas(lista1,lista2):
    pass

#---------------------------------------------------------
# Ejercicio 9.
#---------------------------------------------------------

# Define una función que dada dos listas de números, las
# mezcla y devuelve la mezcla ordenada. Ejemplo: dadas las
# listas [4,1,3] y [2,5] devuelve la lista [1,2,3,4,5]

def mezcla_y_ordena(lista1,lista2):
    pass

#---------------------------------------------------------
# Ejercicio 10.
#---------------------------------------------------------

# Define una función que dada una lista de elementos,
# devuelve una lista donde todos los elementos adyacentes
# que son iguales han sido reducidos a un único elemento.
# Ejemplo: Dada la lista [1,2,2,3] produce la lista [1,2,3]

def elimina_adyacentes(lista):
    pass

#---------------------------------------------------------
# Ejercicio 11.
#---------------------------------------------------------

# Define una función que dada una tupla de elementos,
# devuelve una lista con los elementos de la tupla

def tupla_a_lista(tupla):
    pass

#---------------------------------------------------------
# Ejercicio 12.
#---------------------------------------------------------

# Define una función que dados dos conjuntos de elementos
# devuelva un nuevo conjunto con los elementos del primer
# conjunto que no están en el segundo.

def diferencia_conjuntos(c1,c2):
    pass


#/////////////////////////////////////////////////////////
# Ejercicio de ampliación
#/////////////////////////////////////////////////////////

# El código genético de todos los organismos vivos se
# representa mediante una secuencia enorme de moléculas
# llamadas nucleótidos que forman el ADN. Sólo existen 4
# nucleótidos y el código genético puede verse como un
# string con las letras A, C, G y T.

# El análisis de datos de ADN se basa, en parte, en buscar
# largas cadenas de patrones de string que involucran a las
# letras A, C, G, y T. Con estos ejercicios veremos algunos
# ejemplos de ello. Para aplicaciones reales no es
# recomendable utilizar soluciones a mano y existen librerías
# como BioPython (http://biopython.org/)

# El primer ejercicio consiste en definir una función que 
# verifique que un string es una secuencia de ADN es decir
# que solo contiene las letras A, C, G, y T. La función
# devolverá True en caso de que el parámetro de entrada
# sea una secuencia de ADN y False en caso contrario.

def es_secuencia_adn(secuencia):
    pass



# Dada una secuencia de ADN (un string) que contiene las
# letras A, C, G, y T queremos conocer cuántas veces
# aparece una cierta base en dicha secuencia. Por ejemplo,
# para la secuencia ATGGCATTA, la base A ocurre 3 veces.
# Define una función con esta funcionalidad #

def cuenta(adn, base):
    pass


# El siguiente ejercicio consiste en calcular la frecuencia
# en la que aparece cada letra en cada posición de una lista
# de secuencias (todas las secuencias de la lista tienen
# el mismo número de elementos).
# El resultado será una tupla de listas, donde
# la primera lista corresponde a las frecuencias de A, la
# segunda a las frecuencias de C, la tercera a las de G y la
# cuarta a las de T. Por ejemplo, dada la lista de secuencias
# ['ATGACT', 'AACTGT', 'GGCTAT'] el resultado sería:
# ([2,1,0,1,1,0],[0,0,2,0,1,0],[1,1,1,0,1,0],[0,1,0,1,0,3])

def frecuencias(lista_adns):
    pass

# A continuación pasamos a definir una función que genere
# secuencias aleatorias de adn de un tamaño dado. Para ello
# deberás importar la librería random (import random) y
# utilizar alguna de sus funciones.
# Puedes ver las funciones de esta librería en:
# https://docs.python.org/2/library/random.html
# Pista. Busca una función en esta librería que devuelva
# un elemento aleatorio de una secuencia.

def genera_adn(tam):
    pass


#=========================================================
# Entregable
#=========================================================

# Guarda este fichero con tus soluciones a los distintos
# ejercicios, introduciendo tu nombre al principio
# del mismo. Deberás entregar en un zip este fichero junto
# a los ficheros de test.
