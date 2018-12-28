# -*- coding: utf-8 -*-

from dhondt import *

################################################################
#  Funciones de test
################################################################
def test_calcula_provincias(votos, escaños):
    provincias = calcula_provincias(votos)
    print('PROVINCIAS:', provincias)
    if provincias != set(escaños):
        print("ERROR: los conjuntos de provincias no coinciden")
        print("   Fichero de votos: ", provincias)
        print("   Fichero de escaños: ", set(escaños))


def test_calcula_partidos(votos):
    partidos = calcula_partidos(votos)
    print('PARTIDOS:', partidos)


def test_calcula_diccionario_provincia(votos):
    provincia = 'Sevilla'
    diccionario_votos = calcula_diccionario_provincia(votos, provincia)
    print('VOTOS EN {}:'.format(provincia), diccionario_votos)
        
        
def test_calcula_diccionario_provincias(votos):
    tabla_votos = calcula_diccionario_provincias(votos)
    print('TABLA-2D DE VOTOS:')
    for provincia in tabla_votos:
        print(provincia, '->', tabla_votos[provincia])


def test_totales_por_partido(votos):
    tabla_votos = calcula_diccionario_provincias(votos)
    print('VOTOS POR PARTIDO', totales_por_partido(tabla_votos))


def test_genera_diagrama_tarta(votos):
    tabla_votos = calcula_diccionario_provincias(votos)
    votos_partido = totales_por_partido(tabla_votos)
    genera_diagrama_tarta(votos_partido, limite=6)


def test_genera_mapa_calor(votos):
    tabla_votos = calcula_diccionario_provincias(votos)
    genera_mapa_calor(tabla_votos, limite_columnas=6)


def test_calcula_tabla_porcentajes(votos):
    tabla_votos = calcula_diccionario_provincias(votos)
    tabla_porcentajes = calcula_tabla_porcentajes(tabla_votos)
    genera_mapa_calor(tabla_porcentajes, limite_columnas=6, fmt='.3f')
    

def test_calcula_escaños_provincia(votos, escaños):
    # Ejemplo con datos sintéticos
    votos_sinteticos = {'Partido A': 340000,
                        'Partido B': 280000,
                        'Partido C': 160000,
                        'Partido D': 60000,
                        'Partido E': 15000}
    escaños_provincia = calcula_escaños_provincia(votos_sinteticos, 7)
    print("DIPUTADOS DATOS SINTÉTICOS:", escaños_provincia)
    
    # Ejemplo con datos reales
    votos_provincias = calcula_diccionario_provincias(votos)
    provincia = list(votos_provincias)[0]     # Elegimos una provincia cualquiera
    votos_provincia = votos_provincias[provincia]
    escaños_provincia = calcula_escaños_provincia(votos_provincia, escaños[provincia])
    print("DIPUTADOS '{}': {}".format(provincia, escaños_provincia))
    

def test_calcula_tabla_escaños(votos, escaños):
    # Cálculo de la tabla de votos
    tabla_votos = calcula_diccionario_provincias(votos)
    
    # Inclusión de una provincia 'ÚNICA' para simular la circunscripción única
    votos_UNICA = totales_por_partido(tabla_votos)
    tabla_votos['ÚNICA'] = votos_UNICA
    escaños['ÚNICA'] = sum(escaños.values())
    
    # Cálculo de la tabla de escaños
    tabla_escaños = calcula_tabla_escaños(tabla_votos, escaños)
    genera_mapa_calor(tabla_escaños, limite_columnas=20)

   
################################################################
#  Programa principal
################################################################
#votos, escaños = lee_escrutinio('../data/and-2015-votos.csv', '../data/and-2015-escaños.csv')
#votos, escaños = lee_escrutinio('../data/cat-2017-votos.csv', '../data/cat-2017-escaños.csv')
#votos, escaños = lee_escrutinio('../data/generales-2015-votos.csv', '../data/generales-2015-escaños.csv')
#votos, escaños = lee_escrutinio('../data/generales-2016-votos.csv', '../data/generales-2016-escaños.csv')
votos, escaños = lee_escrutinio('../data/and-2018-votos.csv', '../data/and-2018-escaños.csv')
   
print('TOTAL DE REGISTROS DE VOTOS: ', len(votos)) 
print(votos[:10], '\n')
print('ESCAÑOS POR PROVINCIA:') 
print(escaños, '\n')
    
#test_calcula_provincias(votos, escaños)
#test_calcula_partidos(votos)
#test_calcula_diccionario_provincia(votos)
#test_calcula_diccionario_provincias(votos)
#test_totales_por_partido(votos)
#test_genera_diagrama_tarta(votos)
#test_genera_mapa_calor(votos)
#test_calcula_tabla_porcentajes(votos)
#test_calcula_escaños_provincia(votos, escaños)
#test_calcula_tabla_escaños(votos, escaños)