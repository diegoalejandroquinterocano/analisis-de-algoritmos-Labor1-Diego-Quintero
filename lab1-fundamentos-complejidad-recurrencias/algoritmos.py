"""Módulo de algoritmos de ordenamiento con conteo de comparaciones.

Implementa Insertion Sort y Merge Sort garantizando orden ascendente (menor a mayor).
"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de enteros en orden ascendente usando Insertion Sort.

    Args:
        datos (list[int]): Lista de números enteros a ordenar.

    Returns:
        tuple[list[int], int]: Lista ordenada y total de comparaciones realizadas.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] <= clave:
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

    return arr, comparaciones


def _mezclar(
    izquierda: list[int], derecha: list[int]
) -> tuple[list[int], int]:
    """Mezcla dos listas ordenadas en orden ascendente.

    Args:
        izquierda (list[int]): Sublista izquierda ordenada.
        derecha (list[int]): Sublista derecha ordenada.

    Returns:
        tuple[list[int], int]: Sublista unida y total de comparaciones.
    """
    resultado: list[int] = []
    comparaciones = 0
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de enteros en orden ascendente usando Merge Sort.

    Args:
        datos (list[int]): Lista de números enteros a ordenar.

    Returns:
        tuple[list[int], int]: Lista ordenada y total de comparaciones realizadas.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    medio = len(datos) // 2
    izq, comp_izq = merge_sort(datos[:medio])
    der, comp_der = merge_sort(datos[medio:])

    mezclada, comp_mezcla = _mezclar(izq, der)
    return mezclada, comp_izq + comp_der + comp_mezcla
