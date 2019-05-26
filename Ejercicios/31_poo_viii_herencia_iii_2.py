# -*- coding: utf-8 -*-

class Persona():
    
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.residencia)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()

        print("Salario:", self.salario,"€", "\nAntigüedad:", self.antiguedad)

# Antonio = Persona("Antonio", "30", "Madrid")
# Antonio.descripcion()

Trabajador = Empleado("1500", "7", "Antonio", "55", "Madrid")
Manuel = Persona("Manuel", "55", "Madrid")
Trabajador.descripcion()
print("-------")
print("Is instance:", isinstance(Trabajador, Empleado))
print("Is instance:", isinstance(Manuel, Empleado))