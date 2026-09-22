"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion de mayor a menor."""
    A = datos.copy()
    comparaciones = 0
    for i in range(1, len(A)):
        clave = A[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if A[j] < clave:  # De mayor a menor
                A[j + 1] = A[j]
                j -= 1
            else:
                break
        A[j + 1] = clave
    return A, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla de mayor a menor."""
    if len(datos) <= 1:
        return datos.copy(), 0

    mid = len(datos) // 2
    left, comp_left = merge_sort(datos[:mid])
    right, comp_right = merge_sort(datos[mid:])

    resultado, comp_merge = _mezclar(left, right)
    return resultado, comp_left + comp_right + comp_merge

def _mezclar(left: list[int], right: list[int]) -> tuple[list[int], int]:
    resultado = []
    i = j = 0
    comparaciones = 0
    while i < len(left) and j < len(right):
        comparaciones += 1
        if left[i] >= right[j]:  # De mayor a menor
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado, comparaciones
