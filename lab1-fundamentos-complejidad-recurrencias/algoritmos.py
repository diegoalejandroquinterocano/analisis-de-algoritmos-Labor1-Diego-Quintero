"""Módulo de implementación de algoritmos de ordenamiento.

Este módulo contiene las implementaciones de Insertion Sort y Merge Sort,
incluyendo el conteo explícito de comparaciones para análisis de complejidad.
"""


def insertion_sort(lista: list) -> tuple[list, int]:
    """Ordena una lista de elementos utilizando el algoritmo Insertion Sort.

    Args:
        lista (list): Lista de elementos comparables a ordenar.

    Returns:
        tuple[list, int]: Una tupla con la lista ordenada y el número
        total de comparaciones realizadas.
    """
    arr = lista.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] < clave:
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

    return arr, comparaciones


def _mezclar(
    izquierda: list, derecha: list
) -> tuple[list, int]:
    """Función auxiliar para combinar dos subarreglos ordenados en Merge Sort.

    Args:
        izquierda (list): Subarreglo izquierdo ya ordenado.
        derecha (list): Subarreglo derecho ya ordenado.

    Returns:
        tuple[list, int]: Tupla con la lista combinada ordenada y el conteo
        de comparaciones realizadas durante la mezcla.
    """
    resultado = []
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


def merge_sort(lista: list) -> tuple[list, int]:
    """Ordena una lista de elementos utilizando el algoritmo Merge Sort.

    Args:
        lista (list): Lista de elementos comparables a ordenar.

    Returns:
        tuple[list, int]: Una tupla con la lista ordenada y el número
        total de comparaciones realizadas durante el proceso.
    """
    if len(lista) <= 1:
        return lista, 0

    medio = len(lista) // 2
    izq_ordenada, comp_izq = merge_sort(lista[:medio])
    der_ordenada, comp_der = merge_sort(lista[medio:])

    mezclada, comp_mezcla = _mezclar(izq_ordenada, der_ordenada)
    total_comparaciones = comp_izq + comp_der + comp_mezcla

    return mezclada, total_comparaciones