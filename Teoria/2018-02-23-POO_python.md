## Ejercicios

**1.** Cree una clase llamada _Cuenta_. Como atributo tendrá un número float llamado saldo, con una cantidad inicial de 0 euros.
Tendrá dos métodos:

    - _ingresar_, con un parámetro que indica la cantidad a sumar al saldo.
    - _retirar_, con un parámetro que será un número float de euros a restar del saldo.

Cree un programa para ingresar 125.23, 503.4 y 50 euros y luego retire, 333.34 euros.
Muestre tras cada operación, el saldo de la cuenta.

**2.** Cree una clase llamada _Fichero_. Esa clase tendrá un atributo llamado ruta y otro llamado texto.
Implemente dos métodos:

    - _leer_fichero_, que leerá el fichero dado por el atributo ruta y guardará su contenido en el atributo texto.
    - _mostrar_fichero_, que imprimirá por pantalla el texto del fichero leído.

Use su nueva clase para leer el fichero que contiene al ejercicio 1.

**3.** Cree una clase llamada _Persona_. Contendrá el _nombre, DNI, dirección, teléfono_ y _e-mail_ (este último opcional) de un individuo.
Por método tendrá mostrar que imprimirá por pantalla los datos de la persona.
Utilice esa clase para crear una lista de personas y mostrar cada una de ellas. Los datos de cada persona están en el fichero [personas.txt](http://www.iaa.es/python/ejercicios/personas.txt). El formato de este fichero es una linea con los datos de cada persona. Están separados por ';'. Contiene información por este orden:

`nombre;DNI;dirección;teléfono;e-mail;saldo`

**4.** Cree una clase llamada _Punto_. Tendrá como atributos las coordenadas _x0_ e _y0_ del origen _(0, 0)_ por defecto, y las coordenadas _x_ e _y_ del punto en cuestión.
Los métodos serán: _distancia_ y _muestra_punto_. El primero devolverá la distancia del punto a su origen. El segundo imprimirá por pantalla el mensaje de texto: _(x,y)_, donde _x_ e _y_ son las coordenadas del punto.
Ejecute un programa que cree dos puntos con origen en (0,0) y muestre por pantalla el que tenga una distancia menor al centro:

```Python
distancia = math.sqrt ((x-x0)**2 + (y-y0)**2)
```

Tendremos que importar el modulo _math_, perteneciente a la librería estándar de Python.

**5.** Cree una clase llamada _Segmento_. Sus atributos serán dos objetos de la clase _Punto_. Esos puntos tendrán el mismo origen de coordenadas.
Como método tendrá _longitud_, que devolverá la distancia entre los dos puntos que componen el segmento.
Ejecute un programa que cree un segmento, muestre la longitud de ese segmento y el punto más cercano al origen.
NOTA: Si se reutiliza código ya hecho, este ejercicio se realiza en 20 lineas de código

**6.** Modifique la clase _Cuenta_ del ejercicio 1. Haga que el atributo saldo quede oculto. Cuando alguien desee leer ese atributo, debe escribir un número pin. Ese valor se introducirá como parámetro de la función _leer_saldo_, que agregará como nuevo método de la clase.
El PIN para poder realizar la operación será 3210.
Ahora que la variable saldo está oculta, ¿podría acceder a ella para mostrar su contenido sin conocer el PIN?. En caso afirmativo, explique cómo.

**7.** Cree una nueva clase que herede de Cuenta del ejercicio 1. Se llamará _Cuenta_ahorro_. Contendrá un nuevo método oculto ___avisar_ que informará en el momento en el que se realice una operación (_retirar_) que dé lugar a un saldo negativo. El mensaje a mostrar será _'NUMEROS ROJOS'_.
Modifique el método _retirar_ para que no deje sacar dinero si el saldo es negativo. En ese caso mostrará el mensaje por pantalla _'NO TIENE CREDITO'_.
Cree un programa que genere una cuenta en la que se ingresan 300 euros y se sacan, 290, 20 y 30 euros. En cada operación, muestre el saldo actual.

**8.** Cree una clase llamada _Buscador_. Sirve para buscar y reemplazar palabras dentro de un fichero. Esa clase heredará de la clase Fichero del ejercicio 2.
Tendrá tres nuevos métodos:

    - _buscar_, que tendrá como parámetro una cadena de caracteres que buscar en el fichero. Devolverá el número de veces que se ha encontrado el texto buscado.
    - _reemplazar_, que tendrá como parametros dos cadenas de caracteres: la cadena a buscar y la cadena por la que reemplazar la cadena buscada.
    - _escribir_, que guardará el fichero en la ruta que se pase como parámetro a este nuevo método.

Ejecute un código Python que cree un objeto _Buscador_. Leerá el fichero _ejercicio1.txt_ y devolverá el número de veces que aparezca la palabra _self_. Posteriomente, reemplazará la palabra _self_ por _this_, y guardará el texto resultante en el fichero _ejercicio1_mod.txt_. Compruebe que los cambios se han llevado a cabo en este último fichero.

**9.** Cree una clase llamada _Cliente_. Contendrá los datos de una _Persona_ (ejercicio 3) y de una _cuenta de ahorro_ (ejercicio 7) como atributos (herede _Cliente_ de _Persona_ y _Cuenta_ahorro_). Tendrá un nuevo atributo llamado _credito_ que, por defecto, será de 1000 euros.
Tendrá un método nuevo que será _mostrar_datos_, que imprimirá por pantalla los datos de la persona y su saldo y credito actuales.
Cree una persona con estos datos:

```
   Nombre: Mariano Fuentes
   DNI: 45365968L
   Direccion: C/ de las Alpujarras 2, bajo
   Telefono: 958776566
   Saldo: 2500
   Credito: 1500
   email: mfuentes@iaa.es
```

y muestre estos datos.

**10.** Cree una clase _Entidad_. Contendrá por atributos el _número de entidad_, su _director_ y _clientes_. Los dos primeros datos serán proporcionados al crear la entidad. Los siguientes se leerán del fichero _personas.txt_.
La clase _Entidad_ tendrá dos métodos:

    - _num_clientes_, que devolverá el número de clientes asociados a la entidad.
    - _balance_, que devolverá la suma de los saldos de los clientes de la entidad.


Este es un ejemplo de reutilización de código.

**11.** Crear una nueva clase _Fecha_. Tendrá por atributos el _día, mes_ y _año_. Estos parámetros se podrán inicializar cuando se cree un objeto.
Sobrecargar el método especial `__ge__` para que devuelva True cuando el año de la fecha con la que se compare un objeto sea posterior al de otro objeto.
Sería implementar la funcion:

```Python
def __ge__(self, otra_fecha):
	# codigo
```

**12.** Heredar de la clase _Fecha_ otra llamada _Fecha_mod_. Tendrá, además de los metodos anteriores, otro que imprima por pantalla una fecha en formato _dd/mm/aaaa_ cuando se ejecute la instrucción:

```Python
print(objeto_Fecha_mod)
```

Pruébelo mediante este código que haga uso de la clase Fecha_mod:

```Python
o = Fecha_mod(8, 2, 12)
print(o)
```
Ejercicios extrado de la página del curso de iniciacin a Python del Instituto de Astrofsica de Andalucí: [ejercicios](http://www.iaa.es/python/ejercicios/) y [curso](http://www.iaa.es/python/). **Nota:** el código mostrado se encuentra en la versión 2 de Python.
