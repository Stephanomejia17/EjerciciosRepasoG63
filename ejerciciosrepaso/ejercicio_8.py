lista = []
tamanio = int(input("Ingrese el tamanio de la lista: "))
for i in range(0, tamanio):
    valores = int(input("Ingrese el valor: "))
    lista.append(valores)

def inverse(list):
    lista_inversa = []
    for i in range((len(list))-1, -1, -1):
        lista_inversa.append(list[i])
    return lista_inversa

print(inverse(lista))
