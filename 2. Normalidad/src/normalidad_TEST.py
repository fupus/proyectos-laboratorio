# -*- coding: utf-8 -*-

from normalidad import *
from scipy.stats import jarque_bera

################################################################
#  Funciones de test
################################################################
def test_muestra_histograma():
    muestra_histograma(FRECUENCIAS)
    muestra_histograma(PESOS)
    muestra_histograma(SINTETICA)
    

def test_calcula_momento_central():
    # El momento central de grado 1 es 0 (o muy cercano)
    print("Momento central(1) - Frecuencias: ", calcula_momento_central(FRECUENCIAS, grado=1))
    # El momento central de grado 2 coincide con la varianza
    print("Momento central(2) - Frecuencias: ", calcula_momento_central(FRECUENCIAS), "\n")
    

def test_calcula_asimetria():
    # La distribución de FRECUENCIAS no es simétrica
    print("Asimetría - Frecuencias: ", calcula_asimetria(FRECUENCIAS))
    # La distribución de PESOS es simétrica
    print("Asimetría - Pesos: ", calcula_asimetria(PESOS))
    # La distribución SINTETICA es muy simétrica
    print("Asimetría - Sintética: ", calcula_asimetria(SINTETICA), "\n")


def test_calcula_curtosis():
    # La distribución de FRECUENCIAS es más 'picuda'
    print("Curtosis - Frecuencias: ", calcula_curtosis(FRECUENCIAS))
    # La distribución de PESOS es más 'acampanada'
    print("Curtosis - Pesos: ", calcula_curtosis(PESOS))
    # La distribución SINTETICA es muy 'acampanada'
    print("Curtosis - Sintética: ", calcula_curtosis(SINTETICA), "\n")
    
    
def test_calcula_jarque_bera():
    # La distribución de FRECUENCIAS 'no es normal'
    print("JarqueBera - Frecuencias: ", calcula_jarque_bera(FRECUENCIAS))
    # La distribución de PESOS 'es más normal'
    print("JarqueBera - Pesos: ", calcula_jarque_bera(PESOS))
    # La distribución SINTETICA 'es muy normal'
    print("JarqueBera - Sintética: ", calcula_jarque_bera(SINTETICA), "\n")


def test_calcula_pvalue():
    # No podemos afirmar que FRECUENCIAS es normal
    jb_frec = calcula_jarque_bera(FRECUENCIAS)
    print("Pvalue - Frecuencias: ", calcula_pvalue(jb_frec, valores_chi2_2, pvalues_chi2_2))
    # No podemos afirmar que PESOS es normal
    jb_peso = calcula_jarque_bera(PESOS)
    print("Pvalue - Pesos: ", calcula_pvalue(jb_peso, valores_chi2_2, pvalues_chi2_2))
    # Podemos afirmar que SINTETICA es normal con un nivel de significación de 0.95
    jb_sint = calcula_jarque_bera(SINTETICA)
    print("Pvalue - Sintética: ", calcula_pvalue(jb_sint, valores_chi2_2, pvalues_chi2_2))
    # Cálculo del estadístico Jarque-Bera y el pvalue con la implementación de Scipy
    print("JarqueBera/Pvalue (Scipy) - Frecuencias: ", jarque_bera(FRECUENCIAS))
    print("JarqueBera/Pvalue (Scipy) - Pesos: ", jarque_bera(PESOS))
    print("JarqueBera/Pvalue (Scipy) - Sintética: ", jarque_bera(SINTETICA))
    

################################################################
#  Programa principal
################################################################
FRECUENCIAS = lee_serie('../data/frecuencias.csv')
print("Frecuencias[:10] ->", FRECUENCIAS[:10])
PESOS = lee_serie('../data/pesos.csv', float)
print("Pesos[:10] ->", PESOS[:10])
SINTETICA = lee_serie('../data/1000-puntos-normal-0-1.csv', float)
print("Sintética[:10] -> ", SINTETICA[:10], "\n")
    
#test_muestra_histograma()
#test_calcula_momento_central()
#test_calcula_asimetria()
#test_calcula_curtosis()
#test_calcula_jarque_bera()
#test_calcula_pvalue()    