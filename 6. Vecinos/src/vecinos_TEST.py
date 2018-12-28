# -*- coding: utf-8 -*-

from vecinos_SOLUCION import *

################################################################
#  Funciones de test
################################################################

def test_calcula_distancia():
    print("DISTANCIA 'euclidean':", calcula_distancia([0, 1, 2], [1, -1, 3]))
    print("DISTANCIA 'cityblock':",calcula_distancia([0, 1, 2], [1, -1, 3], distancia='cityblock'))
    print("DISTANCIA 'canberra':",calcula_distancia([0, 1, 2], [1, -1, 3], distancia='canberra'))
    print("DISTANCIA 'chebyshev':",calcula_distancia([0, 1, 2], [1, -1, 3], distancia='chebyshev'))
    print("DISTANCIA 'desconocida':",calcula_distancia([0, 1, 2], [1, -1, 3], distancia='desconocida'))
    print()


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
    train = Dataset(train[0][:10], train[1][:10]) # Primeros 10 elementos del dataset

    # Igual al primero de los 10 registros, k=3
    registro = (5.4, 3.4, 1.7, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', vecinos_mas_cercanos(registro, train, k=3))
    
    # Igual al primero de los 10 registros, k=5
    registro = (5.4, 3.4, 1.7, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', vecinos_mas_cercanos(registro, train, k=5))
    
    # Muy parecido al último de los 10 registros, k=3
    registro = (4.75, 3.2, 1.55, 0.2)
    print('PARECIDO A UN REGISTRO DE LA BD:', vecinos_mas_cercanos(registro, train, k=3))
    
    # No parecido a ningún registro, k=3
    registro = (5.05, 3.7, 1, 0.8)
    print('NO PARECIDO A NINGÚN REGISTRO DE LA BD:', vecinos_mas_cercanos(registro, train, k=3))
    print()    
    
    
def test_votacion(train):
    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 3
    registro = (5.4, 3.7, 1.5, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', votacion(registro, train, k=3))

    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 5
    registro = (5.4, 3.7, 1.5, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', votacion(registro, train, k=5))

    # Igual a ((5.0, 2.0, 3.5, 1.0), versicolor), k=3
    registro = (5.0, 2.0, 3.5, 1.0)
    print('IGUAL A UN REGISTRO DE LA BD:', votacion(registro, train, k=3))
    
    # Igual a ((6.5, 3.2, 5.1, 2.0), virginica), k=3
    registro = (6.5, 3.2, 5.1, 2.0)
    print('IGUAL A UN REGISTRO DE LA BD:', votacion(registro, train, k=3))
    
    # Parecido a ((5.4, 3.7, 1.5, 0.2), setosa), k=3
    registro = (5.6, 3.5, 1.8, 0.5)
    print('PARECIDO A UN REGISTRO DE LA BD:', votacion(registro, train, k=3))

    # Media de los siguientes registros con k=50 (asegura variedad de clases)
    #         ((5.4, 3.7, 1.5, 0.2), setosa)
    #         ((5.0, 2.0, 3.5, 1.0), versicolor)
    #         ((6.5, 3.2, 5.1, 2.0), virginica)
    registro = (5.6, 2.9, 3.3, 1.1)
    print('MEDIA DE TRES REGISTROS DE LA BD:', votacion(registro, train, k=50))
    print()


def test_ponderacion(train):
        # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 3
    registro = (5.4, 3.7, 1.5, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', ponderacion(registro, train, k=3))

    # Igual a ((5.4, 3.7, 1.5, 0.2), setosa), k = 5
    registro = (5.4, 3.7, 1.5, 0.2)
    print('IGUAL A UN REGISTRO DE LA BD:', ponderacion(registro, train, k=5))

    # Igual a ((5.0, 2.0, 3.5, 1.0), versicolor), k=3
    registro = (5.0, 2.0, 3.5, 1.0)
    print('IGUAL A UN REGISTRO DE LA BD:', ponderacion(registro, train, k=3))
    
    # Igual a ((6.5, 3.2, 5.1, 2.0), virginica), k=3
    registro = (6.5, 3.2, 5.1, 2.0)
    print('IGUAL A UN REGISTRO DE LA BD:', ponderacion(registro, train, k=3))
    
    # Parecido a ((5.4, 3.7, 1.5, 0.2), setosa), k=3
    registro = (5.6, 3.5, 1.8, 0.5)
    print('PARECIDO A UN REGISTRO DE LA BD:', ponderacion(registro, train, k=3))
    
    # Media de los siguientes registros con k=50 (asegura variedad de clases)
    #         ((5.4, 3.7, 1.5, 0.2), setosa)
    #         ((5.0, 2.0, 3.5, 1.0), versicolor)
    #         ((6.5, 3.2, 5.1, 2.0), virginica)
    registro = (5.6, 2.9, 3.3, 1.1)
    print('MEDIA DE TRES REGISTROS DE LA BD:', ponderacion(registro, train, k=50))
    print()


def test_evalua_clasificador(train, test):
    '''
    Todas las configuraciones dan muy buen resultado. Esto ocurre porque el
    dataset IRIS es un conjunto de datos 'fácil'. Es decir, hay mucha
    correlación entre algunos de los atributos de las flores y el tipo
    de flor.
    
    En otros datasets más complejos, los cambios en la configuración de los
    experimentos (número de vecinos, distancia, estrategia) sí afectarán
    a los resultados.
    '''
    print("EXPERIMENTO 'euclidean'-'votación':",
          evalua_clasificador(train, test, k=3, distancia='euclidean', estrategia=votacion))
    print("EXPERIMENTO 'euclidean'-'ponderación':",
          evalua_clasificador(train, test, k=3, distancia='euclidean', estrategia=ponderacion))
    print("EXPERIMENTO 'chebyshev'-'ponderación':",
          evalua_clasificador(train, test, k=10, distancia='chebyshev', estrategia=ponderacion))


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
train = lee_dataset_iris('../data/iris_train.csv')
print("ATRIBUTOS TRAIN: ", train[0])
print("CLASES TRAIN: ", train[1])

test = lee_dataset_iris('../data/iris_test.csv')
print("ATRIBUTOS TEST: ", test[0])
print("CLASES TEST: ", test[1], "\n")

#test_calcula_distancia()
#test_vecinos_mas_cercanos(train)
#test_votacion(train)
#test_ponderacion(train)
#test_evalua_clasificador(train, test)
#test_visualiza_vecinos_iris(train)