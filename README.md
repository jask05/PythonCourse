# PythonCourse

Curso de Python - [Píldoras informáticas](https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

## Vistos

1. Curso Python. Vídeo 1
2. Curso Python. Introducción. Vídeo 2
3. Curso Python. Sintaxis Básica I. Vídeo 3
4. Curso Python. Sintaxis Básica II Tipos, operadores y variables. Vídeo 4
5. Curso Python. Sintaxis Básica III Funciones I. Vídeo 5

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