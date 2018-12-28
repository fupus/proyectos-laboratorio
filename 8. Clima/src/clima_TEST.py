# -*- coding: utf-8 -*-

from clima import *

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
    periodo_base = list(range(1951, 1990))
    periodo_estudio = list(range(1990, 2017))
    evolucion_variaciones_anuales(registros, periodo_base, periodo_estudio)


################################################################
#  Programa principal
################################################################
registros = lee_registros('../data/madrid-1951-2016.csv')
print("TOTAL DE REGISTROS: ", len(registros)) 
print(registros[:10], '\n')

#test_filtro_por_periodo(registros)
#test_medias_por_meses(registros)
#test_genera_climograma(registros)
#test_variaciones_mensuales(registros)
#test_variaciones_anuales(registros)
#test_evolucion_variaciones_anuales(registros)