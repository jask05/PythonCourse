print("[+] Decoradores II - Recibir parámetros\n")

# Muchas funciones
# Se les quiere dar una funcionalidad añadida a TODAS por igual (pueden ser algunas escogidas).
# Alternativa 1: entrar en cada función para modificarla.
# Alternativa 2: usar decoradores.

def funcion_decoradora(funcion_parametro):
	# *args: recibe un indeterminado nº de parámetros
	# **kwargs: recibe argumentos clave-valor
	def funcion_interior(*args, **kwargs): 
		# Acciones adicionales que decoran
		print("--------------------------")
		print("[+] Se va a realizar un cálculo:")
		funcion_parametro(*args, **kwargs)

		# Acciones adicionales que decoran.
		print("[+] Ejecución finalizada.\n")
		print("--------------------------")

	return funcion_interior

# Decorando la función
@funcion_decoradora
def suma(n1,n2,n3):
	print(n1+n2+n3)

def resta(n1,n2):
	print(n1-n2)

@funcion_decoradora
def multiplicacion(n1,n2):
	print(n1*n2)

@funcion_decoradora
def potencia(base,exponente):
	print(pow(base,exponente))

suma(7,5,123)
resta(12,10)
multiplicacion(22,33)
potencia(base=5,exponente=3)