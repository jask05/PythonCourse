# PythonCourse

Curso de Python - [Píldoras informáticas](https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

## Vistos

1. [Vídeo 1](https://www.youtube.com/watch?v=G2FCfQj-9ig&index=1&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)
2. Introducción. [Vídeo 2](https://www.youtube.com/watch?v=9ojhJsXNWCI&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=2)
3. Sintaxis Básica I. [Vídeo 3](https://www.youtube.com/watch?v=yppT6GPZMyo&index=3&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)
4. Sintaxis Básica II Tipos, operadores y variables. [Vídeo 4](https://www.youtube.com/watch?v=u4I9PqhqCo8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=4)
5. Sintaxis Básica III Funciones I. [Vídeo 5](https://www.youtube.com/watch?v=VY448UWAQ_0&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=5)
6. Sintaxis Básica IV Funciones II. [Vídeo 6](https://www.youtube.com/watch?v=vawEHhV_HFA)
7. Sintaxis Básica V. Las listas. [Vídeo 7](https://www.youtube.com/watch?v=Q8hugySbLQQ)
8. Sintaxis Básica VI. Las tuplas. [Vídeo 8](https://www.youtube.com/watch?v=Ufqh8aoR9hE)
9. Sintaxis Básica VII Los diccionarios. [Vídeo 9](https://www.youtube.com/watch?v=2OmgHl8lp0I)
10. Condicionales I. [Vídeo 10](https://www.youtube.com/watch?v=iV-4F0jGWak)
11. Condicionales II. [Vídeo 11](https://www.youtube.com/watch?v=cf7o4s9nFu8)
12. Condicionales III. [Video 12](https://www.youtube.com/watch?v=qxgEolsC6rg)
13. Condicionales IV. [Video 13](https://www.youtube.com/watch?v=rDGsWYnQEJY)
14. Bucles I. For. [Video 14](https://www.youtube.com/watch?v=GQGhU1526Oo)
15. Bucles II. For. [Video 15](https://www.youtube.com/watch?v=D416qOEDrhI)
16. Bucle III. For. [Video 16](https://www.youtube.com/watch?v=KFz-mXB7qVI)
17. Bucles IV. While. [Video 17](https://www.youtube.com/watch?v=UfUM6uzl5SM)
18. Bucles V. Continue, pass y else. [Video 18](https://www.youtube.com/watch?v=c8WCRTU4udo)
19. Generadores I. [Video 19](https://www.youtube.com/watch?v=TLVnoqXGWpY)
20. Generadores II. [Video 20](https://www.youtube.com/watch?v=ucaHqGII350)
21. Excepciones I. [Video 21](https://www.youtube.com/watch?v=2MaAs7XU2T0)
22. Excepciones II. [Video 22](https://www.youtube.com/watch?v=HH3c6ZBvSx8)
23. Excepciones III. [Video 23](https://www.youtube.com/watch?v=dLH-oay4Bts)
24. POO I. [Video 24](https://www.youtube.com/watch?v=5Ohme4A2Weg)
25. POO II. [Video 25](https://www.youtube.com/watch?v=2UNrSiKEI8w)
26. POO III. [Video 26](https://www.youtube.com/watch?v=Y_SiIgxc-xI)
27. POO IV. [Video 27](https://www.youtube.com/watch?v=x5CY8fVyYLo)
28. POO V. [Video 28](https://www.youtube.com/watch?v=OU-e2uhoGxE)
29. POO VI. Herencia I. [Video 29](https://www.youtube.com/watch?v=u_VbLsIyzRk)
30. POO VII. Herencia II. [Video 30](https://www.youtube.com/watch?v=jMQQN9OxwVc)
31. POO VIII. Herencia III. [Video 31](https://www.youtube.com/watch?v=oe04X1B14YY)
32. POO IX. Polimorfismo I. [Video 32](https://www.youtube.com/watch?v=kV1cN_bqcSw)
33. Métodos de cadenas. [Video 33](https://www.youtube.com/watch?v=zH0VsRuD2ok)

# Apuntes

## Vídeo 1
- URLs interesantes:
    - [Referencia de la Biblioteca Python](http://pyspanishdoc.sourceforge.net/lib/lib.html)

## Vídeo 2

- Creado por Guido Van Rossum.
- Lenguaje de alto nivel. Gramática sencilla, clara y muy legible.
- Tipado dinámico y fuerte.
- Orientado a objetos.
- Librerías estándar.
- Interpretado.

## Vídeo 3 - Sintaxis básica I

- \>>> Prompt
- print ("Hola alumnos"); print("Adios")
- Comentarios en una línea con #
- \ dentro de un string hace un salto de línea pero solo a nivel visual del código.
- Identación.

## Vídeo 4 - Sintaxis básica II

- **Tipos de datos**
    - Numéricos
        - Enteros (int)
        - Coma flotante (float)
        - Complejos
    - Textos
    - Booleanos
        - True
        - False

- **Operadores**
    - Aritméticos
        - Suma: +
        - Resta: -
        - Multiplicación: *
        - División: /
        - Módulo (resto): %
        - Exponente (potencia): **
        - División entera (nº entero de una división): //
    - Comparación
    - Lógicos
    - Asignación
    - Especiales

- **Variable**: espacio en la memoria del ordenador donde se almacenará un valor que podrá cambiar durante la ejecución del programa. Empieza con una letra mayúscula o minúscula. Contiene letras, cifras y guió bajo.

- **Condicional if**:

    ```python
    numero1=5
    numero2=7
    if numero1>numero2:
        print("El numero1 es mayor")
    else:
        print("El numero2 es mayor")
    ```

## Notas

- En Python todo es un objeto. Se puede ver el tipo con la función *type()*.
    ```python
    num=5
    type(num)
    <class 'int'>
    
    text="Hola"
    type(text)
    <class 'str'>
    #Puede tener multisalto utilizando triple comillas dobles (""")
    
    coma=5.2
    type(coma)
    <class 'float'>
    ```

## Video 5 - Sintaxis Básica III Funciones I

- **Funciones**
    - **Qué son?** 
        - Una o varias líneas de código agrupadas de forma que funcionan como una unidad realizando una tarea específica.
        - Pueden devolver valores.
        - Pueden tener parámetros/argumentos.
        - Se les llama "métodos" cuando se encuentran definidas dentro de una clase.
    - **Utilidad**
        - Reutilización de código.
    - **Sintáxis**
        ```python
        def nombre_funcion(parametro) # parámetro opcional
            # instrucción de la función
            return # opcional

        # Ejecución
        nombre_funcion(parametro)
        ```
## Vídeo 6 - Sintaxis Básica IV Funciones II

- **Funciones**
    - Parámetros separados por coma.
    - Pueden tener de 0 a n.
    - Pueden devolver valor con **return**.

## Vídeo 7 - Sintaxis Básica V. Las listas.
- **Listas**
    - Equivalente a arrays/vectores.
    - Permite almacenar en la memoria del ordenador varios valores.
    - Variable = cajón // Lista = estantería (simil)
    - Permiten guardar diferentes tipos de valores.
    - Se pueden expandir dinámicamente.
    - Índice: posición dentro de la lista. Empieza por **0**.
    
    ```python
    nombreLista = [e1, e2, e3 ...]

    # Muestra toda la lista
    lista[:]

    # Tercer elemento (empieza en 0)
    lista[2]

    # De atrás hacia delante
    lista[-3]

    # Los tres primeros
    lista[0:3] # El uĺtimo nº es exclusión.

    # Acceso a los dos últimos elementos
    lista[2:]

    # Añadir elementos al final de la lista
    lista.append("Luis")

    # Añadir elemento al comienzo de la lista
    # Primer parámetro: posición donde añadirlo.
    lista.insert(0,"Mariano")

    # Añadir varios elementos a la vez
    lista.extend(["ele1", "ele2", "ele3"])

    # Índice de donde está un elemento
    lista.index("ele1")

    # Devuelve True/False si el elemento se encuentra o no en la lista
    print("elemento" in lista)

    # Eliminar elementos
    lista.remove("elemento")

    # Elimina último elemento añadido a la lista
    lista.pop()

    # Sumar listas diferentes
    lista = ["ele1", "ele2", "ele3"]
    lista2 = ["ulu1", "ulu2", "ulu3"]
    lista3 = lista + lista2

    # Repite la lista X veces
    lista = ["ele1", "ele2", "ele3"] * 3
    ```

## Video 8 - Sintaxis Básica VI. Las tuplas.
- **Tuplas**
    - Listas inmutables (ni añadir, ni eliminar, ni modificar elementos).
    - Permiten extraer porciones, pero el resultado es una tupla nueva.
    - ~~No permiten utilizar búsquedas (index).~~ A partir de Python 2.6 se puede utilizar el método _index_ en las tuplas.
    - Se puede comprobar si un elemento se encuentra dentro de la tupla.
    - Utilidad:
        - Más rápida a la hora de ejecutarse.
        - Menos espacio (mayor optimización).
        - Formatean cadenas (strings).
        - Se pueden utilizar de claves en un diccionario (las listas no).

        ```python
        tupla = ("e1", "e2", "e3")
        # Los parámetros son opcionales, pero es recomendable ponerlos.

        # Acceso
        tupla[0]

        # Convierte tupla en lista
        lista = list(tupla)

        # Convierte lista en tupla
        tupla = tuple(lista)

        # Contar cuántos elementos se encuentran dentro de una tupla
        tupla.count(13)

        # Averiguar longitud de la tupla
        len(tupla)

        # Tuplas unitarias: con un único elemento.
        tupla = ("elemento", )

        # Empaquetado de tupla. (Tuplas sin paréntesis)
        tupla = "e1", "e2", "e3"

        # Desempaquetado de tupla.
        # Permite asignar todos los elementos que forman parte de una tupla a diferentes variables
        tupla = ("Juan", 13, 1, 1955)
        nombre, dia, mes, anio = tupla
        ```

# Video 9 - Sintaxis Básica VII Los diccionarios.
- **Diccionarios**
    - Estructura de datos parecida a las listas y tuplas. 
    - Los datos se almacenan como **clave:valor**.
    - Permite almacenar listas y otros diccionarios.
    - Los elementos no están ordenados. El orden es indiferente a la hora de almacenar información en un diccionario.

    ```python
    diccionario = {"clave":"valor", "clave":"valor"...}
    print(diccionario)
    print(diccinario["clave"])

    # Agregar/sobrescribe elemento
    diccionario["nuevaclave"]="nuevovalor"

    # Eliminar elemento
    del diccionario["clave"]

    # Devuelve las claves: keys
    diccionario.keys()

    # Devuelve los valores
    diccionario.values()

    # Devuelve la longitud del diccionario
    len(diccionario)
    ```
# Video 10 - Condicionales I
- **Condicionales:**
    - Flujo de ejecución: orden que sigue un programa a la hora de ejecutarse. Suele ser de arriba hacia abajo, pero puede variar.
    
    ```python
    if elemento:
        condición
    # Hay que tener en cuenta el ámbito de la variable. Si se declara dentro de una función, solo "funcionará" aquí dentro. No se puede manipular fuera de la función.

    # Solicitud de valor. Se le puede pasar un texto descriptivo.
    variable = input("Introduce un valor: ") # Por defecto se considera un valor como texto.
    variable2 = int(input())
    ```

# Video 11 - Condicionales II
- **Condicionales:**
    ```python
    if comprobación:
        condición
    elif comprobación:
        condición
    else
        condición
    ```

# Video 12 - Condicionales III
- **Condicionales:**
    - Switch: no existe este condicional.
    - Se puede utilizar concatenación de operadores de comparación a la hora de construir un condicional.
    - Se puede utilizar operadores lógicos AND y OR. También existe "in" para evaluar varias condiciones.
    ```python
    # Se lee de izquierda a derecha. Si la primera condición es "falsa", pasaría a ejecutar el else. En cambio si es "verdadera" evalua la siguiente condición. Si es falsa, pasa al else, si no, ejecuta la condición.
    if 0 < edad < 100:
        print("Edad correcta.")
    else:
        print("Edad incorrecta.")

    # Convierte a string una variable
    str(variable)
    ```

# Video 13 - Condicionales IV
- **Condicionales:**
    - Operadores lógicos **and** y **or**. **And** se podría traducir como un "y si además", y el **or** "o si no".
    - **in**: compara lo que se almacena en una variable con varios valores.

    ```python
    if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
        # contenido

    # Para que no sea case sensitive...
    lower() # Transforma el valor a minúsculas
    upper() # Transforma el valor a mayúsculas
    ```

# Video 14 - Bucles I. For
- **Bucles - For:**
    - Utilidad: repetir una línea de código una o varias veces.
    - Tipos:
        - Determinados: se ejecutan un úmero determinado de veces y se sabe a priori cuántas veces se va a ejecutar el código del interior del bucle.
        - Indeterminados: se ejecutan un número indeterminado de veces y no se sabe a priori cuántas veces se va a ejecutar. El nº de veces dependerá de la circunstancia del programa.

    ```python
    for variable in elemento a recorrer:
        cuerpo del bucle

    # Elemento a recorrer: lista, tupla, string, rango, etc.
    ```

# Video 15 - Bucles II. For
- **Bucles - For:**
    - Recorrido de strings.
    - Tipo "range".
    - Notaciones especiales con print.

    ```python
    for i in ["Pildoras", "Informáticas", 2019]:
        print("Hola", end="") # No hace salto de línea
    ```

# Video 16 - Bucles III. For
- **Bucles - For:**
    - Notación especial con print.
    
    ```python
    for i in range(5):
        print(f"Valor de la variable: {i}")
        # f-strings
        # Unir texto con variables.
        # 
    ```

# Video 17 - Bucles IV. Bucle While
- **Bucles - While:**
    - Se desconoce cuántas veces se va a ejecutar hasta que se sepa con exactitud.
```python
while condicion
    # cuerpo del bucle
```

# Video 18 - Bucles V. Bucles: continue, pass y else
- **Bucles: continue, pass y else:**
    - **Continue**: salta a la siguiente iteración del bucle. Ignora esa vuelta de bucle y saltaría a la siguiente.
    - **Pass**: devuelve "null" en cuanto se lee el bucle, es como si no se ejecuta esa iteración. Se suele usar en clases nulas (para dejarla para después) o para bucles sin definir.
    - **Else**: funciona como en un condicional. Se ejecuta cuando el bucle está vacío, cuando haya terminado de recorrer el texto (haya completado todas las vueltas)

# Video 19 - Generadores I
- **Generadores:**
    - Estructuras que extraen valores de una función que se almacenan en objetos iterables. Se pueden recorrer con un bucle (while/for) o con iteradores.
    - Los valores se almacenan de uno en uno.
    - Cada vez que se almacene un valor, el generador permanece en un estado de stand-by o pausa. Llamado: suspensión de estado.
    - ¿Ventajas? 
        - Más eficientes que funciones tradicionales. No guarda todos los elementos en memoria, si no que va 1 a 1 (más rápido).
        - Muy útiles con lista de valores infinitos: generar Ips al azar.
        - En algunos escensarios, será más útil que un generador devuelva los valores de uno en uno.

    
    ```python
    # Función tradicional
    """ El control de flujo pasa de la llamada a la función. Genera la lista de nº pares y con la instrucción return devuelve la lista, y al devolverla, el control de flujo de la ejecución vuelve otra vez donde se generó la llamada. """
    def generaNumeros():
        return numeros

    # Generador
    """
    Hay una función, con líneas de código que construyen la lista. En lugar de la instrucción return, estaría la instrucción yield. Gracias a esta, lo que se consigue es que cuando en el código hay una llamada a esa función, el control de ejecución pasa a esa función, y la instrucción yield construye un objeto iterable con el primer valor de esa lista (ej nº pares). Se construye un objeto generador iterable en el cual está almacenado el primer valor que nos ha de devolver. Una vez generado ese objeto pasa a stand-by (suspensión) y el control de flujo de ejecución pasa otra vez al algoritmo donde se hizo la llamada. Si se vuelve a llamar al generador vuelve a obtener el segundo valor y entra en suspensión. Se devuelven los valores de 1 en 1 dentro de un objeto generador iterable."""
    def generarNumeros():
        yield numeros
    ```

# Video 20 - Generadores II
- **Generadores:**
    - Cuando se utiliza **yield from** lo que se hace es simplificar el código de los generadores en el caso de utilizar bucles anidados.
    - Se parece un array de 2 dimensiones.

     ```python
    # Cuando se coloca un asterisco se indica que recibe nº
    # indeterminado de elementos y también se le indica
    # que estos argumentos serán tuplas
    # Yield from simplifica la siguiente sintáxis
    """
    def devuelve_ciudades(*ciudades):
        for elemento in ciudades:
            for subElemento in elemento:
                yield subElemento
    """
    def devuelve_ciudades(*ciudades):
        for elemento in ciudades:
            yield from elemento

    ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Valencia", "Bilbao")

    print(next(ciudades_devueltas))
    print(next(ciudades_devueltas))
    ```

# Video 21 - Excepciones
- **Excepciones:**
    - **¿Qué es?** error en tiempo de ejecución. Cuando hay un programa correctamente escrito, sin error de sintáxis, pero pasa algo inesperado.
    - "Intenta ejecutar esta parte del código y si no puedes continúa."

# Video 22 - Excepciones II
- **Excepciones:**
    - Capturar varias excepciones.
    - Cláusula **finally**. Se ejecuta siempre, tanto si ocurre o no una excepción.

# Video 23 - Excepciones III
- **Excepciones:**
    - Instrucción **raise**.
    - Creación de excepciones propias.
    ```python
    def evaluaEdad(edad):
        if edad<0:
            raise TypeError("No se permiten edades negativas")

    print(evaluaEdad(-18))
    ```

# Video 24 - POO I
- **POO**
    - Paradigmas de programación
        - Orientado a procedimientos (antiguos): Fortran, Cobol, Basic...
        - Programación Orientado a objetos
    - ¿Qué es?:
        - Trasladar el comportamiento de los objetos reales a código.
        - Los objetos tienen un estado, un comportamiento (¿qué pueden hacer?), y unas propiedades.
    - Ejemplo (coche):
        - **Estado**: parado, circulando, aparcado, etc.
        - **Propiedades (atributos)**: color, peso, tamaño, etc.
        - **Métodos (Comportamiento)**: Función especial que pertenece a la clase donde se crea. La función no pertenece a ninguna clase. Puede arrancar, frenar, girar, acelerar, etc.
            - **self**: hace referencia al propio objeto perteneciente a la clase.
    - Ventajas:
        - Programa dividido en "partes" (módulos,clases, etc.). Modularización.
        - Código reutilizable. Herencia.
        - Si existe algún fallo el programa no cae, sigue funcionando.
        - Encapsulamiento.

# Video 25 - POO II
- **POO**
    - Vocabulario:
        - **Clase**: modelo donde se redactan las características comunes de un grupo de objetos. Coche => chasis, 4 ruedas.
        - **Objeto / Ejemplar de clase / instacia de clase / ejemplarizar una clase**: objeto o ejemplar perteneciente a una clase. Comparten una serie de características comunes, y luego cada uno de ellos tiene sus propias características.
        - **Modularización**: aplicación con varias clases. Cada elemento puede funcionar de forma independiente.
        - **Encapsulamiento / encapsulación**: el funcionamiento interno de un objeto está protegido del exterior. Una clase "no sabe" lo que hace otra clase. Las clases se "conectan" utilizando **métodos de acceso.** Solo tendrán acceso a ciertas características de algunas clases.
        - **Herencia**: 
        - **Polimorfismo**:
        - **Nomenclatura del punto:** 
            - Objeto: miCoche
            - Acceso a propiedades: miCoche.valor // miCoche.color // miCoche.altura
            - Acceso a comportamientos: miCoche.arranca() // miCoche.frena() // miCoche.gira()

# Video 26 - POO III
- **POO**
    - El **self** dentro de un método se "traduce" como el nombre de la variable con la que se instancia la clase.
    ```python
    class Coche():
        enmarcha = Flase

        def arrancar(self):
            self.enmarcha = True

    miCoche = Coche()
    miCoche.arrancar() # True // Traducción: miCoche.enmarcha = Ture
    ```

# Video 27 - POO IV
- **Constructor**: método especial que le da estado inicial a los objetos. Forma de especificar claramente cual va a ser el estado inicial de los objetos que pertenezcan a una clase.
- **Encapsulación:** protege una propiedad para que no se pueda modificar desde fuera de la clase. Para ello se pone dos guiones bajos en el nombre de la variable. **IMPORTANTE**: cuando se usa la variable hay que poner los dos guiones bajos. Si se llama a la variable como "ruedas" en vez de "__ruedas" estaríamos hablando de dods variables diferentes.
```python
self.__ruedas = 4
    ```
# Video 28 - POO V
- **Encapsulación de métodos:** igual que con las variables, utilizando guión bajo. Se deben encapsular cuando el objeto o la clase así lo necesite. Depende del comportamiento que se busque que tenga según el propio criterio del desarrollo.

# Video 29 - POO VI. Herencia
- **Herencia**
    - **¿Qué es?**: clase 1 (clase padre/superclase) => clase 2 (subclase/superclase). Conjunto de clases que toman elementos de otras.
    - **¿Para qué sirve?**: Reutilización de código. Preguntarse qué características en común tienen todos los objetos. También qué comportamientos en común tienen entre todos.
    - **¿Cómo hacer que las clases hereden?**: Se engloban todos las propiedades y métodos en una clase/superclase. Las particularidades se construyen en sus propias clases.

# Video 30 - POO VII. Herencia II
- **Herencia**
    - Sobre escritura de métodos.
    - **Herencia simple y múltiple**: hereda el constructor de la primera clase asignada en la herencia múltiple (más a la izquierda).

# Video 31 - POO VIII. Herencia III
- **Herencia**
    - Como depende de que clase herede primera, puede heredar su **init** o no. La solución **no elegante** es duplicar ese init que se necesita en el de la clase que va a heredar. La **mejor solución** es utilizar el método **super()**.
    - **super()**: llama al método de la clase padre.
    - **isinstance()**: informa si un objeto es instancia de una clase determinada. Devuelve True o False. **No hace falta utilizar self.**

# Video 32 - POO. Polimorfismo.
- **Polimorfismo**: "muchas formas". Un objeto puede cambiar de forma dependiendo del contexto donde se utilice el método/compotamiento. Se tienen que llamar todos los métodos de la misma clase de la misma manera.

# Video 33 - Métodos de cadenas
- **Manipulación de cadenas (strings)**:
    - **upper()**: convierte en mayúscula todas las letras de un string.
    - **lower()**: convierte en minúsculas todas las letras de un string.
    - **capitalize()**: string pone la primera letra en mayúscula.
    - **count()**: cuenta cuantas veces aparece una letra o una cadena de caractéres dentro de un texto.
    - **find()**: representa el índice, la posición, en la cual aparece un carácter o un grupo de ellos dentro de un texto.
    - **isdigit()**: comprueba si un dígito es valor númérico o no. Devuelve True/False.
    - **isalum()**: comprueba si los caracteres son alfanuméricos.
    - **isalpha()**: comprueba si hay solo letras. Espacios NO cuentan.
    - **split()**: separa por palabras utilizando espacios.
    - **strip()**: borra los espacios sobrantes al principio y final.
    - **replace()**: cambia una palabra/letra por otra.
    - **rfind()**: representa el índice de un carácter, pero lo hace contando desde atrás.
    - [Más métodos...](http://pyspanishdoc.sourceforge.net/lib/string-methods.html)