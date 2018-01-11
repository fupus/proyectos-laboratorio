# -*- coding: utf-8 -*-
''' Análisis de resultados electorales

AUTOR: José A. Troyano
REVISOR: Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 22/12/2017

En este proyecto trabajaremos con datos de escrutinios electorales. Estos datos
son públicos y podemos descargarlos desde muchas fuentes. Por ejemplo, las
ediciones digitales de los periódicos son una buena opción. Los ficheros de
entrada estarán en formato CSV y contendrán, en cada línea, el número de votos
que ha obtenido un partido en una determinada provincia. Estas son las primeras
líneas de un fichero de entrada:

    Provincia,Partido,Votos
    Almería,PP,99917
    Almería,PSOE-A,88709
    Almería,PODEMOS,29496
    Almería,C's,25335
    Almería,IULV-CA,11300
    Almería,UPyD,4822

A partir de estos datos, generaremos distintos informes y gráficos para poder
analizar los resultados electorales desde distintos puntos de vista. Por
último, implementaremos el sistema D'Hont que es uno de los más utilizados a la
hora de asignar escaños a los partidos en función de los votos. Gracias a esta
implementación podremos comparar, por ejemplo, el número de escaños que se
obtienen con la asignación por provincias (sistema actual en España) frente a
una asignación mediante circunscripción unica (sumando los votos de todas las
provincias).

Disponemos de dos conjuntos de datos correspondientes a:
   - Elecciones autonómicas de Andalucía (2015)
   - Elecciones autonómicas de Cataluña (2016)  

Las distribuciones de diputados por provincia, para cada una de las dos
elecciones, están especificadas en los siguientes diccionarios:

diputados = {'Almería': 12,
           'Cádiz': 15,
           'Córdoba': 12,
           'Granada': 13,
           'Huelva': 11,
           'Jaén': 11,
           'Málaga': 17,
           'Sevilla: 18
           }

diputados = {'Barcelona': 85,
           'Girona': 17,
           'Lleida': 15,
           'Tarragona': 18
           }

FUNCIONES DISPONIBLES:
----------------------
- lee_escrutinio(fichero):
    lee el fichero de escrutinio y devuelve una lista de tuplas
- calcula_provincias(registros):
    calcula el conjunto de provincias presente en un escrutinio
- calcula_partidos(registros):
    calcula el conjunto de partidos presente en un escrutinio
- votos_por_partido(registros):
    calcula el total de votos para cada partido
- genera_diagrama_tarta(diccionario, limite):
    genera un diagrama de tarta a partir de un diccionario de valores
- calcula_tabla_votos(registros):
    calcula una tabla bidimensional a partir de una lista de registros
- genera_mapa_calor(tabla, provincias, partidos, fmt):
    genera un mapa de calor a partir de una tabla de valores
- calcula_tabla_porcentajes(tabla):
    convierte una tabla de votos en porcentajes
- calcula_diputados(votos_partidos, total_diputados, exclusion):
    calcula los escaños correspondientes a cada partido
- calcula_tabla_diputados(tabla_votos, distribucion, exclusion=0.03):
    convierte una tabla de votos en tabla de escaños
'''
import csv
from matplotlib import pylab as plt
import seaborn as sns


# EJERCICIO 1:
def lee_escrutinio(fichero):
    ''' Lee un fichero de escrutinio y devuelve una lista de tuplas
    
    Los ficheros de entrada tendrán este formato:
        Provincia,Partido,Votos
        Barcelona,JxSí,1.107.398
        Barcelona,C's,579.850
        Barcelona,PSC,420.623
        Barcelona,Cat-Sí-Qs-Pot,311.612
    Se generará como salida una lista de tuplas con los siguientes componentes:
        - Provincia (str)
        - Partido (str)
        - Votos (in)
    '''
    pass


# EJERCICIO 2:
def calcula_provincias(registros):
    ''' Calcula el conjunto de provincias presente en un escrutinio
    
    Toma como entrada una lista de tuplas (provincia, patido, valor) y produce
    como salida un conjunto de provincias.
    '''
    pass


# EJERCICIO 3:
def calcula_partidos(registros):
    ''' Calcula el conjunto de partidos presente en un escrutinio
    
    Toma como entrada una lista de tuplas (provincia, patido, valor) y produce
    como salida un conjunto de partidos.
    '''
    pass


# EJERCICIO 4:
def votos_por_partido(registros):
    ''' Calcula el total de votos para cada partido
    
    Toma como entrada una lista de tuplas (provincia, patido, valor) y produce
    como salida un diccionario en el que las claves son partidos y los valores
    la suma del partido en todas las provincias en las que ha obtenido votos.
    '''
    pass


# EJERCICIO 5:
def genera_diagrama_tarta(diccionario, limite=None):
    ''' Genera un diagrama de tarta a partir de un diccionario de valores
    
    Toma un diccionario y un numero máximo de elementos a mostrar (limite).
    Genera un diagrama de tarta con una 'porción' para cada clave del
    diccionario (sin superar el limite). El valor asociado a cada clave
    determinará el área de la correspondiente porción. En caso de existir más
    claves en el diccionario que el limite establecido, se mostrarán aquellas
    con los valores más altos.
    
    Se dispondrá de la siguiente paleta de colores:
        paleta = ['blue', 'red', 'green', 'yellow', 'olive', 
                  'orange', 'cyan', 'pink', 'grey']
    
    Se usarán las siguientes instrucciones matplotlib para generar el diagrama
    de tarta:
        plt.pie(valores, labels=claves, colors=colores, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()
    
    Las tres listas necesarias, se calcularán de la siguiente forma:
        - claves: claves del diccionario ordenadas de mayor a menor según el
          valor asociado. Si limite no es None solo se incluirá el número
          especificado de claves.
        - valores: valores asociados a las claves (en el mismo orden).
        - colores: lista de colores usados para cada clave. Si hay más claves
          que colores en la paleta, se asignarán colores repetidos según un criterio
          circular (empezando de nuevo por el primer color de la paleta).
    '''
    pass


# EJERCICIO 6:
def calcula_tabla_votos(registros):
    ''' Calcula una tabla bidimensional a partir de una lista de registros
    
    Toma como entrada una lista de tuplas (provincia, patido, valor), el valor
    podrá ser el dato original en votos o el dato calculado escaño.    
    Se produce como salida un diccionario de dos dimensiones con dos claves:
        - Provincia (str)
        - Partido (str)
    Y un valor:
        - Votos (in)
    Los diccionarios de dos dimensiones en Python son simplente diccionarios
    de una dimensión cuyos valores son, a su vez, diccionarios. En nuestro caso
    serán:
        - Diccionarios con provincias como clave, cuyos valores son ...
        - ... diccionarios con partidos como clave
    '''
    pass


# EJERCICIO 7:
def genera_mapa_calor(tabla, provincias=None, partidos=None, fmt='d'):
    ''' Genera un mapa de calor a partir de una tabla de valores
    
    El mapa de calor es un gráfico pensado especialmente para visualizar
    datos organizados en tablas de dos dimensiones. Consiste en una
    cuadrícula en la que cada eje se asocia a una dimensión de la tabla
    (en nuestro caso las dos dimensiones son provincias y partidos). Cada
    celda de la cuadrícula se rellenará de un color en función del valor de
    la tabla (en nuestro ejemplo los valores podrán ser votos, porcentajes
    o escaños según las tablas).
    
    La función toma como entrada una tabla de valores, una lista de provincias
    que se mostrarán en el eje Y, y una lista de partidos que se mostrarán en
    el eje X. Si la lista de provincias es None se mostrarán todas. Lo mismo
    pasará con la lista de partidos. El parámetro fmt indica el formato en el
    que se mostrarán los números en las celdas del mapa de calor: 'd' para 
    decimales y 'f' para reales.
    
    Utilizaremos el paquete seaborn para generar la gráfico. seaborn es un
    wrapper sobre matplotlib, menos potente pero mucho más fácil de usar. Las
    instrucciones 'seaborn' que tendremos que ejecutar son:
    
        sns.heatmap(vectores, annot=True, fmt=fmt, cmap="PuBu",
                xticklabels=partidos, yticklabels=provincias)
        plt.show()
        
    Donde 'datos' es una lista de vectores (uno por cada provincia). El vector
    de cada provincia será una lista con los valores de la tabla para esa
    provincia y para cada partido. Los partidos se ordenarán siempre de la misma
    forma para los vectores de todas las provincias.
    '''
    pass


# EJERCICIO 8:
def calcula_tabla_porcentajes(tabla):
    ''' Convierte una tabla de votos en porcentajes
    
    Toma como entrada una tabla de dos dimensiones con el número de votos por
    provincia y partido.
    Produce como salida una tabla de porcentajes sobre las mismas dimensiones.
    
    Se calculan los porcentajes dividiendo el voto de cada partido por el total
    de los votos de la provincia. 
    '''
    pass


# EJERCICIO 9:
def calcula_diputados(votos_partidos, total_diputados, exclusion=0.03):
    ''' Calcula los escaños correspondientes a cada partido
    
    Toma como entrada un diccionario con el número de votos por cada partido,
    el número de escaños a repartir entre estos partidos y un porcentaje
    de exclusión. Solo se tendrán en cuenta en el reparto de escaños aquellos
    partidos que superen el porcentaje de exclusión. En la legislación
    española ese porcentaje es el 3%, por esta razón se establece 0.03 como
    valor por defecto de este parámetro. 
    Produce como salida un diccionario con el número de escaños asignado a cada
    partido según el sistema D'Hont.
    
    El método D'Hont se basa en el cálculo de cocientes sucesivos para cada
    partido. En cada momento el cociente para un partido se obtiene con la
    siguiente fórmula:
         cociente = votos / (diputados asignados + 1)
         
    El sistema se basa en la asignación por rondas. En cada ronda (iteración)
    se asigna un diputado al partido que en ese momento tiene el mayor
    cociente, y se actualiza el cociente para dicho partido. Se puede encontrar
    una descripción más detallada, y también ejemplos, en el siguiente artículo
    de Wikipedia:
        https://es.wikipedia.org/wiki/Sistema_d%27Hondt

    Seguiremos el siguiente procedimiento:
    1) Calcular un diccionaio 'resultado' con los partidos como clave y con
       0 diputados asignados a cada uno
    2) Calcular la lista de 'partidos' que superan el porcentaje de exclusión
    3) Calcular la lista de 'votos' (alineada con la anterior) de cada partido
    3) Calcular la lista inicial de 'cocientes', que será una copia de la lista
       de votos
    4) Para cada ronda:
        - determimar el índice del partido ganador de la ronda
        - incrementar el número de votos de dicho partido
        - calcular el nuevo cociente de dicho partido
    5) Construir un diccionario con los diputados asignados a los partidos
    6) Actualizar el diccionario 'resultado' con el diccionario anterior
    '''
    pass


# EJERCICIO 10:
def calcula_tabla_diputados(tabla_votos, distribucion, exclusion=0.03):
    ''' Convierte una tabla de votos en tabla de escaños
    
    Toma como entrada una tabla de dos dimensiones con el número de votos por
    provincia y partido, y también recibe como entrada un diccionario con el
    número de diputados por cada provincia. Recibe también un porcentaje de
    exclusión que se establece por defecto en el 3%.
    Produce como salida una tabla de dos dimensiones con el número de diputados
    por provincia y partido.
    
    Los valores de la tabla se calculan usando la función calcula_diputados.
    '''
    pass
    

################################################################
#  Funciones de test
################################################################
def test_calcula_provincias(registros):
    provincias = calcula_provincias(registros)
    print('PROVINCIAS:')
    for p in provincias:
        print('  -', p)
    

def test_calcula_partidos(registros):
    partidos = calcula_partidos(registros)
    print('PARTIDOS:')
    for p in partidos:
        print('  -', p)


def test_votos_por_partido(registros):
    print('VOTOS POR PARTIDO', votos_por_partido(registros))


def test_genera_diagrama_tarta(registros):
    votos = votos_por_partido(registros)
    genera_diagrama_tarta(votos, limite=7)

  
def test_calcula_tabla(registros):
    tabla_votos = calcula_tabla_votos(registros)
    print('TABLA DE VOTOS:')
    for provincia in tabla_votos:
        print(provincia, '->', tabla_votos[provincia])


def test_genera_mapa_color(registros):
    tabla_votos = calcula_tabla_votos(registros)
    partidos = ['JxC', 'ERC', "C's", 'PSC', 'CUP', 'PP', 'CEC'] 
    genera_mapa_calor(tabla_votos, partidos=partidos)


def test_calcula_tabla_porcentajes(registros):
    tabla_votos = calcula_tabla_votos(registros)
    tabla_porcentajes = calcula_tabla_porcentajes(tabla_votos)
    partidos = ['JxC', 'ERC', "C's", 'PSC', 'CUP', 'PP', 'CEC']
    genera_mapa_calor(tabla_porcentajes, partidos=partidos, fmt='f')
    

def test_calcula_diputados(registros):
    # Ejemplo con datos sintéticos
    votos = {'Partido A': 340000,
             'Partido B': 280000,
             'Partido C': 160000,
             'Partido D': 60000,
             'Partido E': 15000}
    diputados = calcula_diputados(votos, 7)
    print("DIPUTADOS:", diputados)
    
    # Ejemplo con datos reales
    votos_provincias = calcula_tabla_votos(registros)
    votos = votos_provincias['Barcelona']
    diputados = calcula_diputados(votos, 85)
    print("DIPUTADOS:", diputados)
    

def test_calcula_tabla_diputados(registros):
    # Ejemplo por provincias
    tabla_votos = calcula_tabla_votos(registros)
    distribucion = {'Barcelona': 85,
                    'Girona': 17,
                    'Lleida': 15,
                    'Tarragona': 18
                    }
    tabla_diputados = calcula_tabla_diputados(tabla_votos, distribucion)
    partidos = ['JxC', 'ERC', "C's", 'PSC', 'CUP', 'PP', 'CEC']
    genera_mapa_calor(tabla_diputados, partidos=partidos)
    
    # Simulación de circunscripción única
    tabla_votos = {'ÚNICA': votos_por_partido(registros)}
    distribucion = {'ÚNICA': 135}
    tabla_diputados = calcula_tabla_diputados(tabla_votos, distribucion)
    partidos = ['JxC', 'ERC', "C's", 'PSC', 'CUP', 'PP', 'CEC']
    genera_mapa_calor(tabla_diputados, partidos=partidos, provincias=['ÚNICA'])
    
   
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    registros = lee_escrutinio('./csv/cat-2017.csv')
    #registros = lee_escrutinio('./csv/and-2015.csv')
    print("TOTAL DE REGISTROS: ", len(registros)) 
    print(registros[:10], '\n')

    #test_calcula_provincias(registros)
    #test_calcula_partidos(registros)
    #test_votos_por_partido(registros)
    #test_genera_diagrama_tarta(registros)
    #test_calcula_tabla(registros)
    #test_genera_mapa_color(registros)
    #test_calcula_tabla_porcentajes(registros)
    #test_calcula_diputados(registros)
    #test_calcula_tabla_diputados(registros)