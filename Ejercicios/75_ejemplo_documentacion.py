from modulos import comentario_modulos

class Areas:
	""" Esta clase calcula las áreas de diferentes figuras geométricas."""
	def areaCuadrado(self, lado):
		""" Calcula el área de un cuadrado
		elevando al cuadrado el lado pasado
		por parámetro"""
		self.lado = lado
		return "El área del cuadardo es: " + str(self.lado*self.lado)

	def areaTriangulo(self, base, altura):
		""" Calcula el área de un triángulo utilizando los parámetros base y altura."""
		self.base = base
		self.altura = altura
		return "El área del triángulo es: " + str((self.base*self.altura)/2)


areas = Areas()
print(areas.areaCuadrado(3))
# print(areas.areaCuadrado.__doc__)
# help(areas.areaTriangulo)
# help(areas)
help(comentario_modulos)