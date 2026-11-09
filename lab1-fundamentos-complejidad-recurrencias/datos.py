"""Generadores de datos para pruebas de algoritmos de ordenamiento.

Todos los escenarios asumen un orden objetivo ASCENDENTE (de menor a mayor).
"""

import random


def generar_escenario_a(n: int, semilla: int = 42) -> list[int]:
    """Genera el peor caso para orden ascendente: datos en orden descendente.

    Args:
        n (int): Cantidad de elementos a generar.
        semilla (int, optional): Semilla para reproducibilidad. Valor por defecto: 42.

    Returns:
        list[int]: Lista de enteros ordenados estrictamente de mayor a menor.
    """
    return list(range(n, 0, -1))


def generar_escenario_b(n: int, porcentaje_desorden: float = 0.05, semilla: int = 42) -> list[int]:
    """Genera el mejor caso/casi ordenado: datos casi en orden ascendente con pocas inversiones.

    Args:
        n (int): Cantidad de elementos a generar.
        porcentaje_desorden (float, optional): Proporción de elementos fuera de posición.
        semilla (int, optional): Semilla para reproducibilidad. Valor por defecto: 42.

    Returns:
        list[int]: Lista de enteros casi ordenados de menor a mayor.
    """
    random.seed(semilla)
    datos = list(range(1, n + 1))
    intercambios = int(n * porcentaje_desorden)
    for _ in range(intercambios):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        datos[i], datos[j] = datos[j], datos[i]
    return datos


def generar_escenario_c(n: int, semilla: int = 42) -> list[int]:
    """Genera el caso promedio: datos en orden totalmente aleatorio.

    Args:
        n (int): Cantidad de elementos a generar.
        semilla (int, optional): Semilla para reproducibilidad. Valor por defecto: 42.

    Returns:
        list[int]: Lista de enteros ordenados aleatoriamente.
    """
    random.seed(semilla)
    datos = list(range(1, n + 1))
    random.shuffle(datos)
    return datos
