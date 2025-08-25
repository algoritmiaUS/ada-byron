# Problema D - Vales de descuento

Una cadena de supermercados quiere implantar un programa de fidelización que
recompense a sus mejores clientes del mes con vales de descuento de 10€ para
las compras del próximo mes. El número de vales a repartir cada mes, $n$, será
variable y dependerá de la estrategia comercial del supermercado. La idea es
que los clientes compitan por conseguir los $n$ vales y que un cliente sea
recompensado con un número de vales proporcional al importe mensual de sus
compras.

Como los vales son indivisibles la proporcionalidad no puede ser exacta,
entonces se decide que sean asignados a los mayores promedios (sin decimales)
de gasto por vale. Así pues, el método elegido para hacer le reparto consiste
en dividir sucesivamente el gasto realizado por cada cliente entre $1, 2,
\dots, n$ y asignar vales a los clientes correspondientes a los $n$ cocientes
más altos. En caso de empate al asignar un vale, se lo lleva el cliente que
haya gastado más. Con este método se premia con más descuentos a los clientes
con mayor gasto, sin embargo, los que menos gasten es posible que no reciban
premio.

Ayuda al gerente de los supermercados con un programa para repartir los vales
de descuento de cada mes.

## Entrada
Está compuesta por varios casos de prueba, cada uno de los cuales ocupa dos
líneas: en la primera aparece la cantidad de clientes, $m$ ($0 \leq m \leq
100.000$ ), que han hecho compras y el número de vales del mes, $n$ ($0 \leq n
\leq 1000$ ); la segunda línea contiene $m$ números no repetidos,
correspondientes al gasto realizado por cada cliente.

La entrada termina con un caso en el que no hay que hacer reparto, es decir,
$m=0$ clientes o $n=0$ vales.

## Salida
Por cada caso de prueba se escribirá una línea con el número de vales que
recibirán los respectivos clientes de la entrada.

## Entrada de ejemplo
```
3 3
100 25 50
4 5
50 20 35 132
0 0
```

## Salida de ejemplo
```
2 0 1
1 0 1 3
```