def factorial(num):
    resultado = 1
    for i in range(num, 0, -1):
        resultado *= i
    return resultado

print(factorial(5))
