from random import randint

INTENTOS_MAXIMOS = 6
numero_intentos = 1
numero = randint(1, 20)
nombre = input('¡Hola! ¿Cómo te llamas?')
print('Bueno, ' + nombre + ' , estoy pensando en un número entre 1 y 20.')

intento = int(input('Intenta adivinar. '))
while numero_intentos < INTENTOS_MAXIMOS and intento != numero:
    if intento > numero:
        print('Tu estimación es muy alta.')
    elif intento < numero:
        print('Tu estimación es muy baja.')
    intento = int(input('Intenta adivinar. '))
    numero_intentos += 1

if intento == numero:
    print('¡Buen trabajo, ' + nombre + '! ¡Has adivinado mi número en ' + str(numero_intentos) + ' intentos!')
else:
    print('Lo siento, ' + nombre + ' inténtalo de nuevo')
