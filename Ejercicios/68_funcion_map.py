print("\nEjemplo 1: filter, devuelve números par \n")
# Ejemplo 1
# Lista que devuelva los pares
def numeroPar(num):
    if num % 2 == 0:
        return True

numeros = [17, 24, 7, 39, 8, 51, 92, 104, 123, 154218231]

print("Devuelve los números par: ")
print(list(filter(numeroPar, numeros)))


# Filter + Lambda
print("\nDevuelve los números par (filter + lambda): ")
print(list(filter(lambda numeropar: numeropar%2==0, numeros)))

print("\n----------------- \n")


# Ejemplo 2: salario > 50000
print("Ejemplo 2: salario > 5000 \n")

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    # Sirve para poder imprimir llamando a una clase directamente, sin pasar por su método. 
    # Es un método que sirve para obtener la representación de tu objeto como string.
    def __str__(self):
        return "{} que trabaja como {}, y cobra {} €.".format(self.nombre, self.cargo, self.salario)

# A todos se les aplicará una comisión que puede variar mensualmente.
listaEmpleados = [
    Empleado("Juan", "Director", 1200),
    Empleado("Agus", "Ceo", 7500),
    Empleado("Ramón", "Mantenimiento", 2150),
    Empleado("Juán", "CTO", 5500)
]

listaEmpleados2 = [
    Empleado("Juan", "Director", 1200),
    Empleado("Agus", "Ceo", 7500),
    Empleado("Ramón", "Mantenimiento", 2150),
    Empleado("Juán", "CTO", 5500)
]

for x in listaEmpleados:
	print(x)

print("\n")


# La función map sustituiría desde lambda hasta 50000 
# utilizando para ello una función, en vez de una condición
# como hacía "filter".
salarios_altos = filter(lambda empleado:empleado.salario>4000, listaEmpleados)
for salario_alto in salarios_altos:
	print("---> " + str(salario_alto.salario))

print("\n-----------------------\n")

print("Ejemplo 3. Función MAP\n")

def calcula_comision(empleado):
	empleado.salario = empleado.salario * 1.03
	return empleado

lista_empleados_comision = map(calcula_comision, listaEmpleados)
for empleado in lista_empleados_comision:
	print(empleado)

print("\n-----------------------\n")

print("Ejemplo 4. Función MAP + salario a sueldos < 3000€\n")

def calcula_comision_menostresmill(empleado):
	if empleado.salario <= 3000:
		empleado.salario = empleado.salario * 1.03
	return empleado

lista_empleados_comision = map(calcula_comision_menostresmill, listaEmpleados2)
for empleado in lista_empleados_comision:
	print(empleado)