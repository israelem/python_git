from random import randint
from time import sleep

VALORES_CUEVAS = (1, 2)


def mostrar_introduccion():
    print("Estás en una tierra llena de dragones. Frente a ti hay dos cuevas. En \n"
          "una de ellas, el dragón es generoso y amigable y compartirá su tesoro \n"
          "contigo. El otro dragón es codicioso y está hambriento, y te devorará \n"
          "inmediatamente")


def elige_cueva():
    cueva_elegida = int(input('A qué cueva quieres entrar? (1 ó 2)\n'))
    while cueva_elegida not in VALORES_CUEVAS:
        cueva_elegida = int(input('A qué cueva quieres entrar? (1 ó 2)\n'))
    return cueva_elegida


def comprobar_cueva(cueva_elegida):
    cueva_amigable = randint(1, 2)
    print('Te aproximas a la cueva...')
    sleep(2)
    print('Es oscura y espeluznante...')
    sleep(2)
    print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...')
    sleep(2)
    if cueva_elegida == cueva_amigable:
        print('¡Te regala su tesoro!')
    else:
        print('¡Te engulle de un bocado!')


def preguntar():
    respuesta = input('¿Quieres jugar de nuevo? [S/N] \n')
    while respuesta not in 'SN':
        respuesta = input('¿Quieres jugar de nuevo? [S/N] \n')
    return respuesta == 'S'


if __name__ == '__main__':
    jugar_de_nuevo = True
    while jugar_de_nuevo:
        mostrar_introduccion()
        cueva_elegida = elige_cueva()
        comprobar_cueva(cueva_elegida)
        jugar_de_nuevo = preguntar()
