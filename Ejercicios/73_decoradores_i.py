print("[+] Decoradores\n")

# Muchas funciones
# Se les quiere dar una funcionalidad añadida a TODAS por igual (pueden ser algunas escogidas).
# Alternativa 1: entrar en cada función para modificarla.
# Alternativa 2: usar decoradores.

def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		# Acciones adicionales que decoran
		print("[+] Se va a realizar un cálculo:")
		funcion_parametro()

		# Acciones adicionales que decoran.
		print("[+] Ejecución finalizada.\n")

	return funcion_interior

# Decorando la función
@funcion_decoradora
def suma():
	print(15+20)

def resta():
	print(30-10)

@funcion_decoradora
def multiplicacion():
	print(10*20)

suma()
resta()
multiplicacion()