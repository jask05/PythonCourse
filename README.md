# PythonCourse

Curso de Python - [Píldoras informáticas](https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

## Vistos

1. Curso Python. [Vídeo 1](https://www.youtube.com/watch?v=G2FCfQj-9ig&index=1&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)
2. Curso Python. Introducción. [Vídeo 2](https://www.youtube.com/watch?v=9ojhJsXNWCI&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=2)
3. Curso Python. Sintaxis Básica I. [Vídeo 3](https://www.youtube.com/watch?v=yppT6GPZMyo&index=3&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)
4. Curso Python. Sintaxis Básica II Tipos, operadores y variables. [Vídeo 4](https://www.youtube.com/watch?v=u4I9PqhqCo8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=4)
5. Curso Python. Sintaxis Básica III Funciones I. [Vídeo 5](https://www.youtube.com/watch?v=VY448UWAQ_0&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=5)
6. Curso Python. Sintaxis Básica IV Funciones II. [Vídeo 6](https://www.youtube.com/watch?v=vawEHhV_HFA)
7. Curso Python. Sintaxis Básica V. Las listas. [Vídeo 7](https://www.youtube.com/watch?v=Q8hugySbLQQ)
8. Curso Python. Sintaxis Básica VI. Las tuplas. [Vídeo 8](https://www.youtube.com/watch?v=Ufqh8aoR9hE)

# Apuntes

## Vídeo 1

    Nada

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