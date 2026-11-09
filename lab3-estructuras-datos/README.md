# Informe Evaluativo — Laboratorio 03: Estructuras de Datos

**Curso:** Análisis de Algoritmos  
**Institución:** Instituto Tecnológico Metropolitano (ITM)  
**Estudiante:** Diego Alejandro Quintero Cano  
**Grupo de Trabajo:** Grupo 8  
**Ubicación del informe:** `lab3-estructuras-datos/README.md`  

---

## 0. Instrucciones para Reproducir el Experimento

1. **Instalación de dependencias:**
   ```bash
   pip install matplotlib
   ```
2. **Navegar a la carpeta del laboratorio:**
   ```bash
   cd lab3-estructuras-datos
   ```
3. **Ejecutar la suite completa de pruebas unitarias:**
   ```bash
   python pruebas.py
   ```
4. **Ejecutar las mediciones empíricas y generar las gráficas:**
   ```bash
   python medicion.py
   ```

---

## Parte 1 — Implementación y Verificación de Estructuras

Enlaces directos al código fuente implementado:
- 📄 [estructuras.py](estructuras.py): Implementación formal de `Nodo`, `ListaEnlazada` con inserción $\Theta(1)$ al inicio y búsqueda iterativa con ciclo `while`, junto con `TablaHash` con encadenamiento y función hash por división ($h(k) = k \pmod m$).
- 📄 [pruebas.py](pruebas.py): Suite de pruebas unitarias implementadas con aserciones rigurosas.

### Casos cubiertos en la verificación:
1. **Búsqueda exitosa e infructuosa:** Se comprobó que ambas estructuras devuelven el estado correcto ante guías presentes y `None` ante claves inexistentes.
2. **Colisión forzada:** Con $m = 7$, las claves $10, 24, 17$ caen en la casilla 3 ($10 \pmod 7 = 3$, $24 \pmod 7 = 3$, $17 \pmod 7 = 3$). Se verificó que las tres conviven en la lista de la casilla 3, con tamaño 3, recuperan sus estados y el factor de carga es exactamente $3/7$.
3. **Equivalencia sobre 20 colecciones aleatorias:** Se validó que ante 20 conjuntos aleatorios de datos, la lista y la tabla responden con idénticos valores tanto para guías existentes como inexistentes.

---

## Parte 2 — Análisis Empírico y Gráficas

Enlace al script de medición:
- 📄 [medicion.py](medicion.py): Rutinas cronometradas con `time.perf_counter()`, 200 búsquedas infructuosas por punto y selección de módulos primos cercanos a $n / 2$.

### Gráfica 1 — Comparativa Lista frente a Tabla (Experimento A)


*Parámetros:* Evaluado para $n \in [100, 500, 1000, 5000, 15000, 25000]$, con $m$ primo más cercano a $n / 2$ ($lpha pprox 2$).

### Gráfica 2 — Efecto del Factor de Carga $lpha$ (Experimento B)


*Parámetros:* $n = 20.000$ constante, variando $m$ primo para evaluar $lpha \in [0.25, 0.5, 1.0, 2.0, 4.0, 10.0]$.

---

## Parte 3 — Análisis Teórico y Toma de Decisiones

### 1. Costo Teórico
En una búsqueda infructuosa dentro de la lista enlazada simple, al no tener orden interno, es obligatorio comparar la clave buscada contra todos y cada uno de los $n$ nodos hasta alcanzar el puntero final `None`, lo que toma exactamente $n$ comparaciones, es decir, $\Theta(n)$.  
En la tabla hash con encadenamiento, calcular la casilla toma tiempo constante $\Theta(1)$ y la longitud esperada de la lista enlazada de esa casilla corresponde al factor de carga $lpha = n/m$. Por tanto, el costo promedio de búsqueda infructuosa es $\Theta(1 + lpha)$. Este resultado se fundamenta en el **supuesto de dispersión uniforme simple (SUHA)**, el cual establece que cada clave tiene la misma probabilidad de ser asignada a cualquiera de las $m$ casillas, de manera independiente a las demás. Si este supuesto falla y todas las claves caen en la misma casilla, la tabla degenera por completo en una lista enlazada simple, degradando la búsqueda al peor caso de $\Theta(n)$.

### 2. Lo Medido contra lo Esperado
En la primera gráfica (`lista_vs_tabla.png`), al pasar de $n = 5.000$ a $n = 15.000$ (un incremento de $3	imes$), el tiempo medio de búsqueda en la lista enlazada escala en una proporción directa cercana a $3	imes$, validando de forma clara la complejidad asintótica $\Theta(n)$. En contraste, la curva de la tabla hash permanece prácticamente horizontal y pegada al eje, midiendo tiempos en el orden de microsegundos independientemente del tamaño $n$, ya que se mantuvo $lpha pprox 2$, lo cual confirma la cota teórica $\Theta(1 + lpha) = \Theta(1)$.  
En la segunda gráfica (`tiempo_vs_alfa.png`), con $n = 20.000$ fijo, a medida que $lpha$ aumenta de $0.25$ hasta $10.0$, el tiempo de búsqueda exhibe un crecimiento estrictamente lineal respecto al aumento del tamaño promedio de las listas de colisión, lo que coincide con la predicción teórica $\Theta(1 + lpha)$.

### 3. Explicación de Colisiones
Una colisión ocurre cuando dos o más claves distintas producen el mismo índice al evaluarse en la función hash: $h(k_1) = h(k_2)$ con $k_1 
eq k_2$. Por el Principio del Palomar y el efecto de la Paradoja del Cumpleaños, las colisiones son inevitables incluso si la tabla tiene más casillas que guías ($m > n$), debido a que las funciones hash dispersan sobre un rango finito claves provenientes de un universo mucho mayor.  
En el **encadenamiento**, cada casilla contiene una lista enlazada independiente; tiene como ventaja que la tabla nunca se satura ($lpha$ puede ser superior a 1) y borrar un nodo es trivial, pero tiene como costo el uso de memoria adicional para punteros y menor aprovechamiento de la memoria caché. En el **direccionamiento abierto**, todos los elementos se almacenan directamente en el arreglo mediante secuencias de sondeo; ofrece mejor aprovechamiento de memoria y caché al no usar punteros, pero exige estrictamente $lpha < 1$, requiere marcas especiales para eliminaciones y sufre de degradación por agrupamiento (*clustering*).  
*Ejemplo:* Con $m = 7$, las claves $10, 24, 17$ generan $10 \pmod 7 = 3$, $24 \pmod 7 = 3$ y $17 \pmod 7 = 3$. El encadenamiento inserta las tres guías en la lista enlazada de la casilla 3, permitiendo consultar cualquiera de ellas sin afectar las otras casillas.

### 4. Tabla Hash frente a Árbol de Búsqueda Binario
La tabla hash **no sirve** para el monitoreo por rango ("guías entre $X$ y $Y$"). Como la función hash busca intencionalmente dispersar las claves de forma uniforme y no ordenada, se pierde cualquier relación de orden entre elementos contiguos. Responder a un rango obligaría a recorrer todas las casillas y todas sus listas, teniendo un costo prohibitivo de $\Theta(m + n)$.  
Un Árbol de Búsqueda Binario (BST) preserva la propiedad de orden simétrico, permitiendo realizar recorridos acotados en orden para resolver rangos en tiempo $\Theta(h + k)$, donde $h$ es la altura del árbol y $k$ la cantidad de elementos en el rango.  
Si las $400.000$ guías llegaran ya ordenadas y se insertaran en un BST sin autobalanceo, cada elemento nuevo se insertará como hijo derecho del anterior, degenerando en una lista enlazada simple de altura $h = 400.000$. En ese caso, una búsqueda requeriría hasta $400.000$ comparaciones ($\Theta(n)$). En cambio, en un árbol autobalanceado (AVL o Red-Black), la altura máxima queda acotada a $h = \lceil \log_2(400.000) ceil pprox 19$, resolviendo cualquier búsqueda en máximo 19 comparaciones ($\Theta(\log n)$).

### 5. Concepto Técnico para la Jefa de Operaciones
Para resolver de forma óptima los dos requerimientos operativos, se recomienda implementar una **arquitectura híbrida de indexación doble**:
1. **Tabla Hash con encadenamiento** dimensionada con $lpha pprox 0.75$ ($m pprox 550.000$ casillas con número primo) para la consulta puntual del call center, garantizando respuestas casi instantáneas en $\Theta(1)$.
2. **Árbol Autobalanceado (AVL o Red-Black)** sobre los mismos registros para atender el monitoreo por rango de los supervisores en $\Theta(\log n + k)$.

**Estimación a 5.000.000 de envíos:**  
*Declaración de estimación:* A partir de la tasa empírica observada en nuestras mediciones para la lista enlazada ($c_{	ext{lista}} pprox 6.4 	imes 10^{-5}$ ms por nodo inspeccionado al recorrer toda la colección en búsquedas infructuosas), estimamos que una consulta infructuosa en la lista enlazada para $5.000.000$ de envíos tardaría:
$$T_{	ext{lista}}(5 	imes 10^6) pprox (6.4 	imes 10^{-5}\,	ext{ms}) 	imes (5 	imes 10^6) pprox 320.000\,	ext{ms} pprox \mathbf{5.33	ext{ minutos}}$$
Un cliente en llamada telefónica colgará inevitablemente ante semejante tiempo de bloqueo.  
Por su parte, en la tabla hash, manteniendo el redimensionamiento con factor de carga controlado ($lpha pprox 1.5$ asignando $m pprox 3.333.337$ casillas), el costo depende únicamente de evaluar la función hash y recorrer una cadena promedio de 1 a 2 nodos:
$$T_{	ext{tabla}}(5 	imes 10^6) pprox \mathbf{0.0008	ext{ ms (menos de 1 microsegundo)}}$$
La migración a la tabla hash erradica los tiempos muertos del call center y garantiza disponibilidad operativa absoluta.
