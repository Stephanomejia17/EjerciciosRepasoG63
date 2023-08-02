lista = []
tamanio = int(input("Ingrese el tamanio de la lista: "))
for i in range(0, tamanio):
    valores = int(input("Ingrese el valor: "))
    lista.append(valores)

def num_mayor(list):
    mayor = -999
    for i in range(0, len(list)):
        if(mayor < list[i]):
            mayor = list[i]
    return mayor

def num_menor(list):
    menor = 999
    for i in range(0, len(list)):
        if (menor > list[i]):
            menor = list[i]
    return menor

print("El numero mayor es", num_mayor(lista), "\nEl numero menor es", num_menor(lista))

