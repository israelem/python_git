import random as rd


def calcular_minas():
    return 10


def calcular_adyacentes(t_interno, fila, columna):
    if t_interno[fila][columna] != -1:
        minas_adyacentes = 0
        for d_fila in range(-1, 2):
            for d_columna in range(-1, 2):
                if 0 <= fila + d_fila < len(t_interno) and \
                        0 <= columna + d_columna < len(t_interno) and \
                        t_interno[fila + d_fila][columna + d_columna] == -1:
                    minas_adyacentes += 1
        t_interno[fila][columna] = minas_adyacentes


def generar_tablero_interno(tamaño, minas):
    # Inicializado a cero
    t_interno = [[0*x for x in range(tamaño)] for x in range(tamaño)]
    pares = [(x, y) for x in range(tamaño) for y in range(len(t_interno))]
    rd.shuffle(pares)
    for par in pares[:minas]:
        # La mina se representa con un -1
        t_interno[par[0]][par[1]] = -1
    for fila in range(len(t_interno)):
        for columna in range(len(t_interno)):
            calcular_adyacentes(t_interno, fila, columna)

    return t_interno


def inicializar_tablero_externo(tamaño):
    return [['.' for x in range(tamaño)] for x in range(tamaño)]


def finaliza_juego(minas, cubiertas):  # , t_externo):
    respuesta = False
    if cubiertas == minas:
        respuesta = True
    return respuesta


def mostrar_datos(t_externo):
    for fila in t_externo:
        print(fila)


def descubrir_casilla(t_interno, t_externo, fila, columna):
    for d_fila in range(-1, 2):
        for d_columna in range(-1, 2):
            if 0 <= fila + d_fila < len(t_externo) and \
                    0 <= columna + d_columna < len(t_externo):
                if t_interno[fila + d_fila][columna + d_columna] == 0:
                    t_externo[fila + d_fila][columna + d_columna] = ' '
                    t_interno[fila + d_fila][columna + d_columna] = -2
                    descubrir_casilla(t_interno, t_externo, fila + d_fila, columna + d_columna)
                elif t_interno[fila + d_fila][columna + d_columna] > 0:
                    t_externo[fila + d_fila][columna + d_columna] = t_interno[fila + d_fila][columna + d_columna]

        
def calcular_movimiento(t_interno, t_externo):
    instrucción, fila, columna = [x for x in input('Introduzca código [d/m/?] fila y columna a descubrir: ').split()]
    if instrucción == 'd':
        if t_interno[fila][columna] != -1:
            descubrir_casilla(t_interno, t_externo, fila, columna)
    elif instrucción == 'm':
        t_externo[fila][columna] = 'm'
    elif instrucción == '?':
        t_externo[fila][columna] = '?'


if __name__ == '__main__':

    TAMAÑO = 8

    minas = calcular_minas()
    t_interno = generar_tablero_interno(TAMAÑO, minas)
    cubiertas = len(t_interno) ** 2
    t_externo = inicializar_tablero_externo(len(t_interno))
    fin_juego = False
    while finaliza_juego(minas, cubiertas):
        mostrar_datos(t_externo)
        calcular_movimiento(t_interno, t_externo)
