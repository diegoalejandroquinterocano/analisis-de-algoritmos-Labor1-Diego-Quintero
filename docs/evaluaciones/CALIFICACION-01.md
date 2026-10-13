# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Diego Alejandro Quintero Cano · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-11 23:59 · **Versión revisada:** commit `975b93f`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 10 / 25 |
| Calidad de la explicación teórica | 10 / 25 |
| Corrección de la implementación | 13 / 20 |
| Calidad del análisis de las gráficas | 6 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **43 / 100** |
| **Nota (0–5)** | **2.15** |

## 1. Corrección conceptual (10 / 25)
**Lo que hizo bien:**
- Explica bien que duplicar la velocidad del servidor solo reduce el tiempo a la mitad y que un algoritmo cuadrático sigue incumpliendo la ventana de cuatro horas.
- Incluye un segundo ejemplo propio (triage de urgencias) con cantidad de datos y restricción de tiempo.
- Menciona la tensión ética de que el orden de la lista decide a quién se atiende primero.

**Lo que puede mejorar:**
- El informe habla de una empresa de energía y de facturación de medidores, no del caso Tamiza (1.200.000 registros de tamizaje cardiovascular). Ese era el caso de clase que no debía repetirse. Los dos perjuicios y quién asume el costo se explican sobre cortes de luz, no sobre pacientes de Tamiza.
- No distingue con claridad "corrección" y "eficiencia" para Tamiza.
- El consumo de energía se calcula con valores supuestos que no salen de sus mediciones, y no se relaciona con el tiempo real del proceso.
- La obligación sobre la corrección del orden (a quién se llama primero) queda muy breve.

## 2. Calidad de la explicación teórica (10 / 25)
**Lo que hizo bien:**
- Plantea bien la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando que se cumple el caso 2.
- Muestra el código de insertion sort con el número de veces que se ejecuta cada línea.

**Lo que puede mejorar:**
- Falta por completo la Parte 3.1: no define peor caso, mejor caso y caso promedio, no dice cuál usaría para decidir y no escribe la predicción antes de medir.
- El conteo línea a línea no se suma ni se concluye la cota final de insertion sort.
- No hay tabla de complejidades (mejor, peor y promedio) para los dos algoritmos.

## 3. Corrección de la implementación (13 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida y cuentan comparaciones entre elementos. Merge sort tiene su propia mezcla recursiva y no usa `sorted()` ni `list.sort()` para ordenar.
- Los generadores usan semilla y dan valores distintos.

**Lo que puede mejorar:**
- No se declara el sentido del orden. Los algoritmos ordenan de menor a mayor, pero el escenario B se genera de mayor a menor y el C de menor a mayor. Con el código entregado, el escenario C sería el mejor caso y B no sería casi ordenado, lo contrario de lo que muestran las gráficas publicadas. Las gráficas no corresponden al código entregado.
- Los nombres de parámetros y los tipos no siguen las firmas pedidas (`lista: list` en vez de `datos: list[int]`).
- Las funciones de `datos.py` no tienen el *docstring* completo (Args y Returns) y faltan líneas en blanco entre importaciones y funciones.

## 4. Calidad del análisis de las gráficas (6 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y las curvas están en los mismos ejes.
- La gráfica `parte4_tiempo.png` muestra con claridad que insertion sort crece mucho más rápido que merge sort (cerca de 1.1 s contra casi 0 en n = 6400).

**Lo que puede mejorar:**
- Ninguna gráfica está incrustada en el informe ni se analiza. No se dice cuál escenario es el peor, el mejor y el promedio, ni se contrasta con una predicción.
- No hay conclusión sobre qué algoritmo conviene a partir de la gráfica, ni comparación con las complejidades calculadas.
- Falta el concepto técnico final (4.3): recomendación, respuesta a la compra del servidor con un dato medido, extrapolación a 1.200.000 registros declarada como estimación y una consideración distinta del tiempo.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- La carpeta `lab1-fundamentos-complejidad-recurrencias/` está en la ubicación acordada y tiene todos los archivos pedidos.
- Incluye su nombre y enlaces a los cuatro archivos de código.

**Lo que puede mejorar:**
- No hay instrucciones para reproducir los experimentos.
- Las gráficas no están incrustadas en el informe, y las partes del informe no siguen el orden y contenido pedidos (Partes 3 y 4 ausentes como secciones).
- Solo hay cuatro commits que tocan este laboratorio; se pedían al menos cinco descriptivos.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente en mis pruebas y los dos scripts corren y generan las gráficas. Pero el sentido del orden no es consistente con los escenarios.

## Para el próximo laboratorio
- Responda siempre sobre el caso del laboratorio (Tamiza) y con sus datos, no con otro caso.
- Defina un solo sentido de orden y úselo igual en algoritmos, generadores e interpretación.
- Incruste cada gráfica en el informe y escriba lo que se ve en ella.
- Complete todas las partes pedidas (3.1 y 4.3) y la tabla de complejidades.
- Agregue instrucciones de reproducción y haga commits más frecuentes y descriptivos.
