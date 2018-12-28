# -*- coding: utf-8 -*-

from poblacion import *

################################################################
#  Funciones auxiliares
################################################################

def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 
################################################################
#  Funciones de test
################################################################
def test_lee_poblaciones():
    print("Leidos " , len (POBLACIONES), "datos de población mundial")
    mostrar_numerado(POBLACIONES)    
        
        
def test_calcula_paises():         # Test de la función calcula_ediciones
    paises = calcula_paises(POBLACIONES)
    print("Paises")
    print("Leidos " , len (paises), "paises distintos")
    mostrar_numerado(paises)
  
def test_filtra_por_pais():         # Test de la filtra_por_pais
    poblacion_es = filtra_por_pais(POBLACIONES, "Spain")
    print("Poblacion españa")
    print("Leidos " , len (poblacion_es), "datos de población de España")
    mostrar_numerado(poblacion_es)

def test_filtra_por_paises_y_anyo():         # Test de la filtra_por_pais
    paises= ["Spain","Portugal","France","Mexico","China"]
    poblacion_2016 = filtra_por_paises_y_anyo(POBLACIONES, 2016, paises)
    print("Leidos " , len (poblacion_2016), "datos del año 2016 para los paises", paises)
    mostrar_numerado(poblacion_2016)
        
def test_muestra_evolucion_poblacion():
    muestra_evolucion_poblacion(POBLACIONES, "Spain")

def test_muestra_comparativa_paises_anyo():
    muestra_comparativa_paises_anyo(POBLACIONES, 2016,["Spain","Portugal","France","Mexico","China"])
        
################################################################
#  Programa principal
################################################################
POBLACIONES = lee_poblaciones('../data/population.csv')

#test_lee_poblaciones()
#test_calcula_paises()
#test_filtra_por_pais()
#test_filtra_por_paises_y_anyo()
#test_muestra_evolucion_poblacion()
#test_muestra_comparativa_paises_anyo()