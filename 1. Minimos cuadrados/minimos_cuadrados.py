# -*- coding: utf-8 -*-
''' Cálculo de recta de regresión con mínimos cuadrados
Aplicación a registros de (genero, edad, altura, peso)

AUTOR: José A. Troyano
REVISOR: Fermín Cruz
ÚLTIMA MODIFICACIÓN: 08/10/2017

Un ejemplo de solución en lenguaje C:
   http://www.ccas.ru/mmes/educat/lab04k/02/least-squares.c

CÁLCULO DE LA RECTA DE REGRESIÓN POR EL MÉTODO DE MÍNIMOS CUADRADOS:
--------------------------------------------------------------------
Dada una serie de puntos {(x1,y1), (x2,y2),..., (xn,yn)}, se calcula
    sum_x = x1 + x2 + ... + xn
    sum_y = y1 + y2 + ... + yn
    sum_xy = x1*y1 + x2*y2 + ... + xn*yn
    sum_xx = x1*x1 + x2*x2 + ... + xn*xn
A partir de estas sumas, la pendiente (a) y el punto de corte (b)
se calculan así:
    a = (sum_x*sum_y - n*sum_xy) / (sum_x*sum_x - n*sum_xx)
    b = (sum_y - a*sum_x) / n

CÁLCULO DEL ERROR ABSOLUTO MEDIO:
---------------------------------
Dadas:
   - una recta con pendiente 'a' y punto de corte 'b'
   - una serie de puntos {(x1,y1), (x2,y2), ..., (xn,yn)}
Se calcula la serie de predicciones {py1, py2, ..., pyn} aplicando la
ecuación de la recta:
     py = a*x + b
Posteriormente se calcula MAE a través de la media de la serie
{|y1-py1|, |y2-py2|, ..., |yn-pyn|} de los valores absolutos de los
errores cometidos en la prediccíón


FORMATO DE ENTRADA:
-------------------
Cada registro del fichero de entrada ocupa una línea y contiene cuatro
datos (genero, edad, altura, peso). Un fragmento de entrada es:
    f,11.9,143.0,38.6
    f,12.9,158.2,47.6
    f,12.8,160.8,49.0
    f,13.4,149.9,41.7
    f,15.9,158.8,51.0
    f,14.3,158.8,50.8

FUNCIONES DISPONIBLES:
----------------------
- lee_registros(fichero):
    lee el fichero de registros y devuelve una lista de tuplas
- pesos_alturas_por_edades(registros, edad_min, edad_max):
    calcula una serie de puntos (peso,altura) según edades
- pesos_alturas_por_genero(registros, genero):
    calcula una serie de puntos (peso,altura) según género
- calcula_recta_regresion(puntos):
    Calcula la recta de regresión a partir de una serie de puntos
- evalua_metrica_MAE(puntos, a, b):
    Calcula el error relativo medio de y=ax+b sobre una serie de puntos
- muestra_recta_y_puntos(a, b, puntos):
    Genera un gráfico con la nube de puntos y la recta y=ax+b
'''

import csv
from matplotlib import pylab as plt


# EJERCICIO 1:
def lee_registros(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas '''
    pass


# EJERCICIO 2:
def pesos_alturas_por_edades(registros, edad_min, edad_max):
    ''' Serie de puntos (peso,altura) según edades

    Devuelve una lista de tuplas (peso, altura) a partir de los registros
    cuya edad esté comprendida entre edad_min y edad_max.
    '''
    pass


# EJERCICIO 3:
def pesos_alturas_por_genero(registros, genero):
    ''' Serie de puntos (peso,altura) según género

    Devuelve una lista de tuplas (peso, altura) a partir de los registros
    cuyo género sea el mismo que el recibido como parámetro.
    '''
    pass


# EJERCICIO 4:
def calcula_recta_regresion(puntos):
    '''  Calcula la recta de regresión a partir de una serie de puntos

    Devuelve la pendiente (a) y el punto de corte con el eje vertical (b)
    '''
    pass


# EJERCICIO 5:
def evalua_metrica_MAE(puntos, a, b):
    ''' Calcula el error relativo medio de y=ax+b sobre una serie de puntos'''
    pass


# EJERCICIO 6:
def muestra_recta_y_puntos(a, b, puntos):
    ''' Genera un gráfico con la nube de puntos y la recta y=ax+b

    Usa la función scatter de la librería matplotlib para mostrar la nube de
    puntos y la función plot para trazar la recta de regresión. Con las
    siguientes tres instrucciones se representarán los puntos en color negro
    y la recta en azul:
        plt.scatter(xs, ys, color='black')
        plt.plot((x_min,x_max), (y_min, y_max), '-', color='blue')
        plt.show()
    Las listas xs e ys contendrán los valores correspondientes a los ejes X e Y
    de los puntos recibidos como parámetros. Por su parte (x_min, y_min) y
    (x_max, y_max) marcarán los extremos de la recta. Se añadirá un 10% del
    rango [x_min, x_max] a ambos extremos de la recta para que el trazado de la
    misma sobresalga visiblemente de la nube de puntos.
    '''
    pass


################################################################
#  Funciones de test
################################################################
def test_pesos_alturas_por_edades(registros):
    puntos = pesos_alturas_por_edades(registros, 11, 13.9)
    print(len(puntos), puntos)
    puntos = pesos_alturas_por_edades(registros, 14, 21)
    print(len(puntos), puntos)


def test_pesos_alturas_por_genero(registros):
    mujeres = pesos_alturas_por_genero(registros, 'f')
    print(len(mujeres), mujeres)
    hombres = pesos_alturas_por_genero(registros, 'm')
    print(len(hombres), hombres)


def test_calcula_recta_regresion(registros):
    puntos = pesos_alturas_por_edades(registros, 11, 21)
    a, b = calcula_recta_regresion(puntos)
    print("Recta: a={}    b={}".format(a, b))


def test_evalua_metrica_MAE(registros):
    menores = pesos_alturas_por_edades(registros, 9, 13.9)
    jovenes = pesos_alturas_por_edades(registros, 14, 21)
    a, b = calcula_recta_regresion(menores)
    print("Recta: a={}    b={}".format(a, b))
    print("Error menores: {}".format(evalua_metrica_MAE(menores, a, b)))
    print("Error jovenes: {}".format(evalua_metrica_MAE(jovenes, a, b)))


def test_muestra_recta_y_puntos(registros):
    hombres = pesos_alturas_por_genero(registros, 'm')
    a, b = calcula_recta_regresion(hombres)
    muestra_recta_y_puntos(a, b, hombres)


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    registros = lee_registros('./datos/registros.csv')
    print("TODOS LOS REGISTROS: ", registros, '\n')

    # test_pesos_alturas_por_edades(registros)
    # test_pesos_alturas_por_genero(registros)
    # test_calcula_recta_regresion(registros)
    # test_evalua_metrica_MAE(registros)
    # test_muestra_recta_y_puntos(registros)
