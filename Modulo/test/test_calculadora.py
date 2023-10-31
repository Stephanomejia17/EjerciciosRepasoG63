import pytest

from Modulo.Modelo.calc import Calculadora

# Requiere instalacion de pytest en el entorno virtual

#Decorador para parametrizar y probar varios valores


@pytest.mark.parametrize("a, b, esperado", [
    (2, 10, 12),
    (-150, -2000, -2150),
    (500, -300, 200),
    (0, -5, -5)
])
def test_calculadora_suma_correctamente(a, b, esperado):
    # Arrange
    calculadora = Calculadora()

    # Act

    resultado = calculadora.sumar(a, b)

    # Assert
    assert esperado == resultado


def test_calculadora_divide_correctamente():
    # Arrange
    calculadora = Calculadora()

    a = 50
    b = 20

    #Act
    resultado = calculadora.dividir(a, b)

    #Assert
    assert 2.5 == resultado

def test_calculadora_arroja_error_cuando_se_divide_por_cero():
    # Arrange
    calculadora = Calculadora()

    a = 50
    b = 0

    # Espera de una excepcion
    with pytest.raises(ZeroDivisionError):
        calculadora.dividir(a, b)

