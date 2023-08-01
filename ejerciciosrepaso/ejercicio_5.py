def cambio_fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) * 5/9

temperaturaFahrenheit = int(input("Ingrese la temperatura en Fahrenheit: "))
print(cambio_fahrenheit_a_celsius(temperaturaFahrenheit))