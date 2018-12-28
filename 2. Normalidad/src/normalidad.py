# -*- coding: utf-8 -*-

''' Normalidad

AUTOR: José A. Troyano
REVISOR: José C. Riquelme, Fermín Cruz, Carlos G. Vallejo 
ÚLTIMA MODIFICACIÓN: 30/10/2018


En este proyecto trabajaremos con series numéricas, representadas mediante
listas. Implementaremos una serie de funciones que nos permitirán calcular
distintos indicadores estadísticos y, en última instancia, determinar si
los datos de la serie obedecen a una distribución normal. 

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye tres conjuntos de datos de prueba:
  - frecuencias.csv: con las frecuencias de aparición de todas las palabras
    presentes en El Quijote (en el fichero palabras_frecuencias.csv se
    muestran, además de las frecuencias, las correspondientes palabras).
  - pesos.csv: con los pesos de todos los futbolistas incluidos en el
    videojuego FIFA18 (en el fichero jugadores_pesos.csv se muestran, además
    de los pesos, los nombres de los jugadores).
  - 1000-puntos-normal-01.csv: con 1000 valores aleatorios generados siguiendo
    una distribución normal de media 0 y varianza 1.


TEST DE NORMALIDAD DE JARQUE-BERA:
----------------------------------
Para determinar si un conjunto de datos sigue una distribución normal
utilizaremos el test de Jarque-Bera, que se apoya en las siguientes métricas
estadísticas:
  - Momento central: valores esperados de ciertas funciones. Por ejemplo, el
    momento central de grado 2 (que se corresponde con la varianza) se calcula
    con la siguiente fórmula:
                                  E[(X-E[X])**2]
  - Asimetría: mide el grado de simetría de los datos con respecto a la media
  - Curtosis: mide el grado de concentración de valores en torno a la media
  

El estadístico de Jarque-Bera se distribuye asintóticamente como una
distribución chi2 con dos grados de libertad. Esto significa que, siempre que
el conjunto de muestras sea lo suficientemente grande, se puede usar la
distribución chi2 para verificar la hipótesis de que los datos pertenecen a una
distribución normal.

Las siguientes dos listas alineadas, sirven para 'tabular' la distribución chi2
con dos grados de libertad:
  - valores_chi2_2: muestra los valores críticos del estadístico (ordenados de
    mayor a menor)
  - pvalues_chi2_2: nivel de confianza para el correspondiente
    valor crítico

valores_chi2_2 = [13.8150, 11.9827, 10.5965, 9.2104, 7.3778, 5.9915, 4.6052,
                  3.7942, 3.2189, 2.7726, 2.4079, 2.0996, 1.8326, 1.5970,
                  1.3863, 1.1957, 1.0217, 0.8616, 0.7133, 0.5754, 0.4463,
                  0.3250, 0.2107, 0.1026, 0.0506, 0.0201, 0.0100, 0.0050, 0.0020]

pvalues_chi2_2 = [0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25,
                0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 
                0.85, 0.9, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999]

A partir de estas dos listas alineadas, se puede calcular la confianza
o pvalue con el siguiente procedimiento:
  - Calcular el estadístico del test Jarque-Bera
  - Buscar el menor de los valores críticos que supera o iguala al estadístico
  - El nivel de confianza será el elemento de la lista 'pvalues' correspondiente
    a dicho valor crítico


VISUALIZACIÓN:
--------------
En este proyecto solo usaremos una función de visualización que se proporciona
ya implementada:
- muestra_histograma(serie):
    genera un histograma a partir de una serie numérica


FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_serie(fichero, funcion_conversion=int):
    lee el fichero de entrada y devuelve una lista de valores numéricos
- calcula_momento_central(serie, grado=2):
    calcula el momento central de una serie para un determinado grado
- calcula_asimetria(serie):
    calcula la medida de asimetría de una serie
- calcula_curtosis(serie):
    calcula la medida de curtosis de una serie
- calcula_jarque_bera(serie):
    calcula el estadístico del test Jarque-Bera
- calcula_pvalue(estadistico, valores_criticos, pvalues):
    calcula el pvalue asociado a un determinado estadístico con respecto a una distribución
'''


from matplotlib import pyplot as plt
import seaborn as sns

valores_chi2_2 = [13.8150, 11.9827, 10.5965, 9.2104, 7.3778, 5.9915, 4.6052,
                  3.7942, 3.2189, 2.7726, 2.4079, 2.0996, 1.8326, 1.5970,
                  1.3863, 1.1957, 1.0217, 0.8616, 0.7133, 0.5754, 0.4463,
                  0.3250, 0.2107, 0.1026, 0.0506, 0.0201, 0.0100, 0.0050, 0.0020]

pvalues_chi2_2 = [0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25,
                0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 
                0.85, 0.9, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999]


# EJERCICIO 1:
def lee_serie(fichero, funcion_conversion=int):
    ''' Lee el fichero de entrada y devuelve una lista de valores numéricos
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
       - funcion_conversion: para pasar cadenas a valores numéricos -> type
    SALIDA: 
       - lista de números -> [float]  ó  [int]

    Toma como entrada un nombre de fichero y una función de conversión. Cada línea
    del fichero contiene un valor numérico de la serie. La función de conversión
    se utilizará para interpretar una cadena de caracteres como un valor numérico. Por 
    defecto se aplicará la función int(str), pero se podrá cambiar en la llamada por
    float(str) si se quieren manejar valores reales.
    '''
    pass
    

def muestra_histograma(serie):
    ''' Genera un histograma a partir de una serie numérica
    
    ENTRADA: 
       - serie: lista de números -> [float]  ó  [int]
    SALIDA EN PANTALLA: 
       - gráfica con histograma y estimación de distribución de probabilidad
    
    Usaremos la función distplot de seaborn que, además, muestra una 
    estimación de la función de densidad de probabilidad.
    '''
    sns.distplot(serie)
    plt.show()
    

# EJERCICIO 2:
def calcula_momento_central(serie, grado=2):
    ''' Calcula el momento central de una serie para un determinado grado
    
    ENTRADA: 
       - serie: lista de números -> [float]  ó  [int]
       - grado: grado del momento central a calcular -> int
    SALIDA: 
       - momento central del grado correspondiente -> float

    Toma como entrada una serie numérica y un grado (número entero positivo), y
    calcula el momento central con la siguiente expresión:
    
    momento = ((x1-media)**grado + (x2-media)**grado + ... + (xi-media)**grado)) / n
    
    Donde las variables usadas significan:
       - media: media de los valores de la serie
       - n: número de valores de la serie
    
    El momento central de grado 1 debe ser 0 (o un número muy pequeño por los
    errores de precisión). El momento central de grado 2 es la varianza (cuadrado
    de la desviación típica).
    '''
    pass


# EJERCICIO 3:
def calcula_asimetria(serie):
    ''' Calcula la medida de asimetría de una serie
    
    ENTRADA: 
       - serie: lista de números -> [float]  ó  [int]
    SALIDA: 
       - simetría de la serie de entrada -> float

    Toma como entrada una serie numérica y calcula la asimetría con la siguiente
    expresión:
    
    asimetria = m3 / (m2 ** (3/2))
    
    Donde las variables usadas significan:
       - m2: momento central de grado 2 de la serie
       - m3: momento central de grado 3 de la serie
       
    Un valor de asimetría bajo refleja una distribución simétrica con respecto a la
    media de la serie.
    
    Las distribución normal es simétrica, por tanto, su valor de asimetría es 0.
    '''
    pass


# EJERCICIO 4:
def calcula_curtosis(serie):
    ''' Calcula la medida de curtosis de una serie
    
    ENTRADA: 
       - serie: lista de números -> [float]  ó  [int]
    SALIDA: 
       - curtosis de la serie de entrada -> float

    Toma como entrada una serie numérica y calcula la curtosis con la siguiente
    expresión:
    
    curtosis = m4 / (m2 ** 2)
    
    Donde las variables usadas significan:
       - m2: momento central de grado 2 de la serie
       - m4: momento central de grado 4 de la serie
    
    Un valor alto de curtosis (también llamada 'apuntamiento') refleja una alta
    concentración de valores cerca del pico (media) y lejos de la cola.
    
    La distribución normal presenta una curtosis de 3.
    '''
    pass


# EJERCICIO 5:
def calcula_jarque_bera(serie):
    ''' Calcula el estadístico del test Jarque-Bera
    
    ENTRADA: 
       - serie: lista de números -> [float]  ó  [int]
    SALIDA: 
       - valor del estadístico Jarque-Bera para la serie -> float

    Toma como entrada una serie numérica y calcula el estadístico JB del
    test Jarque-Bera con la siguiente expresión:
    
    JB = n * ((asimetria**2)/6 + ((curtosis-3)**2)/24)
    
    Donde las variables usadas significan:
       - n: número de elementos de la serie
       - asimetria: coeficiente de asimetría de la serie
       - curtosis: coeficiente de curtosis de la serie
       
    El estadístico tiende a cero con distribuciones simétricas (asimetría 0)
    y con curtosis cercanas a 3.
    '''
    pass


# EJERCICIO 6:
def calcula_pvalue(estadistico, valores_criticos, pvalues):
    ''' Calcula el pvalue asociado a un determinado estadístico con respecto a una distribución
    
    ENTRADA: 
       - estadístico: valor calculado para el estadístico -> float
       - valores_criticos: números que marcan los umbrales de la tabla de distribución -> [float]
       - pvalues: pvalues asociados a los valores críticos anteriores -> [float]
    SALIDA: 
       - nivel de confianza correspondiente al valor del estadístico -> float
    
    Recibe como entrada el estadístico y la distribución 'tabulada' mediante dos
    listas alineadas:
        - valores: valores críticos del estadístico (deben estar ordenados de mayor a menor)
        - pvalues: nivel de confianza que asegura el correspondiente valor crítico
    
    El pvalue se calcula de la siguiente forma:
        Si el estadístico es mayor que el máximo de los valores críticos:
            pvalue = 0
        Si no:
            pvalue = elemento de la lista pvalues asociado al menor valor crítico
                      que es mayor o igual que el estadístico
    '''
    pass 