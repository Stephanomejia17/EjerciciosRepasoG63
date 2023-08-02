def palindromo():
    cadena_de_texto = str(input("Ingrese una oracion: "))
    comparacion = ""
    for i in range(len(cadena_de_texto)-1, -1, -1):
        comparacion += cadena_de_texto[i]
    if(cadena_de_texto == comparacion):
        print("Es palindromo")
    else:
        print("No es palindromo")

palindromo()


