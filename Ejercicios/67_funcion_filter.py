# Ejemplo 1

# Lista que devuelva los pares
def numeroPar(num):
    if num % 2 == 0:
        return True

numeros = [17, 24, 7, 39, 8, 51, 92, 104, 123, 154218231]

print(list(filter(numeroPar, numeros)))

# Filter + Lambda
print(list(filter(lambda numeropar: numeropar%2==0, numeros)))

# Ejemplo 2: salario > 50000
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    # Sirve para poder imprimir llamando a una clase directamente, sin pasar por su método. 
    # Es un método que sirve para obtener la representación de tu objeto como string.
    def __str__(self):
        return "{} que trabaja como {}, y cobra {} €.".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Agus", "Ceo", 120000),
    Empleado("Ramón", "Mantenimiento", 20000),
    Empleado("Juán", "CTO", 110000)
]

salatios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for s in salatios_altos:
    print(s)