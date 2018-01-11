# -*- coding: utf-8 -*-
''' Clasificador basado en la técnica de los vecinos más cercanos

AUTOR: José A. Troyano
REVISOR: Fermín Cruz
ÚLTIMA MODIFICACIÓN: 03/12/2017

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

El dataset completo se encuentra en el fichero IRIS.csv de la carpeta /datos.
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
    calcula la distancia entre dos vectores
- vecinos_mas_cercanos(registro, dataset, k, distancia):
    devuelve los vecinos más cercanos de un registro (solo atributos)
- votacion(registro, dataset, k, distancia):
    calcula la clase de un registro en función de las de sus vecinos
- ponderacion(registro, dataset, k, distancia):
    calcula la clase de un registro en función de las de sus vecinos

- evalua_clasificador(train, test, k, distancia, estrategia):
    calcula el porcentaje de acierto clasificando un dataset de test
- visualiza_vecinos_iris(registro, vecinos):
    gráfico-2D con la posición de un registro y sus vecinos del dataset IRIS
'''

import csv
import sys
from matplotlib import pylab as plt
from scipy.spatial import distance


# EJERCICIO 1:
def lee_dataset_iris(fichero):
    ''' Lee el fichero de registros y devuelve un dataset

    Usaremos las funciones de la librería estándar de Python para leer ficheros
    en formato CSV.
    El dataset se representará mediante una tupla de dos componentes:
        - atributos: lista de tuplas, una por cada registro del fichero
        - clases: lista alineada con la anterior con la clase de cada registro
    '''
    pass


# EJERCICIO 2:
def calcula_distancia(v1, v2, distancia='euclidean'):
    '''Calcula la distancia entre dos vectores

    Soportaremos distintas funciones de distancias proporcinadas por la
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
def vecinos_mas_cercanos(registro, train, k=3, distancia='euclidean'):
    ''' Devuelve los vecinos más cercanos de un registro (solo atributos)

    Toma como entrada un registro del que se desconoce la clase (solo una
    tupla de atributos), un dataset de train, un número de vecinos esperado
    y una distancia.

    Produce como salida una lista de tuplas, con los k vecinos más cercanos al
    registro y la distancia a la que está cada uno de ellos. Cada tupla tiene
    las tres siguientes informaciones:
        - distancia del vecino al registro
        - atributos del vecino
        - clase del vecino

    El procedimiento a seguir para calcular esta lista de k vecinos con sus
    correspondientes distancias es el siguiente:
        - Cacular todas las posibles tuplas (distancia, atributos, clase)
        - Ordenar la lista anterior por distancia
        - Seleccionar los k primeros elementos de la lista ordenada
    '''
    pass


# EJERCICIO 4:
def votacion(registro, train, k=3, distancia='euclidean'):
    ''' Calcula la clase de un registro en función de las de sus vecinos

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
          clases que hana aparecido al menos una vez en la lista de vecinos.
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
def ponderacion(registro, train, k=3, distancia='euclidean'):
    ''' Calcula la clase de un registro en función de las de sus vecinos

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
    ''' Calcula el porcentaje de acierto clasificando un dataset de test

    Toma como entrada dos datasets, uno de train y otro de test. Usando una
    estrategia de clasificación (votacion o ponderacion) se determnina a qué
    clase pertenece cada uno de los registros del dataset de test.
    Se compara esta predicción con la clase real de cada registro disponible
    en el dataset de test. Produce como resultado el porcentaje de aciertos
    de la predicción.
    Los parámetros de la función significan lo siguiente:
        - train: dataset de entrenamiento. Tupla con dos componentes
          (atributos, clases)
        - test: dataset de tet. Tupla con dos componentes (atributos, clases)
        - k: número de vecinos usados al clasificar (por defecto 3)
        - distancia: nombre de la función usada para determinar la distancia
          (por defecto 'euclidean')
        - estrategia: función usada para calcular la clase a partir de los
          vecinos (por defecto votacion). IMPORTANTE: no es el nombre de una
          función, ni tampoco una llamada a una función, es ¡¡la función!!  
    '''
    pass


# EJERCICIO 7:
def visualiza_vecinos_iris(registro, vecinos):
    ''' Gráfico2D con la posición de un registro y sus vecinos del dataset IRIS

    El dataset IRIS tiene la ventaja de que dos de sus atributos son muy
    informativos, y prácticamente solo con ellos dos se puede realizar muy bien
    esa clasificación. Estos dos atributos son petal_length y petal_width (la
    tercera y cuarta columna de nuestro fichero). Aprovecharemos esta
    característica del dataset IRIS para generar una visualización de 2D
    usando solo estos atributos.
    La función toma como entrada una lista de tuplas correspondientes a k
    vecinos de un determinado registro. Cada tupla tiene las tres siguientes
    informaciones:
        - distancia del vecino al registro
        - atributos del vecino
        - clase del vecino
    Se usará la función scatter de matplotlib para mostrar en un diagrama cuyos
    ejes serán petal_length y petal_width, lo siguiente:
       - El registro con una cruz en negro
       - Los puntos del dataset, usando un color distinto para cada clase

    Para la cruz en negro del registro llamaresmos a scatter así:
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


################################################################
#  Funciones de test
################################################################

def test_calcula_distancia():
    print(calcula_distancia([0, 1, 2], [1, -1, 3]))
    print(calcula_distancia([0, 1, 2], [1, -1, 3], distancia='cityblock'))
    print(calcula_distancia([0, 1, 2], [1, -1, 3], distancia='canberra'))
    print(calcula_distancia([0, 1, 2], [1, -1, 3], distancia='chebyshev'))
    print(calcula_distancia([0, 1, 2], [1, -1, 3], distancia='desconocida'))


def test_vecinos_mas_cercanos(train):
    '''
    Las pruebas se realizarán comparando los registros solo con los primeros
    10 registros del dataset de train:
        5.4,3.4,1.7,0.2,setosa
        5.1,3.7,1.5,0.4,setosa
        4.6,3.6,1,0.2,setosa
        5.1,3.3,1.7,0.5,setosa
        4.8,3.4,1.9,0.2,setosa
        5,3,1.6,0.2,setosa
        5,3.4,1.6,0.4,setosa
        5.2,3.5,1.5,0.2,setosa
        5.2,3.4,1.4,0.2,setosa
        4.7,3.2,1.6,0.2,setosa
    Se usará la distancia por defecto 'euclidean'
    '''
    train = (train[0][:10], train[1][:10])  # Primeros 10 elementos del dataset

    # Igual al primero de los 10 registros, k=3
    registro = (5.4, 3.4, 1.7, 0.2)
    print(vecinos_mas_cercanos(registro, train, k=3))

    # Igual al primero de los 10 registros, k=5
    registro = (5.4, 3.4, 1.7, 0.2)
    print(vecinos_mas_cercanos(registro, train, k=5))

    # Muy parecido al último de los 10 registros, k=3
    registro = (4.75, 3.2, 1.55, 0.2)
    print(vecinos_mas_cercanos(registro, train, k=3))

    # No parecido a ningún registro, k=3
    registro = (5.05, 3.7, 1, 0.8)
    print(vecinos_mas_cercanos(registro, train, k=3))    


def test_votacion(train):
    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 3
    registro = (5.4, 3.7, 1.5, 0.2)
    print(votacion(registro, train, k=3))

    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 5
    registro = (5.4, 3.7, 1.5, 0.2)
    print(votacion(registro, train, k=5))

    # Parecido a ((5.4, 3.7, 1.5, 0.2), setosa), k=3
    registro = (5.6, 3.5, 1.8, 0.5)
    print(votacion(registro, train, k=3))

    # Igual a ((5.0, 2.0, 3.5, 1.0), versicolor), k=3
    registro = (5.0, 2.0, 3.5, 1.0)
    print(votacion(registro, train, k=3))

    # Igual a ((6.5, 3.2, 5.1, 2.0), virginica), k=3
    registro = (6.5, 3.2, 5.1, 2.0)
    print(votacion(registro, train, k=3))

    # Media de los siguientes registros con k=50 (asegura variedad de clases)
    #         ((5.4, 3.7, 1.5, 0.2), setosa)
    #         ((5.0, 2.0, 3.5, 1.0), versicolor)
    #         ((6.5, 3.2, 5.1, 2.0), virginica)
    registro = (5.6, 2.9, 3.3, 1.1)
    print(votacion(registro, train, k=50))


def test_ponderacion(train):
        # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 3
    registro = (5.4, 3.7, 1.5, 0.2)
    print(ponderacion(registro, train, k=3))

    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 5
    registro = (5.4, 3.7, 1.5, 0.2)
    print(ponderacion(registro, train, k=5))

    # Igual a ((5.0, 2.0, 3.5, 1.0), versicolor), k=3
    registro = (5.0, 2.0, 3.5, 1.0)
    print(ponderacion(registro, train, k=3))

    # Igual a ((6.5, 3.2, 5.1, 2.0), virginica), k=3
    registro = (6.5, 3.2, 5.1, 2.0)
    print(ponderacion(registro, train, k=3))

    # Parecido a ((5.4, 3.7, 1.5, 0.2), setosa), k=3
    registro = (5.6, 3.5, 1.8, 0.5)
    print(ponderacion(registro, train, k=3))
    
    # Media de los siguientes registros con k=50 (asegura variedad de clases)
    #         ((5.4, 3.7, 1.5, 0.2), setosa)
    #         ((5.0, 2.0, 3.5, 1.0), versicolor)
    #         ((6.5, 3.2, 5.1, 2.0), virginica)
    registro = (5.6, 2.9, 3.3, 1.1)
    print(ponderacion(registro, train, k=50))


def test_evalua_clasificador(train, test):
    '''
    Todas las configuraciones dan muy buen resultado. Esto ocurre porque el
    dataset IRIS es un conjunto de datos 'fácil'. Es decir, hay mucha
    correlación entre algunos de los atributos de las flores y el el tipo
    de flor.

    En otros datasets más complejos, los cambios en la configuración de los
    experimentos (número de vecinos, distancia, estrategia) sí afectarán
    a los resultados.
    '''
    print(evalua_clasificador(train, test, k=3, distancia='euclidean', estrategia=votacion))
    print(evalua_clasificador(train, test, k=3, distancia='euclidean', estrategia=ponderacion))
    print(evalua_clasificador(train, test, k=10, distancia='chebyshev', estrategia=ponderacion))


def test_visualiza_vecinos_iris(train):
    # Registro rodeado de vecinos de la misma clase
    registro = (5.6, 2.9, 3.3, 1.1)
    visualiza_vecinos_iris(registro, vecinos_mas_cercanos(registro, train, k=10))
    visualiza_vecinos_iris(registro, vecinos_mas_cercanos(registro, train, k=50))

    # Registro cerca de una frontera entre dos clases
    registro = (5.6, 2.9, 4.8, 1.6)
    visualiza_vecinos_iris(registro, vecinos_mas_cercanos(registro, train, k=20))


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    train = lee_dataset_iris('./datos/iris_train.csv')
    print("ATRIBUTOS TRAIN: ", train[0])
    print("CLASES TRAIN: ", train[1])

    test = lee_dataset_iris('./datos/iris_test.csv')
    print("ATRIBUTOS TEST: ", test[0])
    print("CLASES TEST: ", test[1], "\n")


    # test_calcula_distancia()
    # test_vecinos_mas_cercanos(train)
    # test_votacion(train)
    # test_ponderacion(train)
    # test_evalua_clasificador(train, test)
    # test_visualiza_vecinos_iris(train)