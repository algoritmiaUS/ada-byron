

## **La receta definitiva**

¡Lo has logrado! Después de años de pruebas, experimentos y alguna que otra catástrofe culinaria, has descubierto **la receta definitiva**; un plato tan delicioso que podría cambiar el mundo de la gastronomía para siempre. Sin embargo, hay un pequeño problema: para prepararlo, necesitas una gran variedad de ingredientes, y cada uno se encuentra en un almacén distinto.

Tu restaurante está ubicado en la coordenada $(X, Y)$, mientras que los almacenes con los ingredientes están dispersos en distintas posiciones $(X_i, Y_i)$. Para optimizar la logística, puedes juntar ingredientes procedentes de distintos almacenes en uno solo y transportarlos juntos el resto del trayecto.

El problema es que se nos ha echado el tiempo encima. Los repartidores están dispuestos a hacer horas extra, pero para mantenerlos motivados, queremos diseñar una ruta que **les ofrezca buenas vistas**, ya que cada trayecto entre almacenes o hacia el restaurante tiene un nivel de satisfacción asociado. Para que acepten el encargo, necesitamos alcanzar al menos un nivel de satisfacción total $S$.

Pero hay otro factor a considerar: como empresa ecologista, queremos minimizar el impacto ambiental del transporte, por lo que nos vamos a asegurar de hacer el mínimo número de trayectos posible y los organizaremos de forma que el más largo de todos ellos sea lo más corto posible.


### **Entrada**

  - La primera línea contiene el número de casos de prueba $T$.
  - La segunda línea está formada por tres enteros $N$, $X$ e $Y$, donde $N$ es el número de almacenes.
  - La tercera línea tiene un entero $S$ indicando el nivel mínimo de satisfacción requerido.
  - Las siguientes $N$ líneas están formadas por dos enteros $X_i$ e $Y_i$, que representan la posición de cada almacén.
  - La línea siguiente contiene un entero $M$, el número de conexiones entre almacenes o entre un almacén y el restaurante que tienen buenas vistas.
  - Las siguientes $M$ líneas tienen tres enteros $A$, $B$ y $V$, que representan:
      - Una conexión entre el nodo $A$ y el nodo $B$ (donde los almacenes están numerados de $1$ a $N$ y el restaurante es el nodo $0$).
      - El nivel $V$ de satisfacción de ese trayecto, gracias a sus buenas vistas.

**Importante**: Es posible realizar el trayecto entre cualquier par de puntos, independientemente de si hay buenas vistas o no. Utilizamos la distancia euclídea para medir la longitud.


### **Salida**

Una única línea por cada caso de prueba con un número (redondeado a dos cifras decimales) que indica la longitud del trayecto más largo dentro de la mejor ruta logística posible que cumple con el nivel de satisfacción mínimo $S$. Si no es posible alcanzar dicho nivel de satisfacción con el mínimo de trayectos posible, imprime $-1.00$.

**Importante**: Los valores de la salida deben incluir _exactamente_ dos cifras decimales.


### **Límites**

  - $1 \leq T, N \leq 100$
  - $0 \leq X, Y, X_i, Y_i \leq 10^4$
  - $1 \leq M \leq N(N+1)/2$
  - $0 \leq V \leq 10^6$
  - $0 \leq S \leq 10^9$


### **Ejemplo**


#### **Entrada**

```
2
1 0 0
1
1 1
1
0 1 1
3 14 15
30
92 65
35 89
79 32
6
0 1 3
0 2 8
0 3 4
1 2 6
1 3 2
3 3 6
```


#### **Salida esperada**

```
1.41
-1.00
```
