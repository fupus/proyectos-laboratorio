# -*- coding: utf-8 -*-

''' 
Poblacion mundial

@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: 30/10/2018


En este proyecto trabajaremos con datos de población mundial, representados 
mediante listas. Implementaremos una serie de funciones que nos permitirán mostrar
gráficas de evolución de la población, así como, comparar la población en distintos
países.

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye un conjuntos de datos de prueba:
  - population.csv: con los datos de población de diversos paises o agrupaciones de paises 
    en distintos años.
 
FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_poblaciones(fichero):
    lee el fichero de entrada y devuelve una lista de tuplas 
    (nombre_pais, cod_pais, anyo, num_habitantes)
- calcula_paises(poblaciones):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y devuelve una lista ordenada con los nombres
    de los paises o conjuntos de paises para los que hay datos
- filtra_por_pais(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (anyo, num_habitantes)
    con los datos del pais que se pasa como parámetro. 
    El pais se puede dar con su nombre completo o con su código
- filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (nombre_pais, num_habitantes)
    con los datos del año pasado como parámetro para los paises 
    incluidos en el parámetro paises. 
- muestra_evolucion_poblacion(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y genera un gráfico con la evolución de la población
    del pais dado como parámetro. El pais se puede dar con su nombre completo o con
    su código
- muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes), un año y 
    un grupo de paises y genera un gráfico 
    de barras con la población de esos países en el año dado como parámetro

'''
import csv
from matplotlib import pyplot as plt

########################################################################################
def lee_poblaciones(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas poblaciones
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]

    Cada línea del fichero se corresponde con los datos de un pais o agrupación de países, 
    y se representa con una tupla con los siguientes valores:
        - Nombre pais
        - Código pais
        - Año 
        - Num. habitantes del pais en ese año
    Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    en aquellos datos que sean de tipo numérico.
    '''
    pass
############################################################################################

############################################################################################
def calcula_paises(poblaciones):
    ''' Calcula el conjunto de paises presentes en una lista de paises
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]
    SALIDA: 
       - lista de paises -> [str]

    Toma como entrada una lista de tuplas (pais, cod_pais, anyo, num_habitantes) y 
    produce como  salida una lista ordenada con los nombres de los paises 
    para los que haya al menos un dato de poblacion. 
    La lista de salida no contendrá elementos repetidos.
    '''
    pass
##############################################################################################

############################################################################################## 
def filtra_por_pais(poblaciones, pais):
    ''' Selecciona las tuplas correspondientes a un determinado pais
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]
       - pais: del que se seleccionarán los registros -> str
    SALIDA: 
       - lista de tuplas (año, censo) seleccionadas -> [(int, float)]

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y
    produce como salida otra lista de tuplas (anyo, num_habitantes) con los datos de 
    poblacion del pais que se pasa como parámetro. El pais se puede indicar 
    bien dando su nombre completo, bien dando su código.
    '''
    pass
##############################################################################################

############################################################################################## 
def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    ''' Selecciona las tuplas correspondientes a un conjunto de paises de un año concreto
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]
       - anyo: del que se seleccionarán los registros -> int
       - paises: de los que se seleccionarán los registros -> [str]
    SALIDA: 
       - lista de tuplas (pais, censo) seleccionadas -> [(str, float)]

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida otra lista de tuplas (nombre_pais, num_habitantes) 
    en la que solo se incluyen aquellos datos
    correspondientes al año dado como parámetro y de los paises 
    incluidos en la colección paises
    '''
    pass
##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais):
    ''' Genera una curva con la evolución de la población de un país. El pais puede
    darse como su nombre completo o por su código.
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]
       - pais: del que se generará la gráfica -> str
    SALIDA EN PANTALLA: 
       - diagrama con la evolución del censo del país

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico con la evolución de la población del país dado como
    parámetro a lo largo del tiempo. 
    
    Estas son las instrucciones 'matplotlib' para trazar el gráfico
    a partir una cadena con el título que se va a mostrar en el gráfico,
    una lista de años y otra lista con los número de habitantes (con el mismo orden):
        
        plt.title(titulo)
        plt.plot(l_anyos,l_habitantes)
        plt.show()
    '''
    pass
###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    ''' Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, float)]
       - anyo: del que se generará la gráfica -> int
       - paises: de los que se generará la gráfica -> [str]
    SALIDA EN PANTALLA: 
       - diagrama de barras con la comparativa del censo por paises

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico de barras con el número de habitantes de los paises 
    dados como parámetro en el año anyo.
    Cada barra corresponde a un pais.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una cadena con el título del gráfico, 
    una lista de nombres paises y otra lista (con el mismo orden) de
    número de habitantes de esos países:
       
        plt.title(titulo)
        indice = range(len(l_paises))
        plt.bar(indice, l_habitantes)
        plt.xticks(indice, l_paises, fontsize=8)
        plt.show()
    '''
    # Calculamos la lista de poblaciones del año dado para los paises de la lista
    pass
###############################################################################################
