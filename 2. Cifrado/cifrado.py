# -*- coding: utf-8 -*-
'''
Cifrado y descifrado por el método César

AUTOR: Carlos G. Vallejo
REVISOR: Fermín Cruz, José A. Troyano, Mariano González
ÚLTIMA MODIFICACIÓN: 19/12/2017

La criptografía es el proceso de oscurecer la información para hacerla ilegible
si no se tiene cierta información especial. Durante siglos se han estado
desarrollando esquemas para encriptar (cifrar) mensajes – unos mejores que
otros – pero la llegada de los ordenadores e internet ha revolucionado este
campo. Actualmente es difícil no encontrar algún tipo de encriptación en muchos
aspectos de nuestras vidas. La encriptación nos permite compartir información
con otras personas o entidades de confianza sin temor a que sea revelada.

Un cifrado es un algoritmo para ejecutar la encriptación (cifrar) y la inversa,
la desencriptación (descrifrar). La información original se denomina texto
plano. Después de que es encriptado, se denomina texto crifrado. El texto
cifrado contiene toda la información del texto plano, pero no está en un
formato legible por un humano o un ordenador si no se dispone del mecanismo
adecuado para descifrarlo; debe parecer texto aleatorio para aquellos a los
que no está destinado.

Un cifrado normalmente depende de una pieza de información adicional,
denominada clave. La clave es incorporado en el proceso de cifrado; el mismo
texto plano cifrado con dos claves diferentes debe tener dos textos cifrados
diferentes. Sin la clave debería ser difícil descifrar el texto cifrado para
obtener el texto plano.

Aquí se va a tratar con un método de cifrado muy bien conocido (aunque nada
seguro) denominado el Cifrado César
(https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar).

El Cifrado César
La idea del Cifrado César es tomar un entero y desplazar (shift) cada letra
del mensaje por ese entero. En otras palabras, supóngase que el desplazamiento
es k. Todas las instancias de la i-ésima letra del alfabeto que aparezca en el
texto plano debe convertirse en la (i + k) letra del alfabeto en el texto
cifrado. Hay que ser cuidadoso con el caso en el que i + k supere el número
total de letras del alfabeto. En lo que sigue vamos a considerar exclusivamente
el código ASCII básico, sin tildes ni diéresis, ni la letra eñe. De este modo
la longitud del alfabeto es 26. Así es como se vería el alfabeto si se desplaza
tres lugares hacia la derecha:

Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c

Usando la clave anterior, podemos traducir rápidamente el mensaje “feliz” en
“iholc” (obsérvese cómo se comporta el desplazamiento en las letras finales,
de modo que w → z, x → a, y → b y z → c).

Las letras con tildes y eñes se dejarán igual al cifrar y, naturalmente, al
descifrar. Las mayúsculas se dejarán mayúsculas y las minúsculas, minúsculas.

Para descifrar los mensajes trabajaremos con un vocabulario de palabras en
español que obtendremos de un fichero de texto plano, en el que cada línea
contiene una palabra válida.


FUNCIONES DISPONIBLES:
----------------------
- carga_vocabulario(fichero):
    lee el fichero y devuelve un conjunto de cadenas
- es_palabra_valida(palabra, vocabulario):
    comprueba si la palabra está en el vocabulario y devuelve un booleano
- construye_diccionario_codificacion(desplazamiento):
    devuelve un diccionario con el que se va a cifrar/descifrar
- aplica_desplazamiento(texto, desplazamiento):
    aplica el diccionario anterior al texto; devuelve el texto desplazado
- descifra_mensaje(texto, vocabulario):
    descifra el texto usando el vocabulario; devuelve el texto descifrado
'''
import string

# EJERCICIO 1:
def carga_vocabulario(fichero):
    ''' Carga las palabras contenidas en el 'fichero'; en el archivo es.dic
    cada línea representa una palabra válida del castellano; contiene 292342
    palabras, recopiladas por Juan Luis Varona, de la Universidad de La Rioja.
    Las palabras están todas en minúsculas, y contienen tildes y diéresis.
    La función devolverá un conjunto formado por las palabras del fichero.
    Para eliminar el salto de línea ('\n') al final de las cadenas podemos
    usar el método strip de las cadenas.
    '''
    pass


# EJERCICIO 2:
def es_palabra_valida(palabra, vocabulario):
    ''' Recibe una palabra y el vocabulario de palabras válidas en español,
    y devuelve un booleano indicando si la palabra está en el vocabulario o no.
    Para ello, la pasaremos a minúsculas y eliminaremos todos los signos de
    puntuación que pueda llevar al principio o al final, como comas, abre o
    cierra paréntesis o admiración, etc. Los caracteres que tenemos que
    descartar son " !@#$%^&*()-_+={}[]|\:;'<>?,./\"¡¿"
    '''
    pass


# EJERCICIO 3:
def construye_diccionario_codificacion(desplazamiento):
    ''' Recibe un desplazamiento, que es un número entero, y devuelve un
    diccionario que hace corresponder a cada letra (minúscula o mayúscula) otra
    letra (minúscula o mayúscula como la anterior), que está desplazamiento
    lugares más adelante en el alfabeto. Si el lugar resultante es posterior al
    último, volveremos por el principio.
    Para obtener una string con las letras minúsculas usamos:
        string.ascii_lowercase
    Para obtener una con las mayúsculas usamos:
        string.ascii_uppercase
    '''
    pass


# EJERCICIO 4:
def aplica_desplazamiento(texto, desplazamiento):
    '''
    Aplica el cifrado César al parámetro texto con el desplazamiento indicado.
    Para ello, crea un vocabulario de codificación con el desplazamiento
    indicado y aplica ese desplazamiento a cada uno de los caracteres del texto
    que sean ascii puro (string.ascii_letters) omitiendo los caracteres de
    puntuación pero también las vocales con tilde o diéresis y la eñe.
    Devuelve el mensaje codificado con ese desplazamiento.
    '''
    pass


# EJERCICIO 5:
def descifra_mensaje(texto, vocabulario):
    '''
    Recibe un texto, que ha sido codificado con un desplazamiento que ignoramos,
    y el vocabulario de palabras válidas en español, y devuelve una tupla
    formada por el desplazamiento que ha sido necesario para decodificar y el
    texto decodificado.
    El procedimiento a seguir es el siguiente: probar todos los posibles valores
    de desplazamiento y elegir el "mejor". Definimos el "mejor" como el
    desplazamiento que crea el mayor número de palabras reales cuando usamos
    aplica_desplazamiento(desplazamiento) sobre el mensaje original.
    Si d fue el desplazamiento usado para cifrar el mensaje, se supone que
    26 - d será el mejor desplazamiento para descifrarlo.
    Nota: si hay varios valores de desplazamiento que son igual de buenos, se
    devolverá el desplazamiento (y el correspondiente mensaje descifrado) del
    primero que se haya encontrado.
    '''
    pass


def test_es_palabra_valida(vocabulario):
    palabra = input("Introduce una palabra (enter para finalizar): ")
    while palabra != "":
        valida = es_palabra_valida(palabra, vocabulario)
        if valida:
            print("La palabra", palabra, "es válida")
        else:
            print("La palabra", palabra, "no es válida")
        palabra = input("Introduce una palabra:")


def test_construye_diccionario_codificacion(vocabulario):
    diccionario = construye_diccionario_codificacion(3)
    print(diccionario)


def test_aplica_desplazamiento():
    texto_cifrado = aplica_desplazamiento('Programación', 24)
    print('Salida esperada: Npmepykyagól')
    print('Salida real:', texto_cifrado)

    
def test_descifra_mensaje(vocabulario):
    texto_descifrado = descifra_mensaje("Npmepykyagól", vocabulario)
    print('Salida esperada:', (2, 'Programación'))
    print('Salida real:', texto_descifrado)


def test_descrifra_historia(vocabulario):
    with open("./datos/historia.txt", encoding='utf-8') as f:
        historia_cifrada = f.read()
    desplazamiento_historia, texto = descifra_mensaje(
        historia_cifrada, vocabulario)
    print("Desplazamiento historia, valor esperado (17):",
          desplazamiento_historia)
    print("Texto descifrado:\n" + texto)


if __name__ == '__main__':
    vocabulario = carga_vocabulario("./datos/es.dic")
    print("Esperadas 292342 palabras;", end=' ')
    print("hay", len(vocabulario))
    print("Las palabras no deben terminar con '\\n' y deben tener tildes")
    print(list(vocabulario)[:10])
    
    #test_es_palabra_valida(vocabulario)
    #test_construye_diccionario_codificacion(vocabulario)
    #test_aplica_desplazamiento()
    #test_descifra_mensaje(vocabulario)
    #test_descrifra_historia(vocabulario)
