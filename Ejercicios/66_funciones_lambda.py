# Función normal
def area_triangulo(base, altura):
    resultado = (base*altura) / 2
    return resultado

print(area_triangulo(5,7))

# Función lambda
area_triangulo_lbd = lambda base,altura:(base*altura)/2
print(area_triangulo_lbd(8,5))
print(area_triangulo_lbd(5,7))

al_cubo = lambda base:(base**3)
print(al_cubo(5))

destacar_valor = lambda comision:"¡{}! €".format(comision)

print(destacar_valor(1234))