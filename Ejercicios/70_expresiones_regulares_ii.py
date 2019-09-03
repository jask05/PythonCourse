import re

print("\nEjemplo I - Anclas\n")
print("Permite encontrar coincidencias de texto al comienzo o al final.")

lista_nombres = ['Ana Martín', 'Raúl Cimas', 'Juán Gómez', 'Sandra López', 'Sandra García']

print("\n=> Comienza por \"^Sandra\":")
for elemento in lista_nombres:
	if re.findall('^Sandra', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Termina por \"Martín$\":")
for elemento in lista_nombres:
	if re.findall('Martín$', elemento):
		print("[+] Encontrado: " + elemento)

dominios = [
	'http://pildorasinformaticas.es', 
	'ftp://pildorasinformaticas.es', 
	'http://pildorasinformaticas.com', 
	'ftp://pildorasinformaticas.com',
	'ftp://pildorasinformaticas.eñe',
	'http://pildorasinforñaticas.com',
	'http://holaespaña.com'
]

print("\n=> Dominio \".es$\":")
for elemento in dominios:
	if re.findall('.es$', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Dominio que comience \"^ftp\":")
for elemento in dominios:
	if re.findall('^ftp', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Dominio que incluya la letra Ñ \"[ñ]\":")
for elemento in dominios:
	if re.findall('[ñ]', elemento):
		print("[+] Encontrado: " + elemento)

elementos = [
	'hombres',
	'mujeres',
	'niños',
	'niñas',
	'mascotas',
	'abuelo',
	'abuela',
	'camión',
	'camion'
]

print("\n=> Elemento que tenga tanto niños como niñas \"niñ[oa]s\":")
for elemento in elementos:
	if re.findall('niñ[oa]s', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Elemento que tenga (o no) acentos \"cami[óo]n\":")
for elemento in elementos:
	if re.findall('cami[óo]n', elemento):
		print("[+] Encontrado: " + elemento)