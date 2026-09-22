"""Experimento Parte 4: Comparacion de Insertion Sort vs Merge Sort en Escenario A."""
import time
import matplotlib.pyplot as plt
import os
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

os.makedirs('graficas', exist_ok=True)
tamanios = [100, 200, 400, 800, 1600, 3200, 6400]

tiempos_insertion = []
tiempos_merge = []

for n in tamanios:
    datos = generar_aleatorio(n)

    t0 = time.perf_counter()
    insertion_sort(datos)
    t1 = time.perf_counter()
    tiempos_insertion.append(t1 - t0)

    t0 = time.perf_counter()
    merge_sort(datos)
    t1 = time.perf_counter()
    tiempos_merge.append(t1 - t0)

plt.figure(figsize=(8, 5))
plt.plot(tamanios, tiempos_insertion, marker='o', label='Insertion Sort (O(n²))', color='red')
plt.plot(tamanios, tiempos_merge, marker='s', label='Merge Sort (O(n log n))', color='blue')
plt.title('Comparación de Tiempo: Insertion Sort vs Merge Sort (Escenario A)')
plt.xlabel('Tamaño de Entrada (n)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.legend(); plt.grid(True)
plt.savefig('graficas/parte4_tiempo.png')
plt.close()

print("✓ Mediciones Parte 4 finalizadas y gráfica generada.")
