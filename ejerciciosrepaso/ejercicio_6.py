
lista = []
tamanio = int(input("Ingrese el tamanio de la lista: "))
for i in range(0, tamanio):
    valores = int(input("Ingrese el valor: "))
    lista.append(valores)

def calcular_suma(lista):
    tamanio = len(lista)
    suma_total = 0
    for i in range(0, tamanio):
        suma_total += lista[i]

    return suma_total

print(calcular_suma(lista))


