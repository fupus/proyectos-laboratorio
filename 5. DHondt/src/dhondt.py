# -*- coding: utf-8 -*-
''' Análisis de resultados electorales

AUTOR: José A. Troyano
REVISOR: Mariano González, Fermín Cruz, José C. Riquelme
ÚLTIMA MODIFICACIÓN: 03/12/2018

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


Además de los datos de escrutinio, también es necesario conocer el número de escaños
asignados a cada provincia. Esta información también se encuentra en un fichero CSV. Estas
son las primeras líneas de uno de estos ficheros:

    Provincia,Escaños
    Almería,12
    Cádiz,15
    Córdoba,12
    Granada,13

A partir de estos datos, generaremos distintos informes y gráficos para poder
analizar los resultados electorales desde distintos puntos de vista. Por
último, implementaremos el sistema D'Hondt que es uno de los más utilizados a la
hora de asignar escaños a los partidos en función de los votos. Gracias a esta
implementación podremos comparar, por ejemplo, el número de escaños que se
obtienen con la asignación por provincias (sistema actual en España) frente a
una asignación mediante circunscripción unica (sumando los votos de todas las
provincias).

Disponemos de dos conjuntos de datos correspondientes a:
   - Elecciones autonómicas de Andalucía (2015)
   - Elecciones autonómicas de Cataluña (2016)
   - Elecciones generales al gobierno de España (2015)
   - Elecciones generales al gobierno de España (2016)
     

FUNCIONES DISPONIBLES:
----------------------
- lee_escrutinio(fichero):
    lee un fichero de votos y un fichero de escaños
- calcula_provincias(votos):
    calcula el conjunto de provincias presentes en un escrutinio
- calcula_partidos(votos):
    calcula el conjunto de partidos presentes en un escrutinio
- calcula_diccionario_provincia(votos, provincia):
    calcula un diccionario con los votos de cada partido en una provincia
- calcula_diccionario_provincias(votos):
    calcula un diccionario-2D a partir de una lista de registros
- totales_por_partido(tabla):
    calcula la suma de valores para cada partido a partir de un diccionario-2D de valores
- genera_diagrama_tarta(diccionario, limite):
    genera un diagrama de tarta a partir de un diccionario de valores
- genera_mapa_calor(tabla_valores, limite_columnas=None, fmt='d')
    genera un mapa de calor a partir de una tabla de valores
- calcula_tabla_porcentajes(tabla_votos):
    convierte una tabla de votos en porcentajes
- calcula_escaños_provincia(votos_partidos, total_escaños, exclusion=0.03):
    calcula los escaños correspondientes a cada partido en una provincia
- calcula_tabla_escaños(tabla_votos, escaños, exclusion=0.03):
    convierte una tabla de votos en tabla de escaños
'''

import csv
from collections import Counter
from matplotlib import pyplot as plt
import seaborn as sns


# EJERCICIO 1:
def lee_escrutinio(fichero_votos, fichero_escaños):
    ''' Lee un fichero de votos y un fichero de escaños
    
    ENTRADA: 
       - fichero_votos: nombre del fichero donde se encuentran los votos -> str
       - fichero_escaños: nombre del fichero donde se encuentran los escaños por provincia -> str 
    SALIDA: 
       - lista de tuplas de votos -> [(str, str, int)]
       - diccionario con los escaños por provincia -> {str:int}
    
    Los ficheros de entrada tienen los siguentes campos:
        - Fichero de votos: Provincia,Partido,Votos
        - Fichero de escaños: Provincia, Escaños
    '''
    pass


# EJERCICIO 2:
def calcula_provincias(votos):
    ''' Calcula el conjunto de provincias presentes en un escrutinio
    
    ENTRADA: 
       - votos: lista de registros de votos -> [(str, str, int)]
    SALIDA: 
       - conjunto de provincias presentes en el escrutinio -> {str}
    '''
    pass


# EJERCICIO 3:
def calcula_partidos(votos):
    ''' Calcula el conjunto de partidos presentes en un escrutinio
    
    ENTRADA: 
       - votos: lista de registros de votos -> [(str, str, int)]
    SALIDA: 
       - conjunto de partidos presentes en el escrutinio -> {str}
    '''
    pass


# EJERCICIO 4:
def calcula_diccionario_provincia(votos, provincia):
    ''' Calcula un diccionario con los votos de cada partido en una provincia
    
    ENTRADA: 
       - votos: lista de tuplas (provincia, patido, valor) -> [(str, str, int)]
       - provincia: de la que se calculará el diccionario -> str
    SALIDA: 
       - diccionario con los votos por partido en la provincia -> {str:int}
    '''
    pass


# EJERCICIO 5:
def calcula_diccionario_provincias(votos):
    ''' Calcula un diccionario-2D a partir de una lista de registros
    
    ENTRADA: 
       - votos: lista de tuplas (provincia, patido, valor) -> [(str, str, int)]
    SALIDA: 
       - diccionario-2D con los votos por provincia y partido -> {str:{str:int}}
    
    Los diccionarios de dos dimensiones en Python son simplemente diccionarios
    de una dimensión cuyos valores son, a su vez, diccionarios. En nuestro caso
    el diccionario de salida tiene la siguiente estructura:
        - clave: provincia -> str
        - valor: diccionario con el valor por partido para la provincia clave -> {str:int}
    '''
    pass


# EJERCICIO 6:
def totales_por_partido(tabla_valores):
    ''' Calcula la suma de valores para cada partido a partir de un diccionario-2D de valores
    
    ENTRADA: 
       - tabla_valores: diccionario-2D con los votos por provincia y partido -> {str:{str:int}}
    SALIDA: 
       - diccionario con la suma de valores por cada partido -> {str:int}
    
    Toma como entrada un diccionario-2D {provincia: {patido, valor}} y produce
    como salida un diccionario en el que las claves son partidos y los valores
    la suma de los valores asociados al partido en todas las provincias.
    
    En este ejercicio hará falta combinar dos diccionarios sumando los valores de las claves
    que aparezcan en ambos. Una forma pitónica de hacer esto es a través de la clase Counter
    que soporta el operador suma:
    
        A = Counter({'a':1, 'b':2, 'c':3})
        B = Counter({'b':3, 'c':4, 'd':5})
        resultado = dict(A+B)
    '''
    pass


# EJERCICIO 7:
def genera_diagrama_tarta(diccionario, limite=None):
    ''' Genera un diagrama de tarta a partir de un diccionario de valores
    
    ENTRADA: 
       - diccionario: diccionario con los valores por cada clave -> {str:int}
       - limite: número máximo de partidos a mostrar en el diagrama -> int
    SALIDA EN PANTALLA: 
       - diagrama de tarta con los votos por partido
    
    El diagrama de tarta tendrá una 'porción' para cada clave del
    diccionario (sin superar el límite). El valor asociado a cada clave
    determinará el área de la correspondiente porción. En caso de existir más
    claves en el diccionario que el límite establecido, se mostrarán aquellas
    con los valores más altos.
    
    Se usarán las siguientes instrucciones matplotlib para generar el diagrama
    de tarta:
        plt.pie(valores, labels=claves, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()   
    
    Las dos listas necesarias para la poder generar el diagrama son:
        - claves: claves del diccionario ordenadas de mayor a menor según el
          valor asociado. Si limite no es None solo se incluirá el número
          especificado de claves.
        - valores: valores asociados en el dicionario a las claves 
          (en el mismo orden que la lista de claves).
    '''
    pass  


# EJERCICIO 8:
def genera_mapa_calor(tabla_valores, limite_columnas=None, fmt='d'):
    ''' Genera un mapa de calor a partir de un diccionario-2D de valores
    
    ENTRADA: 
       - tabla_valores: diccionario-2D con los votos por provincia y partido -> {str:{str:int}}
       - limite_columnas: número máximo de columnas a mostrar -> int
       - fmt: formato de los valores de cada celda (enteros: 'd', reales: 'f') -> str
    SALIDA EN PANTALLA: 
       - mapa de calor con los acumulados por partido en cada provincia:
            * Las filas (provincias) se mostrarán por orden alfabético
            * las columnas (partidos) se mostrarán por orden descendente del acumulado de valores
    
    El mapa de calor es un gráfico pensado especialmente para visualizar
    datos organizados en tablas de dos dimensiones. Consiste en una
    cuadrícula en la que cada eje se asocia a una dimensión de la tabla
    (en nuestro caso las dos dimensiones son provincias y partidos). Cada
    celda de la cuadrícula se rellenará de un color en función del valor de
    la tabla (en nuestro ejemplo los valores podrán ser votos, porcentajes
    o escaños según las tablas).
    
    Utilizaremos el paquete seaborn para generar la gráfica. seaborn es un
    wrapper sobre matplotlib, menos potente pero mucho más fácil de usar. Las
    instrucciones 'seaborn' que tendremos que ejecutar son:
    
        nombres_partidos = [partido[:10] for partido in partidos] # Acortar nombres largos
        g = sns.heatmap(filas, annot=True, fmt=fmt, cmap="PuBu",
                        xticklabels=nombres_partidos, yticklabels=provincias)
        g.set_yticklabels(g.get_yticklabels(), rotation =0)
        g.set_xticklabels(g.get_xticklabels(), rotation =65)
        plt.show()
        
    Donde 'filas' es una lista de vectores, uno por cada provincia:. 
        - El vector de cada provincia será una lista con los valores de la tabla para esa
          provincia y para cada partido.
        - Los partidos se ordenarán siempre de la misma forma para los vectores de todas
          las provincias.
    '''
    pass


# EJERCICIO 9:
def calcula_tabla_porcentajes(tabla_votos):
    ''' Convierte una tabla de votos en porcentajes
    
    ENTRADA: 
       - tabla_votos: diccionario-2D con los votos por provincia y partido -> {str:{str:int}}
    SALIDA: 
       - diccionario-2D con los porcentajes de votos por provincia y partido -> {str:{str:float}}
   
    Se calculan los porcentajes dividiendo el voto de cada partido por el total
    de los votos de la provincia. 
    '''
    pass


# EJERCICIO 10:
def calcula_escaños_provincia(votos_partidos, total_escaños, exclusion=0.03):
    ''' Calcula los escaños correspondientes a cada partido en una provincia
    
    ENTRADA: 
       - votos_partidos: diccionario con los votos para cada  partido -> {str:int}
       - total_escaños: número de escaños a repartir -> int
       - exclusion: porcentaje mínimo de votos para entrar en el reparto de escaños -> float
    SALIDA: 
       - diccionario con el número de escaños por partido -> {str:int}
       
    Solo se tendrán en cuenta en el reparto de escaños aquellos
    partidos que superen el porcentaje de exclusión. En la legislación
    española ese porcentaje es el 3%, por esta razón se establece 0.03 como
    valor por defecto de este parámetro. 
    Produce como salida un diccionario con el número de escaños asignado a cada
    partido según el sistema D'Hondt.
    
    El método D'Hondt se basa en el cálculo de cocientes sucesivos para cada
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
    1) Calcular un diccionario 'diputados' con los partidos como clave y con
       0 diputados asignados a cada uno
    2) Calcular la variable 'umbral' con el número de votos minimo para poder
       recibir escaños 
    3) Calcular un diccionario cocientes con cada partido y el numero de votos. Solo
       consideraremos los partidos que superen el umbral    
    4) Para cada ronda (tantas veces como escaños hay en juego):
        - Buscar el partido ganador (el que tenga el cociente máximo)
        - Incrementamos en uno el número de diputados de ese partido ganador 
          (diccionario 'diputados')
        - Actualizamos el cociente de ese partido (diccionario 'cocientes')
    '''
    pass


# EJERCICIO 11:
def calcula_tabla_escaños(tabla_votos, escaños, exclusion=0.03):
    ''' Convierte una tabla de votos en tabla de escaños
    
    ENTRADA: 
       - tabla_votos: diccionario-2D con los votos por provincia y partido -> {str:{str:int}}
       - escaños: número de escaños a repartir por cada provincia -> {str:int}
       - exclusion: porcentaje mínimo de votos para entrar en el reparto de escaños -> float
    SALIDA: 
       - diccionario-2D con los escaños por provincia y partido -> {str:{str:int}}
           
    Los valores de la tabla se calculan usando la función calcula_escaños_provincia.
    '''
    pass