"""Experimentos de medicion y generacion de graficas para Lab 3."""
import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion."""
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(n: int) -> bool:
    """Verifica primalidad simple."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def proximo_primo(n: int) -> int:
    """Encuentra el primo mas cercano mayor o igual a n."""
    candidato = max(2, n)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def experimento_a() -> None:
    """Experimento A: Comparativa Lista vs Tabla con alfa ~ 2."""
    valores_n = [100, 500, 1000, 5000, 15000, 25000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    azar = random.Random(42)
    num_busquedas = 200

    print("Ejecutando Experimento A...")
    for n in valores_n:
        m = proximo_primo(max(5, int(n / 2)))
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        guias_set: set[int] = set()

        while len(guias_set) < n:
            g = azar.randint(10**9, 10**10 - 1)
            if g not in guias_set:
                guias_set.add(g)
                lista.insertar(g, "en bodega")
                tabla.insertar(g, "en bodega")

        # Verificacion de consistencia
        muestra = next(iter(guias_set))
        assert lista.buscar(muestra) == tabla.buscar(muestra)

        inexistentes = generar_guias_inexistentes(guias_set, num_busquedas, semilla=7)

        # Medir lista
        t0 = time.perf_counter()
        for g in inexistentes:
            lista.buscar(g)
        t_lista_medio = (time.perf_counter() - t0) / num_busquedas
        tiempos_lista.append(t_lista_medio * 1000)  # Convertir a ms

        # Medir tabla
        t0 = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        t_tabla_medio = (time.perf_counter() - t0) / num_busquedas
        tiempos_tabla.append(t_tabla_medio * 1000)  # Convertir a ms

        print(f"n={n}: Lista={t_lista_medio*1000:.4f} ms | Tabla={t_tabla_medio*1000:.6f} ms")

    # Grafica Experimento A
    os.makedirs("graficas", exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.plot(valores_n, tiempos_lista, marker="o", color="crimson", label="Lista Enlazada Θ(n)")
    plt.plot(valores_n, tiempos_tabla, marker="s", color="royalblue", label="Tabla Hash Θ(1 + α)")
    plt.title("Tiempo Medio de Búsqueda de Guías Inexistentes vs Número de Guías (n)")
    plt.xlabel("Número de Guías Almacenadas (n)")
    plt.ylabel("Tiempo Medio por Búsqueda (milisegundos)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=300)
    plt.close()
    print("Grafica graficas/lista_vs_tabla.png generada.")


def experimento_b() -> None:
    """Experimento B: Efecto del factor de carga alfa en la Tabla Hash."""
    n_fijo = 20000
    alfas = [0.25, 0.5, 1.0, 2.0, 4.0, 10.0]
    tiempos_alfa: list[float] = []

    azar = random.Random(42)
    num_busquedas = 200

    print("Ejecutando Experimento B...")
    guias_set: set[int] = set()
    while len(guias_set) < n_fijo:
        guias_set.add(azar.randint(10**9, 10**10 - 1))
    guias_lista = list(guias_set)

    inexistentes = generar_guias_inexistentes(guias_set, num_busquedas, semilla=11)

    for alfa in alfas:
        m = proximo_primo(max(2, int(n_fijo / alfa)))
        tabla = TablaHash(m)
        for g in guias_lista:
            tabla.insertar(g, "en transito")

        t0 = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        t_medio = (time.perf_counter() - t0) / num_busquedas
        tiempos_alfa.append(t_medio * 1000)
        print(f"alfa={alfa:.2f} (m={m}): Tabla={t_medio*1000:.6f} ms")

    # Grafica Experimento B
    plt.figure(figsize=(9, 5))
    plt.plot(alfas, tiempos_alfa, marker="o", color="teal", label="Tabla Hash (n = 20.000)")
    plt.title("Tiempo Medio de Búsqueda de Guías Inexistentes vs Factor de Carga (α)")
    plt.xlabel("Factor de Carga (α = n / m)")
    plt.ylabel("Tiempo Medio por Búsqueda (milisegundos)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=300)
    plt.close()
    print("Grafica graficas/tiempo_vs_alfa.png generada.")


if __name__ == "__main__":
    experimento_a()
    experimento_b()
