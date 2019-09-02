import re

print("\n Ejemplo I\n")

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintáxis sencilla."

print("[+] Busca aprender: ")
print(re.search("aprender", cadena))

print("\n[+] Busca aprenderr: ")
print(re.search("aprenderr", cadena))

textoBuscar = "aprender"
if re.search(textoBuscar, cadena) is not None:
	print("\n[+] He encontrado el texto.")
else:
	print("\n[+] NO he encontrado el texto.")

textoEncontrado = re.search(textoBuscar, cadena)

print("\n[+] Caracter dónde comienza a encontrar el texto: start ")
print(textoEncontrado.start())

print("\n[+] Caracter dónde finaliza el texto encontrado: end ")
print(textoEncontrado.end())

print("\n[+] Devuelve en una tupla dónde comienza y termina el texto buscado: span")
print(textoEncontrado.span())

print("\n[+] Encuentra todas las coincidencias del texto: findall")
textoBuscar = "Python"
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))
