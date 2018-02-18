# Diccionarios

Después de listas y tuplas, el siguiente tipo estructurado que se debe conocer en Python son los diccionarios. La manera más sencilla de entender lo que es un diccionario es recurrir a lo que todos entendemos por el mismo, un libro donde buscamos el significado de una palabra buscando la misma. Haciendo una abstracción del mismo, podemos entender el diccionario como pares de claves (la palabra) y el valor (el significado / acepciones). De este modo podemos inferir que un diccionario es una colección no ordenada de pares claves, valor donde el acceso a cada elemento no se realiza por su índice como en listas o tuplas, si no por su clave.

## Declaración de un diccionario

Así como los valores de una lista están encerrado entre dos corchetes `[]` o en el caso de las tuplas entre paréntesis `()`, para diccionarios se utilizan las llaves `{}` y para separar la clave del valor se utilizan los dos puntos `:`. Existen dos formas de declarar un diccionario, indicando directamente las parejas clave, valor o con la función `dict()`.

```Python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```

Para acceder a un elemento del diccionario, se utiliza la misma notación que para las listas y tuplas, sin embargo, se utiliza la clave y no el índice, ya que como se ha mencionado es una estructura desordenada. Por ejemplo:

```Python
>>> a['one']
1
```


Una vez declarado un diccionario, es posible añadir más elementos utilizando la notación `dict[key] = value` y de la misma manera si ya hemos añadido la clave al diccionario, vamos a realizar la modificación del valor almacenado. También cabe mencionar que existe una segunda forma de acceder al valor de una pareja y es utilizando el método get(), la ventaja de utilizar dicho método es que si la clave que buscamos no existe devuelve `None` y no lanza una excepción como ocurre con el acceso de la primera forma indicada. Por ejemplo:

```Python
>>> a = dict(one=1, two=2, three=3)
>>> a['four']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'four'
>>> a.get('four') == None
True
```

Por otro lado si necesitamos borrar una pareja de valores se utiliza la instrucción `del` al cual si no existe la clave a borrar, devuelve un error. Para evitar los errores mencionados debido a que la clave buscada no existe en el diccionario podemos comprobar previamente si se encuentra en el mismo utiliznado el operador `in` utilizada de la siguiente manera: `key in d`.

## Iterar sobre un diccionario

Podemos iterar sobre las claves de un diccionario o sobre sus valores o sobre las parejas de clave/valor, utilizando distintos métodos:

```Python
# Iterando solo sobre las claves
>>> for key in a:
...     print(key)
...
one
two
three
>>> for key in a.keys():
...     print(key)
...
one
two
three

# Iterando sobre las parejas clave / valor
>>> for key, value in a.items():
...     print(key, '-', value)
...
one - 1
two - 2
three - 3

# Iterando solo sobre los valores
>>> for value in a.values():
...     print(value)
...
1
2
3

```

## Otras funciones

Por último mencionaré dos funciones que nos pueden resultar últiles, la primera nos devuelve el tamaño del diccionario, es decir, el número de parejas y es la función `len()`. Por otro lado si necesitamos inicializar el diccionaro de forma que queremos borrar todas las parejas no tenemos más que utilizar el método `clear()` de la siguiente manera `d.clear()`.


## Ejercicios

1. Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "_Qué lindo día que hace hoy_" debe devolver: `'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1`

2. Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.

3. Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. **Nota:** utilizar el módulo `random` para obtener tiradas aleatorias.


## Referencias

[Diccionarios en Recursos Python](https://recursospython.com/guias-y-manuales/diccionarios/)

[Tutorial Python Argentina: diccionarios](http://docs.python.org.ar/tutorial/3/datastructures.html#diccionarios)

[Ejercicios](http://librosweb.es/libro/algoritmos_python/capitulo_9/ejercicios_12.html)

[Extendiendo el ahorcado](https://inventwithpython.com/es/9.5.html)

[Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
