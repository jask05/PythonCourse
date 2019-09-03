import re

print("[+] Match: busca si hay coincidencias en un patrón de búsqueda al **comienzo**  de una cadena de texto.\n")

n1 = "Sandra López"
n2 = "sandra Gómez"
n3 = "María López"

if re.match("Sandra", n2, re.IGNORECASE):
	print("[-] Nombre encontrado.")
else:
	print("[-] Nombre NO encontrado.")

print("\n[+] Cadenas de texto que comiencen por una letra sin determinar y a continuación 'ara'.")
n1 = "Jara López"
n2 = "Lara Gómez"
n3 = "María López"

if re.match(".ara", n2, re.IGNORECASE):
	print("[-] Nombre encontrado.")
else:
	print("[-] Nombre NO encontrado.")

print("\n[+] Buscar cadenas de texto que comiencen por números.")
n1 = "Jara López"
n2 = "1234567890"
n3 = "12fadf7adfhu32"

if re.match("\d", n2):
	print("[-] Número encontrado.")
else:
	print("[-] NO número.")

print("\n[+] Search: busca en toda la cadena de texto revisando si el patrón de búsqueda se cumple o no.\n")

n1 = "Jara López"
n2 = "1234567890"
n3 = "12fadf7adfhu32"

if re.search("López", n1):
	print("[-] Nombre encontrado.")
else:
	print("[-] Nombre NO encontrado.")

n1 = "jshadfkjhasfklhaskfjasfhajsf87asdfadsfasdfasdf"
n2 = "sjalfkjasjfkasfashf87 adfsdk jfkaskjf"
n3 = "sadfa fasd fasd fadsfa hshdfg"

if re.search("87", n1):
	print("[-] Número encontrado.")
else:
	print("[-] Número NO encontrado.")