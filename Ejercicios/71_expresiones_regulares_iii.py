import re

# print("\nEjemplo I - Anclas\n")
# print("Permite encontrar coincidencias de texto al comienzo o al final.")

lista_nombres = [
	'Ana', 
	'Pedro', 
	'María', 
	'Rosa', 
	'Sandra',
	'Celia'
]

print("\n=> Buscar nombres que contengan un rango entre las letras o y t \"[o-t]\":")
for elemento in lista_nombres:
	if re.findall('[o-t]', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Buscar nombres que comiencen por un ranto entre A y M \"^[A-M]\":")
for elemento in lista_nombres:
	if re.findall('^[A-M]', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Buscar nombres que terminan con un ranto entre o y t\"[o-t]$\":")
for elemento in lista_nombres:
	if re.findall('[o-t]$', elemento):
		print("[+] Encontrado: " + elemento)

elementos = ['Ma1', 'Se1', 'Ma2', 'Ba.1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'Ma5', 'MaB', 'MaC', 'MaD', 'MaE', 'MaF', 'Ba:3', 'Ba.4', 'Ba:A']

print("\n=> Pedidos de Ma comprendidos entre el 0 y el 3 \"Ma[0-3]\":")
for elemento in elementos:
	if re.findall('Ma[0-3]', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Pedido que comience por Ma NO comprendidos entre el 0 y el 3 \"Ma[^0-3]\":")
for elemento in elementos:
	if re.findall('Ma[^0-3]', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Pedido que comience por Ma comprendidos entre el 0 y el 3 de la A a la B\"Ma[0-3A-BE-F]\":")
for elemento in elementos:
	if re.findall('Ma[0-3A-BE-F]', elemento):
		print("[+] Encontrado: " + elemento)

print("\n=> Pedido que contengan Ba con . o : \"Ba[.:]\":")
for elemento in elementos:
	if re.findall('Ba[.:]', elemento):
		print("[+] Encontrado: " + elemento)