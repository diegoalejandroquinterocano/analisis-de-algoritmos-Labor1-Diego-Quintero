"""Experimento Parte 3: Medicion de Insertion Sort en Escenarios A, B y C."""
import time
import matplotlib.pyplot as plt
import os
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

os.makedirs('graficas', exist_ok=True)
tamanios = [100, 200, 400, 800, 1600, 3200, 6400]

comp_A, comp_B, comp_C = [], [], []
tiempos_A, tiempos_B, tiempos_C = [], [], []

for n in tamanios:
    # Escenario A
    d_A = generar_aleatorio(n)
    t0 = time.perf_counter()
    _, c = insertion_sort(d_A)
    t1 = time.perf_counter()
    comp_A.append(c); tiempos_A.append(t1 - t0)

    # Escenario B
    d_B = generar_casi_ordenado(n)
    t0 = time.perf_counter()
    _, c = insertion_sort(d_B)
    t1 = time.perf_counter()
    comp_B.append(c); tiempos_B.append(t1 - t0)

    # Escenario C
    d_C = generar_inverso(n)
    t0 = time.perf_counter()
    _, c = insertion_sort(d_C)
    t1 = time.perf_counter()
    comp_C.append(c); tiempos_C.append(t1 - t0)

# Grafica Comparaciones
plt.figure(figsize=(8, 5))
plt.plot(tamanios, comp_A, marker='o', label='Escenario A (Aleatorio)')
plt.plot(tamanios, comp_B, marker='s', label='Escenario B (Casi ordenado)')
plt.plot(tamanios, comp_C, marker='^', label='Escenario C (Inverso)')
plt.title('Insertion Sort: Comparaciones vs Tamaño de Entrada')
plt.xlabel('Tamaño de Entrada (n)')
plt.ylabel('Número de Comparaciones')
plt.legend(); plt.grid(True)
plt.savefig('graficas/parte3_comparaciones.png')
plt.close()

# Grafica Tiempos
plt.figure(figsize=(8, 5))
plt.plot(tamanios, tiempos_A, marker='o', label='Escenario A (Aleatorio)')
plt.plot(tamanios, tiempos_B, marker='s', label='Escenario B (Casi ordenado)')
plt.plot(tamanios, tiempos_C, marker='^', label='Escenario C (Inverso)')
plt.title('Insertion Sort: Tiempo de Ejecucion vs Tamaño de Entrada')
plt.xlabel('Tamaño de Entrada (n)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.legend(); plt.grid(True)
plt.savefig('graficas/parte3_tiempo.png')
plt.close()

print("✓ Mediciones Parte 3 finalizadas y gráficas generadas.")
