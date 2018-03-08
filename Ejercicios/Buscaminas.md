Se dispone de un tablero en el que hay localizadas un número determinado de minas. El objetivo del Buscaminas es encontrar todas las minas, sin descubrir ninguna. El juego
acabará cuando queden sin descubrir tantas casillas como minas (éxito), o bien cuando se descubra una mina (fallo).

En cada momento se mostrará el contador de minas restantes y la configuración actual del tablero de juego.

Para jugar, el jugador irá indicando las coordenadas de las casillas que quiere levantar, marcar con una mina o anotar como dudosa. Cada operación se indicará mediante el formato “código fila columna”. Donde código puede ser: 
- d-> Descubrir una casilla
- m-> Marcar que hay una mina  
- ? -> Indicar que una casilla es dudosa.

Al descubrir una casilla podrá ocurrir que levantemos una mina, en cuyo caso el jugador pierde y se acaba el juego, o bien que la casilla esté vacía. Si la casilla estaba vacía,
aparecerá una cifra que indica el número de minas que hay en los cuadrados circundantes (diagonales incluidas). Si al levantar una casilla, vemos que no tiene minas
adyacentes, se deberán levantar además automáticamente todas las casillas que formen una superficie continua sin minas. Por ejemplo, si levantamos la casilla 2,7 ello
ocasionará que se levanten automáticamente además todas aquellas que aparecen en blanco, (porque son casillas contiguas entre si, en las que no hay minas adyacentes) y
las que delimitan dicha zona sin minas (en el ejemplo, las marcadas con número de minas 1, 2 y 3).
```
Minas: 20 Cubiertas: 133
  01234567890123456789
  --------------------
0|.1         2........
1|11 111  1112........
2|   1.1  1.111.......
3|   2.31 111 1.......
4|11 1..1     2.......
5|.211..2111112.......
6|....................
7|....................
8|....................
9|....................

Introduzca código [d/m/?] fila y columna a descubrir
```

Al indicar que en una casilla hay una mina, en la casilla aparecerá el símbolo “m” y el
juego prosigue normalmente.

Al indicar que una casilla es dudosa, en la casilla aparecerá el símbolo “?” y el juego
prosigue normalmente.
