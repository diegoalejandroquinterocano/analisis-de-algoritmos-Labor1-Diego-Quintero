"""Generadores de lotes de registros para los escenarios de Tamiza."""
import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Escenario A: Lote en orden aleatorio."""
    random.seed(semilla)
    return random.sample(range(0, 10000000), n)

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Escenario B: 98% ordenado de mayor a menor y 2% desordenado al final."""
    random.seed(semilla)
    n_98 = int(n * 0.98)
    n_2 = n - n_98
    base = sorted(random.sample(range(10000, 10000000), n_98), reverse=True)
    nuevos = random.sample(range(0, 9999), n_2)
    return base + nuevos

def generar_inverso(n: int) -> list[int]:
    """Escenario C: Orden inverso (de menor a mayor riesgo)."""
    return list(range(n))
