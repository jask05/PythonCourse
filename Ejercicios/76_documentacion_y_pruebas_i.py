import doctest

def areaTriangulo(base, altura):
	"""
	Calcula el área de un triángulo utilizando los parámetros base y altura.
	
	>>> areaTriangulo(3,6)
	'El área del triángulo es: 9.0'

	"""
	base = base
	altura = altura
	return "El área del triángulo es: " + str((base*altura)/2)

def compruebaMail(mailUsuario):
	"""
	Evalua un email recibido en busca
	de la @. Si tiene una @ es correcto, 
	si tiene más de una @ es incorrecto,
	si la @ está al final es incorrecto.
	
	>>> compruebaMail("jask@jask.com")
	True

	>>> compruebaMail("jaskjask.com@")
	False

	>>> compruebaMail("jaskjask.com")
	False

	>>> compruebaMail("jask@@jask.com")
	False
	
	"""

	arroba = mailUsuario.count("@")
	if arroba != 1 or mailUsuario.rfind("@") == (len(mailUsuario)-1) or mailUsuario.find("@") == 0:
		return False
	else:
		return True

# print(areaTriangulo(2,4))
doctest.testmod()