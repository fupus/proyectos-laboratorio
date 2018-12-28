# -*- coding: utf-8 -*-

from minimos_cuadrados import *

################################################################
#  Funciones de test
################################################################
def test_pesos_alturas_por_edades():
    puntos = pesos_alturas_por_edades(REGISTROS, 11, 13.9)
    print(len(puntos), puntos)
    puntos = pesos_alturas_por_edades(REGISTROS, 14, 21)
    print(len(puntos), puntos)


def test_pesos_alturas_por_genero():
    mujeres = pesos_alturas_por_genero(REGISTROS, 'f')
    print(len(mujeres), mujeres)
    hombres = pesos_alturas_por_genero(REGISTROS, 'm')
    print(len(hombres), hombres)


def test_calcula_recta_regresion():
    puntos = pesos_alturas_por_edades(REGISTROS, 11, 21)
    a, b = calcula_recta_regresion(puntos)
    print("Recta: a={}    b={}".format(a, b))


def test_evalua_metrica_MAE():
    menores = pesos_alturas_por_edades(REGISTROS, 9, 13.9)
    jovenes = pesos_alturas_por_edades(REGISTROS, 14, 21)
    a, b = calcula_recta_regresion(menores)
    print("Recta: a={}    b={}".format(a, b))
    print("Error menores: {}".format(evalua_metrica_MAE(menores, a, b)))
    print("Error jovenes: {}".format(evalua_metrica_MAE(jovenes, a, b)))


def test_muestra_recta_y_puntos():
    hombres = pesos_alturas_por_genero(REGISTROS, 'm')
    a, b = calcula_recta_regresion(hombres)
    muestra_recta_y_puntos(a, b, hombres)


################################################################
#  Programa principal
################################################################
REGISTROS = lee_registros('../data/registros.csv')
print("TODOS LOS REGISTROS: ", REGISTROS, '\n')

#test_pesos_alturas_por_edades()
#test_pesos_alturas_por_genero()
#test_calcula_recta_regresion()
#test_evalua_metrica_MAE()
#test_muestra_recta_y_puntos()
