import random
def lista_de_pares():
    tamanio = int(input("Ingrese el tamanio de la lista: "))
    lista = []
    while(len(lista) < tamanio):
        aleatorio = random.randint(1, 100)
        if(aleatorio % 2 == 0):
            lista.append(aleatorio)
    return lista
print(lista_de_pares())
