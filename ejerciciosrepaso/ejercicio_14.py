lista = []
tamanio = int(input("Ingrese el tamanio de la lista: "))
for i in range(0, tamanio):
    valores = int(input("Ingrese el valor: "))
    lista.append(valores)

def media_aritmetica(list):
    suma = 0
    for i in range(0, len(list)):
        suma += list[i]
    return suma/len(list)

print(media_aritmetica(lista))