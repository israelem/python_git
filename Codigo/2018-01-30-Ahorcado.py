import random as rd

IMÁGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
  +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

PALABRAS = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro ' \
           'burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula ' \
           'salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca ' \
           'tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ' \
           'ballena lobo wombat cebra'.split()

ABC = 'abcdefghijklmnñopqrstuvwxyz'


def generar_palabra_secreta():
    return rd.choice(PALABRAS)


def mostrar_tablero(fallos, palabra_secreta, letras_correctas):
    print(IMÁGENES_AHORCADO[fallos])
    palabra_guiones = palabra_secreta
    for c in palabra_secreta:
        if c not in letras_correctas:
            palabra_guiones = palabra_guiones.replace(c, '_ ')
    print(palabra_guiones, '\n')


def leer_letra():
    letra = input('Escriba una letra: ').lower()
    correcto = False
    while not correcto:
        if len(letra) < 1 and letra.lower() not in ABC:
            letra = input('Escriba una letra: ').lower()
        elif letra.lower() in letras_incorrectas + letras_correctas:
            letra = input('Ya ha escrito esa letra, escriba otra: ').lower()
        else:
            correcto = True
    return letra


def comprobar_letra(letra_propuesta, palabra_secreta, letras_correctas, letras_incorrectas, fallos):
    if letra_propuesta in palabra_secreta:
        letras_correctas += letra_propuesta
        print('La letra pertenece a la palabra secreta')
    else:
        letras_incorrectas += letra_propuesta
        fallos += 1
        print('La letra no se encuentra en la palabra secreta')

    return [fallos, letras_correctas, letras_incorrectas]


def comprobar_palabra(palabra_secreta, letras_correctas):
    lista = [c for c in palabra_secreta if c not in letras_correctas]
    return len(lista) == 0


if __name__ == '__main__':
    palabra_secreta = generar_palabra_secreta()
    letras_correctas = ''
    letras_incorrectas = ''
    acertado = False
    fallos = 0
    while fallos < (len(IMÁGENES_AHORCADO) - 1) and not acertado:
        mostrar_tablero(fallos, palabra_secreta, letras_correctas)
        letra_propuesta = leer_letra()
        fallos, letras_correctas, letras_incorrectas = comprobar_letra(letra_propuesta, palabra_secreta,
                                                                       letras_correctas, letras_incorrectas, fallos)
        acertado = comprobar_palabra(palabra_secreta, letras_correctas)
    if acertado:
        print('Enhorabuena, has acertado la palabra secreta:', palabra_secreta)
    else:
        print(IMÁGENES_AHORCADO[fallos])
        print('Lo siento, has perdido')
