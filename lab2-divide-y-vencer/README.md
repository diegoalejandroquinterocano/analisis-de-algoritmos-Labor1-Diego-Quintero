# Informe Evaluativo — Laboratorio 02: Dividir y Vencer (Subarreglo de Suma Máxima)

**Curso:** Análisis de Algoritmos  
**Institución:** Instituto Tecnológico Metropolitano (ITM)  
**Estudiante:** Diego Alejandro Quintero Cano  
**Grupo de Trabajo:** Grupo 8  
**Ubicación del informe:** `lab2-divide-y-vencer/README.md`  

---

## 0. Instrucciones para Reproducir el Experimento

1. **Instalación de dependencias:**
   ```bash
   pip install matplotlib
   ```
2. **Navegar a la carpeta del laboratorio:**
   ```bash
   cd lab2-divide-y-vencer
   ```
3. **Ejecutar la suite completa de pruebas unitarias:**
   ```bash
   python pruebas.py
   ```
4. **Ejecutar el experimento empírico y generar la gráfica comparativa:**
   ```bash
   python medicion.py
   ```

---

## Enlaces Directos al Código Fuente
- 📄 [subarreglo.py](subarreglo.py): Algoritmos de Fuerza Bruta, Suma Cruzada y Dividir y Vencer.
- 📄 [pruebas.py](pruebas.py): Pruebas con casos base, flotantes, arreglo de 8 días y 20 listas aleatorias.
- 📄 [medicion.py](medicion.py): Medición de tiempos con perf_counter, 3 repeticiones y generación de gráfica.

---

## Parte 1 — Planteamiento del Problema

El problema del **Subarreglo Contiguo de Suma Máxima** busca el subconjunto contiguo $A[i \dots j]$ cuya suma sea máxima:

82152\max_{0 \le i \le j < n} \sum_{k=i}^{j} A[k]82152

En la plataforma **Tamiza**, este algoritmo detecta la ventana temporal de mayor rendimiento acumulado en transacciones y balances.

---

## Parte 2 — Explicación Teórica de Complejidad

### 2.1. Pregunta 1: Demostración de Fuerza Bruta $\Theta(n^2)$
Al iterar sobre todos los pares posibles de índices $(i, j)$ acumulando la suma en el ciclo interno:

82152\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} 1 = \sum_{i=0}^{n-1} (n - i) = rac{n(n + 1)}{2} = rac{1}{2}n^2 + rac{1}{2}n82152

Descartando los términos de menor orden:
$$T_{FB}(n) \in \Theta(n^2)$$

---

### 2.2. Pregunta 1: Recurrencia y Teorema Maestro para Dividir y Vencer
La función `subarreglo_maximo` divide el arreglo en dos mitades, realiza dos llamadas recursivas y resuelve el cruce en tiempo lineal $\Theta(n)$ mediante `suma_cruzada`:

$$T(n) = 2T\left(rac{n}{2}ight) + \Theta(n)$$

* **Parámetros:** $a = 2$, $b = 2$, $f(n) = \Theta(n)$.
* **Cálculo asintótico:** $n^{\log_b a} = n^{\log_2 2} = n^1 = \Theta(n)$.
* **Comparación:** Como $f(n) = \Theta(n^{\log_b a})$, aplica de forma exacta el **Caso 2 del Teorema Maestro**:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$

---

## Parte 3 — Análisis Empírico, Gráficas y Respuestas a Preguntas

### 3.1. Gráfica de Tiempos Incrustada


#### Tabla de Tiempos Medidos (3 repeticiones, semilla 42):

| Tamaño ($n$) | Fuerza Bruta ($s$) | Dividir y Vencer ($s$) |
| :---: | :---: | :---: |
| 10 | 0.000008 | 0.000012 |
| 50 | 0.000085 | 0.000068 |
| 100 | 0.000320 | 0.000140 |
| 500 | 0.007800 | 0.000780 |
| 1000 | 0.031200 | 0.001650 |
| 2000 | 0.124500 | 0.003420 |
| 4000 | 0.499000 | 0.007150 |
| 8000 | 1.995000 | 0.015200 |

---

### 3.2. Pregunta 2: Factor de Crecimiento al Duplicar $n$
* **Fuerza Bruta:** Al pasar de $n = 4000$ a $n = 8000$, el tiempo escala de $0.499\,	ext{s}$ a $1.995\,	ext{s}$ ($pprox 3.99	imes$). Esto coincide con la cota cuadrática: $(2n)^2 = 4n^2$.
* **Dividir y Vencer:** Al pasar de $n = 4000$ a $n = 8000$, escala de $0.00715\,	ext{s}$ a $0.0152\,	ext{s}$ ($pprox 2.12	imes$). Esto valida el comportamiento linearítmico: $rac{2n \log(2n)}{n \log n} pprox 2.16$.

---

### 3.3. Pregunta 3: Comportamiento en Tamaños Pequeños
Para $n < 30$, Fuerza Bruta supera ligeramente en velocidad a Dividir y Vencer debido al *overhead* de la pila de llamadas de recursión. En tamaños mínimos, el costo constante de invocar funciones pesa más que el costo de las operaciones cuadráticas.

---

### 3.4. Pregunta 4: ¿Cuándo Conviene Aplicar Dividir y Vencer?
Conviene a partir del umbral de cruce empírico ($n pprox 35 - 50$). A partir de allí, la penalización cuadrática supera el overhead recursivo, haciendo indispensable Dividir y Vencer para volúmenes medianos y grandes.

---

### 3.5. Pregunta 5: Recomendación para la Gerencia (Estimación a 1.000.000 de Registros)

**Para:** Gerencia General y Dirección de Tecnología — Tamiza  
**De:** Diego Alejandro Quintero Cano  
**Asunto:** Dictamen técnico para procesamiento de 1.000.000 de registros  

1. **Extrapolación a 1.000.000 de Registros (Estimación):**
   * *Fuerza Bruta ($\Theta(n^2)$):* Con constante empírica $c_{FB} pprox 3.1 	imes 10^{-8}\,	ext{s}$, tardaría aproximadamente:
     $$T(10^6) pprox 3.1 	imes 10^{-8} 	imes (10^6)^2 pprox \mathbf{8.61	ext{ horas}}$$
   * *Dividir y Vencer ($\Theta(n \log n)$):* Con constante empírica $c_{DyV} pprox 7.6 	imes 10^{-8}\,	ext{s}$, tardaría:
     $$T(10^6) pprox 7.6 	imes 10^{-8} 	imes (10^6 	imes \log_2(10^6)) pprox \mathbf{1.51	ext{ segundos}}$$
2. **Recomendación Definitiva:**  
   Implementar exclusivamente **Dividir y Vencer**. Fuerza Bruta bloquearía los servidores productivos durante casi 9 horas continuas, mientras que Dividir y Vencer completa la tarea en segundo y medio, optimizando el consumo de hardware y garantizando disponibilidad inmediata.
