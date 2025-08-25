# Problema F - Juego de cifras

Utilizando cada una de las cifras del conjunto $\left\lbrace 1, 2, 3, 4
\right\rbrace$ exactamente una vez, y haciendo uso de las cuatro operaciones
aritméticas $`(+, -, *, /)`$ y los paréntesis, es posible formar diferentes
números enteros positivos. Por ejemplo:
```math
\begin{align*}
  &8 = (4 * (1 + 3)) / 2 \\
  &14 = 4 * (3 + 1 / 2) \quad\quad\textbf{Observe que puede usar fracciones} \\
  &19 = 4 * (2 + 3) - 1 \\
  &36 = 3 * 4 * (2 + 1)
\end{align*}
```

Tenga en cuenta que las concatenaciones de los dígitos, como $12+34$, no están
permitidas. Utilizando el conjunto $\left\lbrace 1, 2, 3, 4 \right\rbrace$ es
posible obtener treinta y un números objetivos distintos.

El objetivo es, dado un conjunto de entrada, devolver el número de valores
enteros expresables mayores que cero.

## Entrada
La entrada puede constar de varios casos de prueba. La primera línea
corresponde al número de ellos.

Cada caso de prueba contiene una línea, con números mayores que cero, separados
por un espacio. Cada línea puede tener un número diferente de cifras.

## Salida
La salida debe contener una línea para cada caso de prueba con el número de
valores enteros expresables mayores que cero.

## Entrada de ejemplo
```
3
1 2 3 4
2 5 7 9
1 2 5 8
```

## Salida de ejemplo
```
31
104
70
```