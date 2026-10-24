# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Diego Alejandro Quintero Cano · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `dc55a54`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 0 / 20 |
| Calidad de la explicación teórica | 0 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 10 / 25 |
| Documentación y organización del informe | 2 / 10 |
| **Total** | **33 / 100** |
| **Nota (0–5)** | **1.65** |

## 1. Corrección conceptual (0 / 20)
**Lo lograron:** nada que calificar en este criterio.
**Lo que puede mejorar:**
- El `README.md` quedó cortado: termina en la instrucción `pip install matplotlib`. No aparecen las preguntas 3, 4 y 5 de la Parte 3 (tamaños pequeños, cuándo conviene dividir y recomendación para la gerente con la estimación a 1.000.000 de registros).
- Como el informe es el único texto que se califica, sin esas respuestas no hay nada que evaluar.

## 2. Calidad de la explicación teórica (0 / 20)
**Lo que puede mejorar:**
- Falta la pregunta 1: la recurrencia de `subarreglo_maximo`, su solución con el método maestro y la explicación de por qué la fuerza bruta es `Θ(n²)`.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones (`subarreglo_fuerza_bruta`, `suma_cruzada`, `subarreglo_maximo`) dan la suma correcta en todos los casos probados, incluida la serie de ocho días (17).
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista recibida.
- `pruebas.py` cubre los casos pedidos y 20 listas aleatorias con semilla fija; todas las pruebas pasan.
**Lo que puede mejorar:**
- Faltan dos líneas en blanco entre funciones en `subarreglo.py`, `medicion.py` y `pruebas.py`.
- `medir_tiempos` no tiene *type hints* ni *docstring* estilo Google.

## 4. Calidad del análisis de las gráficas (10 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` existe, con las dos curvas en los mismos ejes, título, ejes rotulados y leyenda, y cubre siete tamaños (de 10 a 8000).
- La medición usa semilla fija, `time.perf_counter()`, repite tres veces y comprueba que ambos algoritmos den la misma suma.
**Lo que puede mejorar:**
- No hay análisis: falta la pregunta 2 (factor de crecimiento al duplicar `n` para cada algoritmo y comparación con `Θ(n²)` y `Θ(n log n)`).
- La gráfica no está incrustada en el `README.md`, así que no se ve en el informe.

## 5. Documentación y organización del informe (2 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` está en la ubicación y con los archivos correctos, y el informe trae su nombre.
**Lo que puede mejorar:**
- El informe está incompleto: no tiene las Partes 1, 2 y 3, no incrusta la gráfica y no enlaza `subarreglo.py`, `pruebas.py` ni `medicion.py`.
- Las instrucciones de reproducción no incluyen los comandos para correr las pruebas y la medición.
- Solo hay dos commits que tocan este laboratorio (se pedían al menos tres).

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en todos los tamaños y `medicion.py` genera la gráfica sin errores.

## Para el próximo laboratorio
- Verifique en GitHub que el `README.md` se vea completo antes de entregar; el de este laboratorio se cortó a mitad.
- Responda todas las preguntas del análisis con datos de su propia gráfica y tabla de tiempos.
- Incruste las gráficas y enlace el código de cada parte.
- Haga varios commits con mensajes descriptivos mientras avanza.
- Deje dos líneas en blanco entre funciones y agregue *type hints* y *docstrings* (con Args y Returns) a todas las funciones.
