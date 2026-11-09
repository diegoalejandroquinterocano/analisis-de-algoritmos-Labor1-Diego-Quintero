"""Módulo para el cálculo del subarreglo de suma máxima.

Implementa soluciones mediante Fuerza Bruta y Dividir y Vencer.
"""


def subarreglo_fuerza_bruta(arr: list[int | float]) -> tuple[int, int, int | float]:
    """Calcula el subarreglo contiguo de suma máxima por fuerza bruta.

    Args:
        arr (list[int | float]): Lista de valores numéricos.

    Returns:
        tuple[int, int, int | float]: Tupla con (inicio, fin, suma_maxima).
    """
    n = len(arr)
    if n == 0:
        return 0, 0, 0

    max_suma = float("-inf")
    inicio = 0
    fin = 0

    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += arr[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
                inicio = i
                fin = j

    return inicio, fin, max_suma


def suma_cruzada(
    arr: list[int | float], bajo: int, medio: int, alto: int
) -> tuple[int, int, int | float]:
    """Encuentra el subarreglo máximo que cruza el punto medio.

    Args:
        arr (list[int | float]): Lista de números enteros o flotantes.
        bajo (int): Índice inicial del subarreglo.
        medio (int): Índice medio divisorio.
        alto (int): Índice final del subarreglo.

    Returns:
        tuple[int, int, int | float]: Tupla con (max_izq, max_der, suma_total).
    """
    suma_izq = float("-inf")
    suma_actual = 0
    max_izq = medio

    for i in range(medio, bajo - 1, -1):
        suma_actual += arr[i]
        if suma_actual > suma_izq:
            suma_izq = suma_actual
            max_izq = i

    suma_der = float("-inf")
    suma_actual = 0
    max_der = medio + 1

    for j in range(medio + 1, alto + 1):
        suma_actual += arr[j]
        if suma_actual > suma_der:
            suma_der = suma_actual
            max_der = j

    return max_izq, max_der, (suma_izq + suma_der)


def subarreglo_maximo(
    arr: list[int | float], bajo: int = 0, alto: int | None = None
) -> tuple[int, int, int | float]:
    """Encuentra el subarreglo de suma máxima utilizando Dividir y Vencer.

    Args:
        arr (list[int | float]): Lista de números enteros o flotantes.
        bajo (int, optional): Índice inferior de búsqueda. Por defecto 0.
        alto (int | None, optional): Índice superior. Por defecto None.

    Returns:
        tuple[int, int, int | float]: Tupla con (inicio, fin, suma_maxima).
    """
    if alto is None:
        alto = len(arr) - 1

    if bajo == alto:
        return bajo, alto, arr[bajo]

    medio = (bajo + alto) // 2

    izq_inicio, izq_fin, izq_suma = subarreglo_maximo(arr, bajo, medio)
    der_inicio, der_fin, der_suma = subarreglo_maximo(arr, medio + 1, alto)
    cruz_inicio, cruz_fin, cruz_suma = suma_cruzada(arr, bajo, medio, alto)

    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return izq_inicio, izq_fin, izq_suma
    elif der_suma >= izq_suma and der_suma >= cruz_suma:
        return der_inicio, der_fin, der_suma
    else:
        return cruz_inicio, cruz_fin, cruz_suma
