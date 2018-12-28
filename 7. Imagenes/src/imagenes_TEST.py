# -*- coding: utf-8 -*-

from imagenes import *


################################################################
#  Funciones de test
################################################################
def test_muestra_imagen(imagen):
    muestra_imagen(imagen)


def test_guarda_imagen(imagen):
    guarda_imagen('../img/salida.jpeg', imagen)


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
    guarda_imagen('../img/grises.jpeg', grises, cmap='gray')


def test_blanco_negro(imagen):
    imagen_bn = blanco_negro(imagen)
    muestra_imagen(imagen_bn, cmap='gray')


################################################################
#  Programa principal
################################################################

imagen = lee_imagen('../img/gibraltar.jpeg')
#test_muestra_imagen(imagen)
#test_guarda_imagen(imagen)
#test_calcula_dimensiones(imagen)
#test_calcula_intensidades_medias(imagen)
#test_reflejo_vertical(imagen)
#test_reflejo_horizontal(imagen)
#test_rotacion(imagen)
#test_filtro_color(imagen)
#test_escala_grises(imagen)
#test_blanco_negro(imagen)
    