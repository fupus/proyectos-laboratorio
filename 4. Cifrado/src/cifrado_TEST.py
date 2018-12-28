# -*- coding: utf-8 -*-

from cifrado import *

################################################################
#  Funciones de test
################################################################

def test_construye_diccionario_codificacion():
    codificacion = construye_diccionario_codificacion(10)
    print('\nSalida esperada:\na -> k\nF -> P\n')
    print('a ->', codificacion['a'])
    print('F ->', codificacion['F'])


def test_cifra_mensaje():
    texto_cifrado = cifra_mensaje('Programación', 24)
    print('\nSalida esperada: nPMEPyKyAGóL')
    print('Salida real:', texto_cifrado)


def test_descifra_mensaje():
    texto_descifrado = descifra_mensaje('nPMEPyKyAGóL', 24)
    print('\nSalida esperada: Programación')
    print('Salida real:', texto_descifrado)


def test_carga_vocabulario():
    vocabulario = carga_vocabulario('../data/es.dic')
    print('\nHay {} palabras en el vocabulario'.format(len(vocabulario)))
    print(list(vocabulario)[:10])


def test_es_palabra_valida():
    vocabulario = carga_vocabulario('../data/es.dic')
    print('\nSalida esperada:\n   hola: True\n   xyz: False')
    print('Salida real:')
    print('   hola:', es_palabra_valida('hola', vocabulario))
    print('   xyz:', es_palabra_valida('xyz', vocabulario))


def test_cuenta_palabras_validas():
    vocabulario = carga_vocabulario('../data/es.dic')
    print('\nSalida esperada: 4')
    print('Salida real:',
          cuenta_palabras_validas('Aquí hay cuatro palabras xxx hatat fff', vocabulario))


def test_rompe_codigo_cifrado():
    vocabulario = carga_vocabulario('../data/es.dic')
    texto_descifrado = rompe_codigo_cifrado('nPMEPyKyAGóL', vocabulario)
    print('\nSalida esperada:', (2, 'Programación'))
    print('Salida real:', texto_descifrado)
    
    with open("../data/historia.txt", encoding='utf-8') as f:
        historia_cifrada = f.read()
    desplazamiento, historia = rompe_codigo_cifrado(historia_cifrada, vocabulario)
    print("\nMejor desplazamiento para historia.txt: ", desplazamiento)
    print("Historia descifrada:\n" + historia)


################################################################
#  Programa principal
################################################################

#test_construye_diccionario_codificacion()
#test_cifra_mensaje()
#test_descifra_mensaje()
#test_carga_vocabulario()
#test_es_palabra_valida()
#test_cuenta_palabras_validas()
#test_rompe_codigo_cifrado()
