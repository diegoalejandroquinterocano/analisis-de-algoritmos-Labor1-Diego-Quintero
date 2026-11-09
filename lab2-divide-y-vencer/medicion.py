"""Módulo para medir y graficar tiempos de ejecución empíricos."""

import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempos(
    tamanos: list[int], repeticiones: int = 3, semilla: int = 42
) -> tuple[list[float], list[float]]:
    """Mide los tiempos promedio de ejecución de Fuerza Bruta y Dividir y Vencer.

    Args:
        tamanos (list[int]): Lista con las longitudes n a evaluar.
        repeticiones (int, optional): Número de repeticiones por n. Por defecto 3.
        semilla (int, optional): Semilla para reproducibilidad. Por defecto 42.

    Returns:
        tuple[list[float], list[float]]: Tiempos promedio de FB y DyV respectivamente.
    """
    random.seed(semilla)
    tiempos_fb: list[float] = []
    tiempos_dyv: list[float] = []

    for n in tamanos:
        t_fb_acum = 0.0
        t_dyv_acum = 0.0

        for _ in range(repeticiones):
            datos = [random.randint(-100, 100) for _ in range(n)]

            t0 = time.perf_counter()
            _, _, suma_fb = subarreglo_fuerza_bruta(datos)
            t1 = time.perf_counter()
            t_fb_acum += (t1 - t0)

            t0 = time.perf_counter()
            _, _, suma_dyv = subarreglo_maximo(datos)
            t1 = time.perf_counter()
            t_dyv_acum += (t1 - t0)

            assert suma_fb == suma_dyv, "Error: Discrepancia entre algoritmos"

        tiempos_fb.append(t_fb_acum / repeticiones)
        tiempos_dyv.append(t_dyv_acum / repeticiones)

    return tiempos_fb, tiempos_dyv


def graficar_resultados(
    tamanos: list[int], tiempos_fb: list[float], tiempos_dyv: list[float]
) -> None:
    """Genera y guarda la gráfica comparativa de tiempos de ejecución.

    Args:
        tamanos (list[int]): Tamaños de entrada n.
        tiempos_fb (list[float]): Tiempos medidos para Fuerza Bruta.
        tiempos_dyv (list[float]): Tiempos medidos para Dividir y Vencer.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, "r-o", label="Fuerza Bruta $\\Theta(n^2)$")
    plt.plot(tamanos, tiempos_dyv, "b-s", label="Dividir y Vencer $\\Theta(n \\log n)$")
    plt.title("Comparación Empírica: Subarreglo de Suma Máxima")
    plt.xlabel("Tamaño de la entrada ($n$)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("tiempo_vs_n.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    tams = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
    t_fb, t_dyv = medir_tiempos(tams)
    graficar_resultados(tams, t_fb, t_dyv)
    print("Gráfica tiempo_vs_n.png generada correctamente.")
