# -*- coding: utf-8 -*-
''' Análisis de datos climáticos

AUTOR: José A. Troyano
REVISOR: Mariano González, Carlos G. Vallejo
ÚLTIMA MODIFICACIÓN: 05/12/2017

La información meteorológica es una fuente continua de datos que de forma
gratuita es distribuida por distintos servicios (tanto las predicciones como
las medidas reales). En este proyecto vamos a trabajar con datos meteorológicos
históricos. A partir de ellos generaremos distintas funciones de consulta y
visualización que permitirán, entre otras cosas, seleccionar datos de distintos
períodos, mostrar gráficas que resuman las mediciones tomadas en esos períodos,
y determinar la evolución de los patrones climáticos durante distintos
períodos.

Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada
ocupa una línea y contiene cuatro datos correspondientes a la información
meteorológica de un determinado día (fecha, precipitación, temperatura máxima,
temperatura mínima). Estas son las primeras líneas de un fichero de entrada:
    DATE,PRCP,TMAX,TMIN
    1951-01-01,1.0,9.0,-0.8
    1951-01-02,35.4,8.4,4.4
    1951-01-03,0.0,7.0,1.2
    1951-01-04,0.0,7.6,-2.4
    1951-01-05,0.0,10.6,0.0
    1951-01-06,0.0,10.0,-1.4
    1951-01-07,0.0,12.0,0.0
    1951-01-08,0.0,9.0,3.0

FUNCIONES DISPONIBLES:
----------------------
- lee_registros(fichero):
    lee el fichero de registros y devuelve una lista de tuplas
- filtro_por_período(registros, incio, fin):
    selecciona los registros comprendidos entre dos fechas
- medias_por_meses(registros):
    media de precipitaciones y temperaturas por meses
- genera_climograma(precs, t_maxs, t_mins):
    genera un gráfico a partir de los valores para cada mes
- variaciones_mensuales(historicos, valores):
    mide la variación, mes a mes, entre valores de dos períodos
- variaciones_anuales(historicos, valores):
    mide la variación anual entre valores de dos períodos
- evolucion_variaciones_anuales(registros, periodo_base, periodo_estudio):
    muestra la evolución de las variaciones anuales
'''

import csv
from matplotlib import pylab as plt
from datetime import datetime
import pandas as pd
import calendar
import locale

# EJERCICIO 1:
def lee_registros(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas

    Los ficheros de entrada tendrán este formato:
        DATE,PRCP,TMAX,TMIN
        1951-01-01,1.0,9.0,-0.8
        1951-01-02,35.4,8.4,4.4
        1951-01-03,0.0,7.0,1.2
        1951-01-04,0.0,7.6,-2.4
    Se generará como salida una lista ordenada de tuplas con las siguientes
    cuatro informaciones para cada registro:
        - Fecha (objeto date del módulo datetime)
        - Precipitación (float)
        - Temperatura máxima (float)
        - Temperatura mínima (float)
    Habrá que tener en cuenta los siguientes tratamientos:
        - Saltar la linea inicial (cabecera)
        - Convertir las precipitaciones y temperaturas de str a float
        - Convertir la fecha de str a date. Para ello se utilizará la función
          strptime del módulo datetime de la librería estándar de Python. En
          concreto, usaremos la siguiente instrucción para convertir una fecha
          en formato cadena a un objeto del tipo date:
             fecha = datetime.strptime(cadena_fecha, '%Y-%m-%d').date()
    '''
    pass


# EJERCICIO 2:
def filtro_por_periodo(registros, inicio, fin):
    ''' Selecciona los registros comprendidos entre dos fechas

    Toma como entrada una lista de tuplas (fecha, prec, t_max, t_min), y dos
    fechas 'inicio' y 'fin' y produce como salida una lista con los registros
    comprendidos entre las dos fechas, ambas incluidas.

    Las fechas se reciben en formato cadena, por lo que habrá que analizarlas
    con la función datetime:
        fecha = datetime.strptime(cadena_fecha, '%Y-%m-%d').date()
    '''
    pass


# EJERCICIO 3:
def medias_por_meses(registros):
    ''' Media de precipitaciones y temperaturas por meses

    Toma como entrada una lista de tuplas (fecha, prec, t_max, t_min).

    Produce como salida una tupla de tres listas, una para precipitaciones y
    las otras dos para temperatura máxima y mínima. Cada lista contiene 12
    valores con las medias de cada medida para los 12 meses del año.

    Si para un determinado mes no hay registros, se incluirá el valor 0 en
    la posición correspondientes de las listas.
    '''
    pass


# EJERCICIO 4:
def genera_climograma(precs, t_maxs, t_mins):
    ''' Genera un gráfico a partir de los valores para cada mes

    El climograma es una gráfica que integra distintas informaciones sobre
    el clima. Por lo general incluye (por cada mes) las precipitaciones, las
    temperaturas máximas y las mínimas.
    En nuestra versión del climograma, las precipitaciones se muestran con un
    diagrama de barras, y las temperaturas máximas y mínimas con sendas líneas
    (en rojo y azul).
    Se usaran las siguientes instrucciones para generar la gráfica:
        ax = plt.gca()
        ax.set_ylabel("Litros")
        plt.bar(indices, precs, color='aqua')
        plt.xticks(indices, meses, rotation=80, fontsize=10)
        ax2 = ax.twinx()
        plt.plot(t_maxs, color='red')
        plt.plot(t_mins, color='blue')
        ax2.set_ylabel("Grados")
        plt.show()
    Donde meses e indices son dos listas con la siguiente información:
        - meses: nombres de los meses
        - indices: números del 0 al 11
        
    Generaremos la lista de nombres usando las utilidades que nos proporcionan
    los módulos 'calendar' y 'locale' de la librería estándar de Python: 
        locale.setlocale(locale.LC_ALL, '')
        meses = [calendar.month_name[i] for i in range(1, 13)]
    '''
    pass


# EJERCICIO 5:
def variaciones_mensuales(historicos, valores_periodo):
    ''' Mide la variación entre valores de dos períodos

    Toma como entrada dos tuplas, cada una de ellas con tres listas
    (precs, t_maxs, t_mins) con el resumen mensual de dos períodos de tiempo.

    Produce como salida una tupla de tres listas con las variaciones del
    segundo período con respecto al primero (valores históricos). Las tres
    listas de salida tendrán también un valor para cada mes, que se calculará
    restando el correspondiente valor histórico al valor actual.

    Para poder recorrer a la vez las seis listas que vienen distribuidas
    en dos tuplas de tres listas, viene bien construir una nueva lista de
    tuplas de la siguiente forma:
        tuplas = zip(historicos[0], historicos[1], historicos[2],
                     valores[0], valores[1], valores[2])
    '''
    pass


# EJERCICIO 6:
def variaciones_anuales(historicos, valores_periodo):
    ''' Mide la variación anual entre valores de dos períodos

    Toma como entrada dos listas de registros meteorológicos correspondientes,
    a dos períodos de tiempo, en forma de dos listas de tuplas (fecha, prec,
    t_max, t_min).
    Produce como salida tres valores correspondientes a las variaciones anuales
    del segundo período con respecto al primero:
        - var_prec: variación anual media de temperatura
        - var_t_max: variación anual media de la temperatura máxima
        - var_t_min: variación anual media de la temperatura mínima

    Para calcular la variación anual media se seguirá el siguiente
    procedimiento:
        - Calcular las medias por meses de cada período
        - Calcular las variaciones mensuales entre ambos períodos
        - Calcular la media de las variaciones mensuales para cada una de las
          tres medidas (prec, t_max, t_min)
    '''
    pass


# EJERCICIO 7:
def evolucion_variaciones_anuales(registros, periodo_base, periodo_estudio):
    ''' Muestra la evolución de las variaciones anuales

    Toma como entrada una lista de tuplas (fecha, prec, t_max, t_min), un rango
    de años (un objeto range) para el período base y un rango de años para el
    período de estudio (otro objeto range).
    Produce como salida una gráfica con tres curvas con las variaciones anuales
    de prec, t_max y t_min de cada año del período de estudio con respecto al
    período base.
    El procedimiento a seguir es el siguiente:
        - Obtener dos listas de enteros (anyos_base y anyos) a partir de los
          rangos recibidos como parámetro.
        - Obtener las fechas de inicio y fin del período base. Se añadirá el
          sufijo "-01-01" al primer año, y el sufijo "-12-31" al último año.
        - Calcular las listas de variaciones de cada métrica (vars_prec,
          vars_tmax, vars_tmin) para cada año del período de estudio. Se usará
          la función variaciones_anuales a la que se le pasará el período base
          y la lista de registros correspondientes a cada año.
    Una vez calculadas las listas vars_prec, vars_tmax y vars_tmin, la gráfica
    se generará con las siguientes instrucciones:
        vars_prec = pd.Series(vars_prec).rolling(window=10,center=False).mean()
        vars_tmax = pd.Series(vars_tmax).rolling(window=10,center=False).mean()
        vars_tmin = pd.Series(vars_tmin).rolling(window=10,center=False).mean()
        ax = plt.gca()
        ax.set_ylabel("Litros")
        plt.plot(vars_prec, color='aqua', label='Lluvia')
        plt.legend(loc='lower left')
        ax2 = ax.twinx()
        plt.plot(vars_tmax, color='red', label='T. máxima')
        plt.plot(vars_tmin, color='blue', label='T. mínima')
        ax2.set_ylabel("Grados")
        plt.legend(loc='lower right')
        plt.show()
    '''
    pass


################################################################
#  Funciones de test
################################################################
def test_filtro_por_periodo(registros):
    inicio = "2016-01-01"
    fin = "2016-01-31"
    seleccion = filtro_por_periodo(registros, inicio, fin)
    print(len(seleccion), seleccion)


def test_medias_por_meses(registros):
    inicio = "2016-01-01"
    fin = "2016-12-31"
    seleccion = filtro_por_periodo(registros, inicio, fin)
    m_prec, m_tmax, m_tmin = medias_por_meses(seleccion)
    print(m_prec)
    print(m_tmax)
    print(m_tmin)


def test_genera_climograma(registros):
    inicio = "2016-01-01"
    fin = "2016-12-31"
    seleccion = filtro_por_periodo(registros, inicio, fin)
    m_prec, m_tmax, m_tmin = medias_por_meses(seleccion)
    genera_climograma(m_prec, m_tmax, m_tmin)


def test_variaciones_mensuales(registros):
    # Cálculo de valores históricos
    inicio_h = "1951-01-01"
    fin_h = "1989-12-31"
    seleccion_h = filtro_por_periodo(registros, inicio_h, fin_h)
    m_prec_h, m_tmax_h, m_tmin_h = medias_por_meses(seleccion_h)
    historicos = (m_prec_h, m_tmax_h, m_tmin_h)
    # Cálculo de valores del período a evaluar
    inicio = "2005-01-01"
    fin = "2016-12-31"
    seleccion = filtro_por_periodo(registros, inicio, fin)
    m_prec, m_tmax, m_tmin = medias_por_meses(seleccion)
    valores = (m_prec, m_tmax, m_tmin)
    # Cálculo y visualización de las diferencias en un climograma
    prec, tmax, tmin = variaciones_mensuales(historicos, valores)
    genera_climograma(prec, tmax, tmin)


def test_variaciones_anuales(registros):
    # Cálculo de registros históricos
    inicio_h = "1951-01-01"
    fin_h = "1989-12-31"
    seleccion_h = filtro_por_periodo(registros, inicio_h, fin_h)
    # Cálculo de registros del período a evaluar
    inicio = "2005-01-01"
    fin = "2016-12-31"
    seleccion_p = filtro_por_periodo(registros, inicio, fin)
    vprec, vtmax, vtmin = variaciones_anuales(seleccion_h, seleccion_p)
    print("Variación anual de precipitación: ", vprec)
    print("Variación anual de temperatura máxima: ", vtmax)
    print("Variación anual de temperatura mínima: ", vtmin)


def test_evolucion_variaciones_anuales(registros):
    rango_base = range(1951, 1990)
    rango_estudio = range(1990, 2017)
    evolucion_variaciones_anuales(registros, rango_base, rango_estudio)


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    registros = lee_registros('./csv/madrid-1951-2016.csv')
    print("TOTAL DE REGISTROS: ", len(registros))
    print(registros[:10], '\n')

    # test_filtro_por_periodo(registros)
    # test_medias_por_meses(registros)
    # test_genera_climograma(registros)
    # test_variaciones_mensuales(registros)
    # test_variaciones_anuales(registros)
    # test_evolucion_variaciones_anuales(registros)
