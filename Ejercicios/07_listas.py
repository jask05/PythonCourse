miLista = ["Maria", 5, "Marta", True, "Mario", 78.34, "Omar", "Santiago"]

print(miLista[:])

print(miLista[2])

print(miLista[-4])

print(miLista[0:3])

print(miLista[2:])

miLista.append("Luis")

print(miLista[:])

miLista.insert(0, "Mariano")

print(miLista[:])

miLista.extend(["ele1", "ele2", "ele3", "ele1"])

print(miLista[:])

print(miLista.index("ele1"))

print("ele1" in miLista)
print("ele4" in miLista)

miLista.remove("ele2")
print(miLista[:])

miLista.pop()
print(miLista[:])

miLista2 = ["xad", "asd", "poi"]

miLista3 = miLista + miLista2
print(miLista3)

miLista2 = ["xad", "asd", "poi"] * 5
print(miLista2)