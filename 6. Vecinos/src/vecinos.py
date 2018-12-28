# -*- coding: utf-8 -*-
''' Clasificador basado en la técnica de los vecinos más cercanos

AUTOR: José A. Troyano
REVISOR: Fermín Cruz
ÚLTIMA MODIFICACIÓN: 22/11/2018

El artículo de Wikipedia sobre 'Vecinos más cercanos':
   https://es.wikipedia.org/wiki/K_vecinos_m%C3%A1s_pr%C3%B3ximos

La técnica de vecinos más cercanos es uno de los métodos de minería de datos
más simple que se puede imaginar. Con este método, se puede predecir
información (que no disponemos) asociada a un determinado registro de datos
simplemente mediante las informaciones (que sí tenemos) de los registros de
datos que más se parezcan a él.

La técnica de vecinos es un método general que se puede aplicar a cualquier
conjunto de datos. En este ejercicio trabajaremos sobre el dataset IRIS. Este
dataset (https://es.wikipedia.org/wiki/Iris_flor_conjunto_de_datos) contiene
150 registros de medidas de flores (lirios) y para cada uno de estos registros
se proporciona la información adicional de la especie a la que pertenece. Hay
tres especies distintas: setosa, versicolor y virginica. Los datos de entrada
estarán en formato CSV, estas son las primeras líneas del fichero de entrada:
        sepal_length,sepal_width,petal_length,petal_width,species
        5.1,3.5,1.4,0.2,setosa
        4.9,3,1.4,0.2,setosa
        4.7,3.2,1.3,0.2,setosa
        4.6,3.1,1.5,0.2,setosa

El dataset completo se encuentra en el fichero IRIS.csv de la carpeta /data.
Además, hay dos ficheros IRIS_test.csv e IRIS_train.csv que conetienen los
mismos registros que IRIS.csv distribuidos en dos grupos de 60 y 90 registros,
respectivamente.

Representaremos esta información mediante una tupla con dos componentes: una
lista de atributos (tupla con las cuatro medidas de los lirios) y la lista de
clases correspondientes. Con esta representación, los cuatro registros del
ejemplo anterior darían lugar a la siguiente tupla:

   (
    [(5.1,3.5,1.4,0.2), (4.9,3,1.4,0.2), (4.7,3.2,1.3,0.2), (4.6,3.1,1.5,0.2)],
    ['setosa', 'setosa', 'setosa', 'setosa']
   )

Mediante una técnica de clasificación automática como la de los vecinos más
cercanos, "aprendemos" la relación existente entre la entrada (medidas de las
flores, en el dataset IRIS) y la salida (especie). Una vez aprendida esta
relación, podremos usar ese conocimiento para poder determinar la salida
correspondiente a un registro que no esté "clasificado" previamente.


FUNCIONES DISPONIBLES:
----------------------
- lee_dataset_iris(fichero):
    lee el fichero y devuelve una lista de tuplas y una lista de salidas

- calcula_distancia(v1, V2, distancia='euclidean'):
    calcula la distancia entre dos vectores de atributos
- vecinos_mas_cercanos(registro, dataset, k, distancia):
    devuelve los vecinos más cercanos a un vector de atributos
- votacion(registro, dataset, k, distancia):
    calcula la clase de un vector de atributos en función de las de sus vecinos
- ponderacion(registro, dataset, k, distancia):
    calcula la clase de un vector de atributos mediante votación ponderada

- evalua_clasificador(train, test, k, distancia, estrategia):
    calcula el porcentaje de aciertos clasificando un dataset de test
- visualiza_vecinos_iris(registro, vecinos):
    gráfico-2D con la posición de un vector de atributos y sus vecinos del dataset IRIS
'''

import csv
from collections import namedtuple
import sys
from matplotlib import pylab as plt
from scipy.spatial import distance


# EJERCICIO 1:
Dataset = namedtuple('Dataset', 'atributos clases')

def lee_dataset_iris(fichero):
    ''' Lee el fichero de registros y devuelve un dataset
    
    ENTRADA: 
       - fichero: nombre del fichero donde se encuentran los registros -> str
    SALIDA: 
       - dataset con listas de vectores de atributos y clases -> Dataset([[float]],[str])
           
    Las listas de vectores de atributos, y de clases deben estar alineadas.
    '''
    pass


# EJERCICIO 2:
def calcula_distancia(v1, v2, distancia='euclidean'):
    '''Calcula la distancia entre dos vectores de atributos
    
    ENTRADA: 
       - v1: vector de atributos -> [float]
       - v2: vector de atributos -> [float]
       - distancia: tipo de distancia a calcular -> str
    SALIDA: 
       - distancia entre los vectores -> str

    Soportaremos distintas funciones de distancias proporcionadas por la
    librería Scipy, que es el estándar de facto en Python para dar soporte
    al cálculo científico. Scipy está incluida en la distribución de Anaconda.
    Las funciones que contemplaremos están incluidas en el módulo 'distance'
    de Scipy. Son las siguientes:

        cityblock (manhattan):     sum(|x - y|
        canberra:                  sum(|x - y| / (|x| + |y|))
        euclidean:                 sqrt(sum((x - y)^2))
        chebyshev:                 max(|x - y|

    Importaremos el módulo 'distance' con la siguiente instrucción:
        from scipy.spatial import distance

    Podremos llamar a todas las funciones, simplemente anteponiendo la
    palabra 'distance' al nombre de la función. Por ejemplo:
        distance.euclidean(v1, v2)

    La función recibe como entrada dos vectores y el nombre de la distancia a
    aplicar (que debe corresponderse con el nombre de alguna de las funciones
    disponibles).
    Produce como salida la distancia entre los dos vectores calculada con la
    función indicada. En caso de que la función solicitada no exista se
    devolverá el valor numérico más grande que se pueda representar. En Python
    accedemos a ese valor con la siguiente variable del módulo sys:
        sys.maxsize

    '''
    pass


# EJERCICIO 3:
def vecinos_mas_cercanos(atributos, train, k=3, distancia='euclidean'):
    ''' Devuelve los vecinos más cercanos de un vector de atributos

    ENTRADA: 
       - atributos: vector de atributos -> [float]
       - train: dataset en el que buscar vecinos -> Dataset([[float]],[str]) 
       - k: número de vecinos a buscar -> int
       - distancia: tipo de distancia a calcular -> str
    SALIDA: 
       - distancias, atributos y clases de los vecinos -> [(float, [float], str)]
    
    El procedimiento a seguir para calcular esta lista de k vecinos con sus
    correspondientes distancias es el siguiente:
        - Cacular todas las posibles tuplas (distancia, atributos, clase)
        - Ordenar la lista anterior por distancia
        - Seleccionar los k primeros elementos de la lista ordenada
    '''
    pass


# EJERCICIO 4:
def votacion(atributos, train, k=3, distancia='euclidean'):
    ''' Calcula la clase de un vector de atributos en función de las de sus vecinos
    
    ENTRADA: 
       - atributos: vector de atributos -> [float]
       - train: dataset en el que buscar vecinos -> Dataset([[float]],[str]) 
       - k: número de vecinos a buscar -> int
       - distancia: tipo de distancia a calcular -> str
    SALIDA: 
       - clase resultado de la predicción -> str

    Usa la función vecinos_mas_cercanos para seleccionar los vecinos
    más cercanos del dataset de train a un determinado registro. Posteriormente
    calcula la predicción de la clase que le corresponde al registro en función
    de la clase mayoritaria de los vecinos. Para ello se calculará la clase con
    mayor número de representantes entre los vecinos. Si hay empate entre
    varias clases, estas se ordenarán alfabéticamente por el nombre y se 
    devolverá la primera de ellas.
    
    El procedimiento será el siguiente:
        - Obtener los k vecinos con la función vecinos_mas_cercanos
        - Calcular una lista con las clases de cada vecino. Llamaremos a esa
          lista 'votos'. Calcularemos tambien el conjunto 'clases' con aquellas
          clases que han aparecido al menos una vez en la lista de vecinos.
        - Calcular el número de votos por cada clase. El resultado será una
          lista de tuplas (frecuencia, clase) ordenada de mayor a menor
          frecuencia
        - Calcular las siguientes informaciones:
             * Frecuencia máxima de la lista de frecuencias
             * Lista de clases que alcanzan la frecuencia máxima
             * Primera clase (de la lista anterior) por orden alfabético
    '''
    pass
    

# EJERCICIO 5:
def ponderacion(atributos, train, k=3, distancia='euclidean'):
    ''' Calcula la clase de un vector de atributos mediante votación ponderada
    
    ENTRADA: 
       - atributos: vector de atributos -> [float]
       - train: dataset en el que buscar vecinos -> Dataset([[float]],[str]) 
       - k: número de vecinos a buscar -> int
       - distancia: tipo de distancia a calcular -> str
    SALIDA: 
       - clase resultado de la predicción -> str
    
    Usa la función vecinos_mas_cercanos para seleccionar los vecinos
    más cercanos del dataset de train a un determinado registro. Posteriormente
    calcula la predicción de la clase que le corresponde al registro en función
    de la clase y la distancia de cada vecino. Para ello se convertirán las
    distancias en similitudes (mayor cuanto más parecidos) y se sumarán las
    similitudes de todos los vecinos de una misma clase. De esta forma, cada
    vecino "vota de forma ponderada" pesando más el voto de los vecinos más
    similares (los más cercanos). Si hay empate entre varias clases (muchísimo
    menos probable que en la votación simple de la función anterior), estas se
    ordenarán  alfabéticamente por el nombre y se devolverá la primera de
    ellas.
    
    El procedimiento será el siguiente:
        - Obtener los k vecinos con la función vecinos_mas_cercanos
        - Calcular una lista llamada similitudes con una tupla (similitud, clase)
          para cada vecino. La similitud se calculará con la siguiente fórmula:
               similitud = distancia_maxima - distancia
        - Calcular, para cada clase de los vecinos, la suma de similitudes. 
          Guardaremos esta información en una lista llamada suma_similitudes
          con una tupla (suma, clase) por cada clase. Esta lista estará
          ordenada por la suma, lo que permitirá identificar fácilmente el
          valor máximo.
        - Calcular las siguientes informaciones:
             * Suma máxima de la lista de sumas
             * Lista de clases que alcanzan la suma máxima
             * Primera clase (de la lista anterior) por orden alfabético
    '''
    pass


# EJERCICIO 6:
def evalua_clasificador(train, test, k=3, distancia='euclidean', estrategia=votacion):
    ''' Calcula el porcentaje de aciertos clasificando un dataset de test
    
    ENTRADA: 
       - train: dataset de entrenamiento -> Dataset([[float]],[str])
       - test: dataset de test -> Dataset([[float]],[str])  
       - k: número de vecinos a buscar -> int
       - distancia: tipo de distancia a calcular -> str
       - estrategia: función a utilizar para combinar vecinos -> class-function
    SALIDA: 
       - porcentaje de aciertos sobre el test -> float

    Toma como entrada dos datasets, uno de train y otro de test. Usando una
    estrategia de clasificación (votacion o ponderacion) se determnina a qué
    clase pertenece cada uno de los registros del dataset de test.
    Se compara esta predicción con la clase real de cada registro disponible
    en el dataset de test. Produce como resultado el porcentaje de aciertos
    de la predicción.
    
    IMPORTANTE: la estrategia no es el nombre de una función (str), ni tampoco
    una llamada a una función, es ¡¡la función!!  
    '''
    pass
        

# EJERCICIO 7:
def visualiza_vecinos_iris(atributos, vecinos):
    ''' Gráfico2D con la posición de un vector de atributos y sus vecinos del dataset IRIS
    
    ENTRADA: 
       - atributos: vector de atributos -> [float]
       - vecinos: distancias, atributos y clases de los vecinos -> [(float, [float], str)] 
    SALIDA EN PANTALLA: 
       - diagrama de puntos con el vector de atributos y los vecinos más cercanos

    El dataset IRIS tiene la ventaja de que dos de sus atributos son muy
    informativos, y prácticamente solo con ellos dos se puede realizar muy bien
    esa clasificación. Estos dos atributos son petal_length y petal_width (la
    tercera y cuarta columna de nuestro fichero). Aprovecharemos esta
    característica del dataset IRIS para generar una visualización de 2D
    usando solo estos atributos.

    Se usará la función scatter de matplotlib para mostrar en un diagrama cuyos
    ejes serán petal_length y petal_width, lo siguiente:
       - El registro con una cruz en negro
       - Los puntos del dataset, usando un color distinto para cada clase
    
    Para la cruz en negro del registro llamaremos a scatter así:
        plt.scatter([plength], [pwidth], color='black', marker='x')

    Para cada capa de color habrá que llamar a scatter de la siguiente forma:
        plt.scatter(plengths, pwidths, color=color, marker='o')

    Donde plengths y pwitdhs son listas con las coordenadas de los puntos y el
    parámetro del color deberá variar para cada clase. Solo necesitaremos estos
    tres colores:
        ['red', 'green', 'blue']

    Tras las llamadas a la función scatter, el gráfico se generará con la
    siguiente instrucción final:
        plt.show()
    '''
    pass


# EJERCICIO 8 (ejercicio abierto):
'''
En el proyecto conviven funciones específicas del dataset IRIS con funciones
más genéricas que podrían aplicarse a otros datasets. En concreto, las dos
funciones que dependen de la estructura del dataset IRIS y que, por tanto, solo
sirven para estos datos son:
- lee_dataset_iris
- visualiza_dataset_iris

Este último ejercicio tiene como objeto aprovechar el resto de funciones para
trabajar con otros conjuntos de datos. Es un ejercicio abierto y no hay ninguna
función de test, ni ninguna sugerencia de nombres de función. Esos elementos del
diseño de la solución también forman parte del trabajo a realizar.

En concreto, el ejercicio consiste en:
1) Buscar otros datasets que puedan servirnos de entrada
2) Implementar las funciones específicas de esos datasets para poder realizar
   un análisis similar al que hemos hecho con el dataset IRIS
   
Los requisitos para ese dataset, que van a permitirnos reaprovechar las
funciones que ya hemos implementado son:
- Los atributos deben ser numéricos, como ocurre con los cuatro atributos
  del dataset IRIS (sepal_length,sepal_width,petal_length,petal_width)
- La clase debe ser "no numérica", como ocurre con la clase del dataset IRIS
  que puede tomar solo tres valores ('setosa', 'versicolor', 'virginica')
- El dataset no debe ser muy grande (varios cientos de registros). Siempre
  se puede recortar un dataset grande eliminando registros.

Un buen sitio para buscar dataset es el repositorio de la Universidad de
Carolina-Irvine (UCI):
   http://archive.ics.uci.edu/ml/index.php
'''