# -*- coding: utf-8 -*-
''' Tratamiento de imágenes

AUTOR: José A. Troyano
REVISOR: Mariano González 
ÚLTIMA MODIFICACIÓN: 22/01/2018

En este proyecto trabajaremos con matrices (listas de listas) para implementar
una serie de funciones de procesamiento de imágenes, como la rotación, el reflejo
o diferentes manipulaciones del color.

REPRESENTACIÓN DE IMÁGENES:
---------------------------
Las imágenes son matrices de píxeles, y habitualmente cada píxel se representa
por tres números que indican el nivel de color de tres colores primarios. A
este modelo se le denomina RGB por las siglas de Red, Green y Blue. En el
formato JPEG, por ejemplo, estos valores de intensidad de color se encuentran
entre 0 y 255.

Representaremos las imágenes usando tipos básicos de Python, mediante listas de
listas de listas de números. Si lo estructuramos se comprende mejor el papel
que juega cada lista:

    lista de filas, donde cada fila es:
        una lista de píxeles, donde cada píxel es:
            una lista de tres números con los valores RGB

Llamaremos a esta estructura "Matriz de píxeles RGB". He aquí una matriz de
píxeles de 3x3 extraida de una imagen real en formato JPEG:

    imagen_3_3 = [ [[150, 185, 241], [150, 185, 241], [150, 185, 241]],
                   [[152, 187, 243], [152, 187, 243], [152, 187, 243]],
                   [[153, 188, 244], [153, 188, 244], [152, 187, 243]] ]

Para leer, guardar y mostrar imágenes nos apoyaremos en las funciones que
proporciona matplotlib. Matplotlib usa arrays numpy para representar las
imágenes y nosotros transformaremos esos arrays numpy en nuestras "matrices de
píxeles RGB". Damos este "paso atrás" por una cuestión didáctica: centrar el
ejercicio en la manipulación de matrices representadas con tipos básicos de
Python (listas de listas) sin tener que aprender a usar la librería numpy.
Las tres funciones que realizan estas tareas se proporcionan ya implementadas
y son:

- lee_imagen(fichero):
    lee una imagen de un fichero
- muestra_imagen(imagen, cmap)
    muestra una matriz de píxeles
- guarda_imagen(imagen, fichero, format, cmap):
    guarda una matriz de píxeles en un fichero


FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- calcula_dimensiones(imagen):
    calcula el número de filas y columnas de una imagen
- calcula_intensidades_medias(imagen):
    calcula la intensidad media de cada uno de los tres colores primarios
- reflejo_vertical(imagen):
    calcula el reflejo vertical de una imagen
- reflejo_horizontal(imagen):
    calcula el reflejo horizontal de una imagen
- rotacion(imagen):
    calcula la rotación una imagen
- filtro_color(imagen, colores):
    mantiene solo los colores primarios indicados en el conjunto 'colores'
- escala_grises(imagen):
    transforma una imagen en color a grados de grises
- blanco_negro(imagen, umbral):
    transforma una imagen en color a blanco y negro
'''

from matplotlib import pylab as plt
import numpy as np

def lee_imagen(fichero):
    ''' Lee una imagen de un fichero
    
    Toma como entrada el nombre del fichero. Produce como salida una matriz de
    píxeles RGB. Se apoya en la función imread que detecta automáticamente el
    formato del fichero de imagen.
    '''
    imagen = plt.imread(fichero)
    imagen = imagen.tolist()
    return (imagen)


def muestra_imagen(imagen, cmap=None):
    ''' Muestra una matriz de píxeles
    
    Toma como entrada una matriz de píxeles y el parámetro 'cmap' que indica
    el mapa de color que se aplicará en la visualización. La función admite dos
    tipos de imágenes:
        - Matriz de píxeles RGB: el parámetro 'cmap' se ignora
        - Matriz de píxeles de escala de grises: cada pixel se representa por un
          único valor. El parámetro 'cmap' debe ser 'gray'
    '''
    imagen = np.array(imagen, dtype='uint8')
    plt.imshow(imagen, cmap=cmap)
    plt.show()


def guarda_imagen(fichero, imagen, format='jpeg', cmap=None):
    ''' Guarda una matriz de píexeles RGB en un fichero
    
    Toma como entrada el nombre del fichero, una matriz de píxeles, el
    parámetro format (por defecto 'jpeg') y el parámetro 'cmap' que indica
    el mapa de color que se aplicará. Se apoya en la función imsave. La función
    admite dos tipos de imágenes:
        - Matriz de píxeles RGB: el parámetro 'cmap' se ignora
        - Matriz de píxeles de escala de grises: cada pixel se representa por un
          único valor. El parámetro 'cmap' debe ser 'gray'
    '''
    imagen = np.array(imagen, dtype='uint8')
    plt.imsave(fichero, imagen, format=format, cmap=cmap)
    plt.show()


# EJERCICIO 1:
def calcula_dimensiones(imagen):
    ''' Calcula el número de filas y columnas de una imagen
    
    Toma como entrada una matriz de píxeles RGB. Produce como salida una tupla
    (filas, columnas) con el número de filas y el número de píxeles por cada
    fila.
    '''
    pass


# EJERCICIO 2:
def calcula_intensidades_medias(imagen):
    ''' Calcula la intensidad media de cada uno de los tres colores primarios
    
    Toma como entrada una matriz de píxeles RGB. Produce como salida una tupla
    (rojo, verde, azul) con las medias de los valores encontrados para cada
    uno de los colores primarios.
    '''
    pass


# EJERCICIO 3:
def reflejo_vertical(imagen):
    ''' Calcula el reflejo vertical de una imagen
    
    Toma como entrada una matriz de píxeles RGB. Produce como salida otra
    imagen que es el reflejo vertical de la que se recibe. 
    
    El reflejo vertical se consigue invirtiendo las filas de píxeles.
    '''
    pass


# EJERCICIO 4:
def reflejo_horizontal(imagen):
    ''' Calcula el reflejo horizontal de una imagen
    
    Toma como entrada una matriz de píxeles RGB. Produce como salida otra
    imagen que es el reflejo horizontal de la que se recibe.
    
    El reflejo horizontal se consigue invirtiendo las columnas de píxeles.
    Esta función es un poco más compleja que la anterior porque la imagen
    no está representada en base a columnas.
    '''
    pass


# EJERCICIO 5:
def rotacion(imagen):
    ''' Calcula la rotación una imagen
    
    Toma como entrada una matriz de píxeles RGB. Produce como salida otra
    imagen que está rotada 90º a la derecha.
    
    El giro de 90º a la derecha se consigue mediante la trasposición (cambiar
    filas por columnas) y posteriormente el reflejo vertical.
    '''
    pass


# EJERCICIO 6:
def filtro_color(imagen, colores):
    ''' Mantiene solo los colores primarios indicados en el conjunto 'colores'
    
    Toma como entrada una matriz de píxeles RGB, y un conjunto de colores. Los
    tres colores primarios se representan con las letras 'R', 'G' y 'B'. De
    esta forma, la siguiente llamada mantendría solo los colores rojo y azul
    de la imagen:
        filtro_color(imagen, {'R', 'B'})
    
    Produce como salida otra imagen en la que se han eliminado los colores
    primarios que no estan presentes en la lista recibida.
    '''
    pass


# EJERCICIO 7:
def escala_grises(imagen):
    ''' Transforma una imagen en color a grados de grises
    
    Toma como entrada una matriz de píxeles RGB, y produce como salida una
    matriz de píxeles con intensidades en escala de grises (un único valor por
    cada pixel).
    
    Para convertir una imagen en color a escala de grises hay que aplicar
    los siguientes pesos para integrar los tres canales de color en un único
    valor de intensidad:
        - Rojo:  0.2989
        - Verde: 0.5870
        - Azul:  0.1140
    '''
    pass


# EJERCICIO 8:
def blanco_negro(imagen, umbral=128):
    ''' Transforma una imagen en color a blanco y negro
    
    Toma como entrada una matriz de píxeles RGB y un umbral de intensidad para
    determinar la diferencia entre blanco y negro. Produce como salida una
    matriz de píxeles (de un solo valor cada uno) con dos posibles
    intensidades:
        - Blanco: 0
        - Negro: 255
    '''
    pass


################################################################
#  Funciones de test
################################################################
def test_muestra_imagen(imagen):
    muestra_imagen(imagen)


def test_guarda_imagen(imagen):
    guarda_imagen('./img/salida.jpeg', imagen)


def test_calcula_dimensiones(imagen):
    filas, columnas = calcula_dimensiones(imagen)
    print("Las dimensiones de la imagen son:")
    print("    - Filas:", filas) 
    print("    - Columnas:", columnas)


def test_calcula_intensidades_medias(imagen):
    rojo, verde, azul = calcula_intensidades_medias(imagen)
    print("Las intensidades medias de la imagen son:")
    print("    - Rojo:", rojo) 
    print("    - Verde:", verde)
    print("    - Azul:", azul)
    
def test_reflejo_vertical(imagen):
    reflejo = reflejo_vertical(imagen)
    muestra_imagen(reflejo)


def test_reflejo_horizontal(imagen):
    reflejo = reflejo_horizontal(imagen)
    muestra_imagen(reflejo)


def test_rotacion(imagen):
    rotada = rotacion(imagen)
    muestra_imagen(rotada)

 
def test_filtro_color(imagen):
    solo_azul_rojo = filtro_color(imagen, ['B', 'R'])
    muestra_imagen(solo_azul_rojo)


def test_escala_grises(imagen):
    grises = escala_grises(imagen)
    muestra_imagen(grises, cmap='gray')
    guarda_imagen('./img/grises.jpeg', grises, cmap='gray')


def test_blanco_negro(imagen):
    imagen_bn = blanco_negro(imagen)
    muestra_imagen(imagen_bn, cmap='gray')


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    imagen = lee_imagen('./img/gibraltar.jpeg')
    #test_muestra_imagen(imagen)
    #test_guarda_imagen(imagen)
    #test_calcula_dimensiones(imagen)
    #test_calcula_intensidades_medias(imagen)
    #test_reflejo_vertical(imagen)
    #test_reflejo_horizontal(imagen)
    #test_rotacion(imagen)
    #test_filtro_color(imagen)
    #test_escala_grises(imagen)
    test_blanco_negro(imagen)
    