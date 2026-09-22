"""
Diego Alejandro Quintero Cano Grupo lunes 6 a 10 am 
Laboratorio 1: Fundamentos de complejidad y recurrencias
Curso: Análisis de Algoritmos - ITM
Autores: Grupo 8
"""

import time
import random
import os
import matplotlib.pyplot as plt

# Crear carpeta para guardar gráficas
os.makedirs('graficas', exist_ok=True)

# ---------------------------------------------------------
# 1. IMPLEMENTACIÓN DE ALGORITMOS
# ---------------------------------------------------------

def insertion_sort(arr):
    A = arr.copy()
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---------------------------------------------------------
# 2. GENERACIÓN DE CASOS DE ENTRADA
# ---------------------------------------------------------

def generar_datos(n, tipo='promedio'):
    if tipo == 'mejor':
        return list(range(n))
    elif tipo == 'peor':
        return list(range(n, 0, -1))
    else:
        return [random.randint(0, 10000) for _ in range(n)]

# ---------------------------------------------------------
# 3. EXPERIMENTACIÓN Y MEDICIÓN DE TIEMPOS
# ---------------------------------------------------------

def medir_tiempo(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return fin - inicio

def ejecutar_experimentos():
    tamanios = [10, 50, 100, 200, 400, 800, 1200, 1600, 2000]
    
    tiempos_insertion_peor = []
    tiempos_insertion_prom = []
    tiempos_insertion_mejor = []
    tiempos_merge_prom = []

    for n in tamanios:
        d_peor = generar_datos(n, 'peor')
        tiempos_insertion_peor.append(medir_tiempo(insertion_sort, d_peor))

        d_prom = generar_datos(n, 'promedio')
        tiempos_insertion_prom.append(medir_tiempo(insertion_sort, d_prom))

        d_mejor = generar_datos(n, 'mejor')
        tiempos_insertion_mejor.append(medir_tiempo(insertion_sort, d_mejor))

        tiempos_merge_prom.append(medir_tiempo(merge_sort, d_prom))

    # ---------------------------------------------------------
    # 4. GENERACIÓN DE GRÁFICAS
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_insertion_peor, label='Insertion Sort (Peor Caso)', color='red', marker='o')
    plt.plot(tamanios, tiempos_insertion_prom, label='Insertion Sort (Caso Promedio)', color='orange', marker='s')
    plt.plot(tamanios, tiempos_insertion_mejor, label='Insertion Sort (Mejor Caso)', color='green', marker='^')
    plt.plot(tamanios, tiempos_merge_prom, label='Merge Sort (Caso Promedio)', color='blue', marker='d')

    plt.title('Comparación de Tiempos de Ejecución: Insertion Sort vs Merge Sort')
    plt.xlabel('Tamaño de la entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/comparativa_tiempos.png')
    print("✓ Experimento finalizado y gráfica guardada en 'graficas/comparativa_tiempos.png'")

if __name__ == '__main__':
    ejecutar_experimentos()