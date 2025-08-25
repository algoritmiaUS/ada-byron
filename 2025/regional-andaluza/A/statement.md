# Problema A - Torneo de Guerreros

En el reino de Arithmancia se celebra un gran torneo de combate donde $N$
guerreros compiten en duelos 1 vs 1 hasta que solo quede un vencedor. El torneo
sigue las siguientes reglas:
1. Cada ronda, los guerreros se enfrentan en combates 1 vs 1.
2. El perdedor de cada combate es eliminado.
3. Si en una ronda el número de ganadores es impar, el mejor perdedor de la
   ronda es rescatado y avanza a la siguiente ronda.
4. El torneo continúa hasta que solo quede un guerrero como campeón.

Tu tarea es determinar cuántos combates se deben realizar en total para que el
torneo termine.

## Entrada
Como entrada tendremos múltiples líneas. La primera línea tendrá un número $T$
que indica la cantidad de torneos a celebrar.

Luego habrá $T$ línea, cada una con un único número entero $N$ ($2 \leq N \leq
10^{19}$), el número total de guerreros al inicio de ese torneo (siempre será
par).

## Salida
Debería indicar $T$ líneas, cada una con la cantidad total de combates
realizados hasta que se determine el campeón.

## Entrada de ejemplo
```
5
6
8
16
18
20
```

## Salida de ejemplo
```
6
7
15
20
21
```