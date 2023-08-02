def crear_matriz():
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    matriz = []
    for i in range(0, filas):
        matriz.append([])
        for j in range(0, columnas):
            valor = int(input("Ingrese un valor: "))
            matriz[i].append(valor)
    return matriz, filas, columnas

def imprimir(matriz, filas, columnas):
    print("Elementos:\n")
    for i in range(0, filas):
        for j in range(0, columnas):
            print(matriz[i][j])
(matriz, f, c) = crear_matriz()
imprimir(matriz, f, c)

