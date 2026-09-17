# 9. Diseña una función que calcule la potencia de un número. La función debe recibir la 
# base y el exponente como argumentos y devolver el resultado. 

# def calcular_potencia(base, exponente):
#     resultado = base ** exponente

#     return resultado

# import math
# def calcular_potencia(base, exponente):

#     resultado = math.pow(base, exponente)

#     return resultado


def calcular_potencia(base: int, exponente: int) -> int:
    """calcula la potencia de un numero dado un exponente

    Args:
        base (int): el valor numerico tomado como base de la potencia
        exponente (int): el valor numerico tomado como exponente

    Returns:
        int: el numero potenciado
    """
    resultado = 1
    for _ in range(0, exponente, 1):
        resultado *= base

    return resultado

##########################################

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

potencia = calcular_potencia(base, exponente)

print(potencia)
