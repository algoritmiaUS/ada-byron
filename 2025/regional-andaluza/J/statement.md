# Problema J - Los mineros y la extracción de cristales

Un grupo de mineros trabaja en una cueva subterránea en busca de cristales
preciosos. La cueva está representada como una cuadrícula de tamaño $N \times
M$ donde cada celda contiene una cantidad de cristales a ganar o a perder. Sin
embargo, la cueva tiene muchas restricciones que hacen que la extracción no sea
trivial.

- Los mineros comienzan en la parte superior izquierda de la cueva $(0, 0)$ y
  deben llegar a la salida en la parte inferior derecha $(N-1,M-1)$.
- Solo pueden moverse en tres direcciones: hacia abajo ( $\downarrow$ ), hacia
  la derecha ( $\rightarrow$ ) o en diagonal ( $\searrow$ ).
- Cada celda $(i,j)$ contiene una cantidad de cristales que el equipo
  recolectará al pasar por ella.

El objetivo es encontrar la ruta que maximiza la cantidad total de cristales
recolectados desde la entrada hasta la salida.

Los mineros deben elegir su ruta óptima para recolectar la mayor cantidad
posible de cristales sin salirse de los límites de la cuebva y saliendo por la
casilla $(N-1, M-1)$.

## Entrada
La primera línea contiene dos enteros $N$ y $M$ ($1 \leq N \leq M \leq 100$),
representando el número de filas y columnas de la cueva.

Luego siguen $N$ líneas, cada una con $M$ enteros $C_{n,m}$ ($-1000 \leq
C_{n,m} \leq 1000$ ), indicando la cantidad de cristales que pueden encontrar o
perder en cada celda de la cuadrícula.

## Salida
Imprimir un único número entero: la máxima cantidad de cristales que los
mineros pueden recolectar en su camino óptimo de $(0,0)$ a $(N-1,M-1)$.

## Entrada de ejemplo
```
4 4
1 3 -1 50
2 -2 4 -48
5 0 3 3
0 4 1 2
```

## Salida de ejemplo
```
16
```

## Ejemplo desarrollado
Para la siguiente cuadrícula de entrada:
```
  1  3 -1  50
  2 -2  4 -48
  5  0  3   3
  0  4  1   2
```

El camino óptimo que maximiza la suma de cristales es:
$$(0,0) \rightarrow (0,1) \rightarrow (1,2) \rightarrow (2,2) \rightarrow (2,3) \rightarrow (3,3)$$

Correspondiente a los valores $1 \rightarrow 3 \rightarrow 4 \rightarrow 3 \rightarrow 3 \rightarrow 2$

Suma total: $1+3+4+3+3+2=16$

Este es el valor total que debe imprimirse como resultado.