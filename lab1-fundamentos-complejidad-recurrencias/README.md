# Informe Evaluativo — Laboratorio 01: Fundamentos, Complejidad Algorítmica y Recurrencias

**Estudiante:** Diego Alejandro Quintero Cano  
**Institución:** Instituto Tecnológico Metropolitan (ITM)  
**Asignatura:** Análisis de Algoritmos  
**Grupo:** Grupo 8  
**Ubicación del informe:** `lab1-fundamentos-complejidad-recurrencias/README.md`  

---

## 📌 Enlaces Directos al Código Fuente
- 📄 [algoritmos.py](algoritmos.py): Implementación de *Insertion Sort* y *Merge Sort* con conteo de comparaciones.
- 📄 [datos.py](datos.py): Generadores de datos (Escenarios A, B y C) con semillas fijas para reproducibilidad.
- 📄 [parte3_casos.py](parte3_casos.py): Script de prueba para peor caso, mejor caso y caso promedio.
- 📄 [parte4_complejidad.py](parte4_complejidad.py): Experimento de medición de tiempo y generación de las tres gráficas oficiales.

---

## Parte 1 — Contexto, Restricciones Técnicas e Impactos Ético-Sociales

### 1.1. Incumplimiento de la Restricción Operativa (Ventana de Tiempo)
En el contexto de la empresa procesadora de datos de energía (plataforma Tamiza), duplicar la velocidad del servidor mediante hardware **no resuelve el problema de fondo**. 

* **El problema algorítmico:** El sistema actual utiliza un algoritmo de ordenamiento con complejidad cuadrática $\Theta(n^2)$ (*Insertion Sort* en el peor escenario). Si el volumen de datos $n$ se duplica, el tiempo de procesamiento se cuadruplica ($2^2 = 4$). Si la entrada crece 10 veces, el tiempo se multiplica por 100.
* **La restricción no negociable:** La empresa cuenta con una **ventana operativa estricta de 4 horas** (de 2:00 a.m. a 6:00 a.m.) para procesar la facturación y lectura de medidores antes del inicio de la jornada laboral. 
* **El fallo:** Cuando el volumen de clientes creció, el procesamiento pasó de tomar 3 horas a requerir más de 12 horas. Comprar un servidor del doble de velocidad solo reduce el tiempo a la mitad (6 horas), lo cual **continúa violando la restricción de 4 horas** y deja al sistema inoperativo a las 6:00 a.m. La corrección del algoritmo a $\Theta(n \log n)$ (*Merge Sort*) es la única solución técnicamente viable.

---

### 1.2. Ejemplo Propio de Sistema Crítico con Restricción Fuerte
* **Sistema:** Plataforma de Asignación de Turnos de Urgencias y Triage en una Red Hospitalaria Pública (150.000 pacientes diarios).
* **Volumen de datos:** Registros de constantes vitales y niveles de gravedad emitidos por sensores biométricos en tiempo real.
* **Restricción que se rompe:** La ventana máxima de procesamiento del algoritmo de priorización es de **2 minutos**. Si la cola de pacientes supera los 10.000 registros y el sistema utiliza un algoritmo $\Theta(n^2)$, el tiempo de cálculo de prioridades se dispara a **25 minutos**.
* **Efecto directo:** Los pacientes en estado crítico (Nivel Triage I y II) quedan en espera en la base de datos sin ser asignados a un médico, rompiendo la restricción de tiempo real y provocando colapsos en la sala de emergencias.

---

### 1.3. Dimensión Económica, Ambiental e Impacto Humano

#### A. Consumo de Energía y Huella de Carbono
Un algoritmo $\Theta(n^2)$ ejecutándose durante 12 horas diarias en servidores de alto rendimiento (TDP de 750W por procesador) consume aproximadamente $9 \text{ kWh}$ por noche. A lo largo de un año, esto equivale a $3.285 \text{ kWh}$ innecesarios por servidor. Multiplicado por una granja de servidores, este desperdicio algorítmico genera toneladas de emisiones de $\text{CO}_2$ secundarias por sobregeneración eléctrica y refrigeración industrial.

#### B. Dos Perjuicios Concretos a Personas Identificables y Responsabilidad del Costo

1. **Perjuicio 1 (Suspensión errónea e injusta del servicio eléctrico):**
   * *Descripción:* Al no finalizar el procesamiento a las 6:00 a.m., los pagos realizados por usuarios vulnerables la tarde anterior no se registran a tiempo. Las cuadrillas de corte salen a campo a las 7:00 a.m. con listas desactualizadas y cortan la luz en hogares de familias de bajos recursos o pequeños comercios.
   * *¿Quién asume el costo?:* **El usuario final** asume el costo humano y económico directo (pérdida de alimentos, costo de reconexión), mientras que **la empresa distribuidora** asume sanciones regulatorias.

2. **Perjuicio 2 (Sobrecargo financiero y cobro de mora a usuarios bancarizados):**
   * *Descripción:* Los procesos de débito automático aplican recargos por mora debido a que el archivo de conciliación bancaria no se generó dentro de la ventana nocturna.
   * *¿Quién asume el costo?:* **El cliente**, quien sufre cobros indebidos y bloqueos en su historial crediticio, teniendo que realizar trámites presenciales de reclamo.

---

### 1.4. Tensión Ética sobre el Orden de la Lista
En sistemas de servicios públicos o asignación de subsidios, el orden en el que se procesa una lista no es un detalle técnico menor:
* Si el algoritmo de ordenamiento es **inestable** o prioriza por el orden de llegada en memoria sin criterio social, los usuarios procesados al final de la lista quedan sistemáticamente excluidos de las ventanas de atención diaria.
* Existe la obligación ética de implementar algoritmos **estables y justos**, donde el criterio de ordenamiento garantice equidad y transparencia.

---

## Parte 2 — Explicación Teórica y Análisis Formal

### 2.1. Recurrencia y Solución mediante el Método Maestro
Para *Merge Sort*, la ecuación de recurrencia que modela su tiempo de ejecución es:

$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

#### Desglose de Términos:
* **$2T(n/2)$ (Parte Recursiva):** El algoritmo divide el arreglo original de tamaño $n$ en dos subproblemas independientes de tamaño $n/2$ (mitad izquierda y mitad derecha).
* **$\Theta(n)$ (Parte No Recursiva / Combinar):** Corresponde al costo de la función `_mezclar()`, la cual realiza un barrido lineal comparando elemento a elemento ambas mitades para unirlas en orden.

#### Aplicación Rigurosa del Método Maestro:
El Teorema Maestro aplica a recurrencias de la forma $T(n) = aT(n/b) + f(n)$.
* Identificación de parámetros: $a = 2$, $b = 2$, $f(n) = \Theta(n)$.
* Cálculo del término crítico: $n^{\log_b a} = n^{\log_2 2} = n^1 = \Theta(n)$.

#### Comprobación de la Condición del Caso:
Comparamos $f(n)$ con $n^{\log_b a}$: $\Theta(n) = \Theta(n)$.

Dado que $f(n) = \Theta(n^{\log_b a})$, se cumple exactamente la condición del **Caso 2 del Método Maestro**.

Por la formulación del Caso 2:
$$T(n) = \Theta(n^{\log_b a} \cdot \log n) = \Theta(n \log n)$$

---

### 2.2. Conteo de Operaciones Línea a Línea de Insertion Sort

```python
def insertion_sort(lista: list) -> tuple[list, int]:
    arr = lista.copy()                           # Costo c1,  Se ejecuta 1 vez
    comparaciones = 0                             # Costo c2,  Se ejecuta 1 vez
    n = len(arr)                                  # Costo c3,  Se ejecuta 1 vez
    for i in range(1, n):                         # Costo c4,  Se ejecuta n veces
        clave = arr[i]                            # Costo c5,  Se ejecuta (n - 1) veces
        j = i - 1                                 # Costo c6,  Se ejecuta (n - 1) veces
        while j >= 0:                             # Costo c7,  Se ejecuta sum(i=1..n-1) (i + 1)
            comparaciones += 1                    # Costo c8,  Se ejecuta sum(i=1..n-1) i
            if arr[j] < clave:                    # Costo c9,  Se ejecuta sum(i=1..n-1) i
                break
            arr[j + 1] = arr[j]                   # Costo c10, Se ejecuta sum(i=1..n-1) i
            j -= 1                                # Costo c11, Se ejecuta sum(i=1..n-1) i
        arr[j + 1] = clave                        # Costo c12, Se ejecuta (n - 1) veces
    return arr, comparaciones                     # Costo c13, Se ejecuta 1 vez