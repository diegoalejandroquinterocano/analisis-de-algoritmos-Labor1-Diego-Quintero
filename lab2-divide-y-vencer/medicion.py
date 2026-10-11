"""Medicion de tiempos de ejecucion y generacion de la grafica."""

import time
import random
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def medir_tiempos():
    # Tamanos de entrada segun los requisitos (dos menores de 100, uno >= 4000)
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    
    tiempos_fb = []
    tiempos_dv = []
    
    random.seed(42) # Semilla fija para reproducibilidad
    
    print("Iniciando mediciones de tiempo...")
    for n in tamanos:
        # Generar lista aleatoria (misma para ambos algoritmos)
        valores = [random.randint(-100, 100) for _ in range(n)]
        
        # 1. Medir Fuerza Bruta
        # Repetimos 3 veces y tomamos el minimo/promedio para evitar el ruido del SO
        t_fb_total = 0
        for _ in range(3):
            inicio_fb = time.perf_counter()
            res_fb = subarreglo_fuerza_bruta(valores)
            fin_fb = time.perf_counter()
            t_fb_total += (fin_fb - inicio_fb)
        tiempo_fb_promedio = t_fb_total / 3
        tiempos_fb.append(tiempo_fb_promedio)
        
        # 2. Medir Divide y Venceras
        t_dv_total = 0
        for _ in range(3):
            inicio_dv = time.perf_counter()
            res_dv = subarreglo_maximo(valores, 0, n - 1)
            fin_dv = time.perf_counter()
            t_dv_total += (fin_dv - inicio_dv)
        tiempo_dv_promedio = t_dv_total / 3
        tiempos_dv.append(tiempo_dv_promedio)
        
        # Verificar que den la misma suma en el experimento
        assert res_fb[2] == res_dv[2], f"Error en n={n}: FB dio {res_fb[2]}, DV dio {res_dv[2]}"
        print(f"Tamano {n:4d}: FB = {tiempo_fb_promedio:.6f} s | DV = {tiempo_dv_promedio:.6f} s")

    # 3. Generar la Grafica
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, marker='o', label='Fuerza Bruta O(n^2)')
    plt.plot(tamanos, tiempos_dv, marker='x', label='Divide y Venceras O(n log n)')
    
    plt.title('Comparacion de Tiempos: Subarreglo Maximo')
    plt.xlabel('Tamano de entrada (n)')
    plt.ylabel('Tiempo de ejecucion (segundos)')
    plt.legend()
    plt.grid(True)
    
    # Guardar en la carpeta graficas/
    plt.savefig('graficas/tiempo_vs_n.png')
    print("Grafica generada y guardada en 'graficas/tiempo_vs_n.png'.")

if __name__ == "__main__":
    medir_tiempos()