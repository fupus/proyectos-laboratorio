# -*- coding: utf-8 -*-
''' Análisis de una colección de tweets

AUTOR: José A. Troyano
REVISOR: Fermín Cruz
ÚLTIMA MODIFICACIÓN: 26/09/2017

Conjunto de funciones que permiten extraer información de tweets y obtener
ciertos indicadores de actividad a partir de una colección de tweets.
En la última función 'ejemplo_de_analisis' se muestra como se puede construir
una consulta compleja combinando las funciones desarrolladas.

Se trabajará sobre una colección de 1000 tweets en formato JSON recuperados
mediante la consulta ['messi', 'ronaldo'] el 28 de junio de 2017. Los alumnos
interesados en aprender cómo descragar colecciones de tweets usando la API de
Twitter pueden hacerlo usando alguno de estos paquetes Python:
    https://pypi.python.org/pypi/TwitterSearch/
    http://www.tweepy.org/
    http://twython.readthedocs.org/en/latest/
    https://pypi.python.org/pypi/twitter
    https://pypi.python.org/pypi/python-twitter/

Los datos de entrada estarán en formato JSON. Para cada tweet se dispone
de cuatro informaciones:
    - autor: usuario twitter autor del tweet
    - fecha: día y hora en la qye se creó el tweet
    - retweets: número de veces que el tweet ha sido retuiteado
    - texto: contenido del tweet

He aquí un fragmento de un fichero de entrada con la información
correspondiente a los dos primeros tweets:
    [
     {
      "texto": "RT @ImMESS10nante: El tatuador de Messi ...",
      "autor": "@lamboglianare01",
      "fecha": "Wed Jun 28 15:49:54 +0000 2017",
      "retweets": 4251
     },
     {
      "texto": "RT @mariomassaccesi: #Ahora #Urgente #Rosario ...",
      "autor": "@MafiaoRepublica",
      "fecha": "Wed Jun 28 15:49:54 +0000 2017",
      "retweets": 12
     },
    ...
    ]


FUNCIONES DISPONIBLES:
----------------------
- lee_fichero_json(fichero):
    lee un fichero JSON y devuelve una lista de tweets
- def filtra_por_retweets(tweets, num_rt):
    devuelve los tweets con al menos num_rt retweets
- filtra_por_usuarios(tweets, usuarios, minusculas=True):
    devuelve los tweets escritos por los usuarios de la lista
- filtra_por_periodo(tweets, inicio, fin):
    devuelve los tweets escritos entre los momentos inicio y fin
- actualiza_diccionario_frecuencias(dicc, lista):
    incrementa las frecuencias de un diccionario a partir de una lista
- numero_tweets_por_autor(tweets):
    calcula el número de tweets que ha escrito cada usuario
- ordena_diccionario(dicc, orden='desc', top=None):
    produce una lista de tuplas (clave, valor) ordenadas por valor
- extrae_informacion_tweet(tweet, minusculas=True):
    obtiene las etiquetas, menciones y palabras de un tweet
- extrae_informacion_coleccion(tweets):
    obtiene las frecuencias de las etiquetas, menciones y palabras de
    una lista de tweets
- distribucion_temporal_tweets(tweets, intervalos):
    traza una gráfica con la evolución temporal de una colección

- ejemplo_de_analisis(tweets):
    consulta construida sobre las funciones básicas anteriores
'''
import json
import re
from datetime import datetime
from matplotlib import pylab as plt


# EJERCICIO 1:
def lee_fichero_json(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tweets

    Cada tweet se representa mediante un diccionario con cuatro
    valores: autor, fecha, retweets, texto
    '''
    pass


# EJERCICIO 2:
def filtra_por_retweets(tweets, num_rt):
    '''Devuelve los tweets con al menos num_rt retweets'''
    pass


# EJERCICIO 3:
def filtra_por_usuarios(tweets, usuarios, minusculas=True):
    '''Devuelve los tweets escritos por los usuarios de la lista

    El parámetro 'minusculas' determina si los nombres de usuarios
    se pasan a minúsculas antes de la comparación, por defecto es True.
    '''
    pass


# EJERCICIO 4:
def filtra_por_periodo(tweets, inicio, fin):
    '''Devuelve los tweets escritos entre los momentos inicio y fin

    Si 'inicio' es None no habrá límite inferior, y si 'fin' es None
    no habrá límite superior. Ambos momentos de tiempo serán proporcionados
    mediante dos cadenas de caracteres. El formato de los tiempos recibidos
    como parámetros será distinto al formato en el que se especifican los
    tiempos en el fichero JSON donde se encuentran los tweets. He aquí
    una misma fecha en los dos formatos:
        - Parámetros:     "15:09:32 28-06-2017"
        - Tweets en JSON: "Wed Jun 28 15:09:32 +0000 2017"

    Para intepretar adecuadamente una fecha almacenada en una cadena
    de caracteres se usará el método 'strptime' del módulo 'datetime'
    de la librería estándar. Este método construye un ojbeto 'datetime'
    a partir de una cadena y un formato:
        objeto_datetime = datetime.strptime(cadena_tiempo_tweet, formato)

    El formato es una cadena de caracteres en la que se indican los elementos,
    y el orden en el que aparecen, que contiene un determinado formato de
    fecha. En el siguiente tutorial se puede encontrar una buena explicación
    sobre cómo construir los formatos:
        Formato: https://www.tutorialspoint.com/python/time_strptime.htm
    '''
    pass


# EJERCICIO 5:
def actualiza_diccionario_frecuencias(dicc, lista):
    ''' Incrementa las frecuencias de un diccionario a partir de una lista

    Toma como entrada un diccionario y una lista de elementos que serán
    usados como claves del diccionario. Por cada elemento de la lista
    se incrementa en uno la frecuencia correspondiente en el diccionario.
    Ya que los diccionarios son objetos, las modificaciones que sufra el
    diccionario 'dentro de la función' persisten 'fuera de ella'.
    '''
    pass


# EJERCICIO 6:
def ordena_diccionario(dicc, orden='desc', limite=None):
    ''' Produce una lista de tuplas (clave, valor) ordenadas por valor

    Además del diccionario 'dicc', recibe dos parámetros más:
       - orden: si es 'desc' el orden es descendente, en otro caso ascendente
       - limite: número de items recuperados. Si es None se recuperan todos
    Se usará la función 'sorted' para ordenar la lista de items de un
    diccionario. Como función clave se usará la siguiente expresión lambda
    que describe una función que accede al segundo elemento de una tupla:
            lambda x: x[1]
    '''
    pass


# EJERCICIO 7:
def numero_tweets_por_autor(tweets):
    ''' Calcula el número de tweets que ha escrito cada usuario

    Se construye un diccionario cuyas claves son los usuarios autores
    de tweets y el valor asociado el número de tweets escritos por
    cada autor.
    Se hace uso de la función:
         actualiza_diccionario_frecuencias(dicc, lista)
    '''
    pass


# EJERCICIO 8:
def extrae_informacion_tweet(tweet, minusculas=True):
    ''' obtiene las etiquetas, menciones y palabras de un tweet

    Recibe un tweet y devuelve como salida tres listas que se
    calculan a partir del atributo 'texto' del tweet:
        - etiquetas: formadas con '#' letras, dígitos y '_'
        - menciones: formadas con '@' letras, dígitos y '_'
        - palabras: fomadas solo con letras

    El parámetro 'minúsculas' determina si el tweet se pasa a
    minúsculas antes de la extracción, por defecto es True.
    Se utilizarán como separadores los siguientes caracteres:
           [' ', ',', '.', ';', '¿', '?', '¡', '!', ':', '/',
            '(', ')', '[', ']', '-', '"', "'", '\t', '\n']
    Para separar un texto en lista de terminos se usaran las funciones:
        - replace: para sustituir cualquier separador por ' '
        - split: para dividir usando como separador ' '

    Las expresiones regulares para cada tipo de término son:
        - expr_etiqueta = '#\w+'
        - expr_mencion = '@\w+'
        - expr_palabra = '\w+'
    Para determinar si un término encaja con una expresión regular se
    usará la función match del módulo re:
            re.match(expresion, termino)
    '''
    pass


# EJERCICIO 9:
def extrae_informacion_coleccion(tweets, descartados=[], minusculas=True):
    ''' Obtiene las frecuencias de las etiquetas, menciones y palabras
        de una lista de tweets

    Construye un diccionario de frecuencias para cada tipo de término.
    Se apoya en las siguientes funciones:
        - extrae_iformacion_tweet(tweet)
        - actualiza_diccionario_frecuencias(dicc, lista)
    Los términos incluidos en la lista 'descartados' no serán tenidos en
    cuenta. El parámetro 'minúsculas' determina si el tweet se pasa a
    minúsculas antes de la extracción, por defecto es True.
    '''
    pass


# EJERCICIO 10:
def distribucion_temporal_tweets(tweets, intervalos=10):
    '''Traza una gráfica con la evolución temporal de una colección

    Genera un diagrama de barras en el que se muestra el número de
    tweets escritos en distintos rangos de minutos. Se usa el método
    bar de matplotlib para generar el gráfico con las siguientes
    instrucciones:
        plt.bar(puntos, tweets_intervalo, width=tam_intervalo*0.9,
                tick_label=etiquetas)
        plt.show()
    Donde cada variable significa lo siguente:
        - puntos: lista de instantes de tiempo (en segundos, contados
        desde el primer tweet) donde se ubicarán las barras en el eje X
        del gráfico
        - tweets_intervalo: número de tweets escritos en cada intervalo
        de tiempo. Será una lista del mismo número de elementos que la
        anterior lista (puntos)
        - tam_intervalo: tamaño del intervalo. Se calcula a partir del
        número de intervalos que se desea visualizar y de la diferencia
        (en segundos) del momento de publicación del primer y último
        tweet.
        - etiquetas: lista de strings con el texto que se asociará a cada
        barra del gráfico. Se indicará (en minutos) el rango de tiempo
        correspondiente a cada intervalo.

    Para obtener todas las informaciones necesarias para componer la
    gráfica, se procederá de la siguiente forma:
        - Calcular una lista ordenada 'segundos' que contenga los segundos
        (a patir del primer tweet) en los que se publica cada tweet
        - Calcular 'tam_intervalo' a partir del primer y último elemento
        de la lista anterior
        - Calcular los puntos de corte de los intervalos (en segundos) y
        el número de tweets que cae dentro de cada intervalo
        - Calcular las etiquetas del eje X del gráfico (rangos de minutos)
    '''
    pass


# EJERCICIO 11:
def ejemplo_de_analisis(tweets):
    '''Consulta construida sobre las funciones básicas anteriores

    Se realizará el siguiente análisis:
        1) Seleccionar tweets con más de 100 retuits escritos después
        de las 15:15:15 del 29/08/2017
        2) Calcular los 50 usuarios más mencionados en dicha colección y
           mostrar esa lista como resultado
        3) Seleccionar de la colección inicial el conjunto de tweets escritos
           por alguno de esos 50 usuarios
        4) Mostrar como resultado los siguientes elementos calculados
           sobre esta última colección de tweets:
           - Número de tweets de la colección
           - Las 10 etiquetas más usadas
           - Los 10 usuarios más mencionados
    '''
    pass


################################################################
#  Funciones de test
################################################################
def test_filtra_por_retweets(tweets):
    filtro = filtra_por_retweets(tweets, 1000)
    print(len(filtro), filtro)


def test_filtra_por_usuarios(tweets):
    filtro = filtra_por_usuarios(tweets, ['@OvacionVE', '@Neymar__Crack'])
    print(len(filtro), filtro)


def test_filtra_por_periodo(tweets):
    filtro = filtra_por_periodo(tweets, "15:09:30 28-06-2017",
                                "15:09:50 28-06-2017")
    print(len(filtro), filtro)
    filtro = filtra_por_periodo(tweets, None, "15:09:50 28-06-2017")
    print(len(filtro), filtro)
    filtro = filtra_por_periodo(tweets, "15:49:54 28-06-2017", None)
    print(len(filtro), filtro)


def test_actualiza_diccionario_frecuencias():
    lista = ['a', 'b', 'a', 'a', 'c', 'c', 'd', 'a', 'a', 'b']
    dicc = {}
    actualiza_diccionario_frecuencias(dicc, lista)
    print(dicc)


def test_ordena_diccionario():
    lista = ['a', 'b', 'a', 'a', 'c', 'c', 'd', 'a', 'a', 'b']
    dicc = {}
    actualiza_diccionario_frecuencias(dicc, lista)
    tuplas = ordena_diccionario(dicc)
    print(tuplas)
    tuplas = ordena_diccionario(dicc, orden='asc')
    print(tuplas)
    tuplas = ordena_diccionario(dicc, limite=2)
    print(tuplas)


def test_numero_tweets_por_autor(tweets):
    dicc = numero_tweets_por_autor(tweets)
    tuplas = ordena_diccionario(dicc, limite=7)
    print(tuplas)
    claves = [c for (c, _) in tuplas]
    valores = [v for (_, v) in tuplas]
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=claves)
    plt.show()


def test_extrae_informacion_tweet(tweets):
    etiquetas, menciones, palabras = extrae_informacion_tweet(tweets[0])
    print(tweets[0])
    print("   ETIQUETAS: ", etiquetas)
    print("   MENCIONES: ", menciones)
    print("   PALABRAS: ", palabras, '\n')

    etiquetas, menciones, palabras = extrae_informacion_tweet(tweets[1],
                                                              minusculas=False)
    print(tweets[1])
    print("   ETIQUETAS: ", etiquetas)
    print("   MENCIONES: ", menciones)
    print("   PALABRAS: ", palabras, '\n')


def test_extrae_informacion_coleccion(tweets):
    sin_interes = ['de', 'https', 't', 'co', 'rt', 'y', 'el', 'la', 'a', 'que',
                   'ya', 'está', 'en', 'se', 'es', 'del', 'lo', 'con', 'su',
                   'un', 'por', 'los', 'me', 'al', 'donde', 'para', 'si',
                   'una', 'las', 'le', 'o', 'pero', 'te', 'sobre', 'q', 'x',
                   'mí', 'mi', 'era']
    ets, mencs, pals = extrae_informacion_coleccion(tweets,
                                                    descartados=sin_interes)
    print("FRECUENCIAS DE ETIQUETAS: ", ordena_diccionario(ets, limite=10))
    print("FRECUENCIAS DE MENCIONES: ", ordena_diccionario(mencs, limite=10))
    print("FRECUENCIAS DE PALABRAS: ", ordena_diccionario(pals, limite=100))


def test_distribucion_temporal_tweets(tweets):
    distribucion_temporal_tweets(tweets, 7)


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    fichero = './datos/messi-ronaldo.json'
    tweets = lee_fichero_json(fichero)
    print("COLECCIÓN INICIAL:", tweets, '\n')

    # test_filtra_por_retweets(tweets)
    # test_filtra_por_usuarios(tweets)
    # test_filtra_por_periodo(tweets)
    # test_actualiza_diccionario_frecuencias()
    # test_ordena_diccionario()
    # test_numero_tweets_por_autor(tweets)
    # test_extrae_informacion_tweet(tweets)
    # test_extrae_informacion_coleccion(tweets)
    # test_distribucion_temporal_tweets(tweets)
    # ejemplo_de_analisis(tweets)
