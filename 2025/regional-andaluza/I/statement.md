# Problema I - Ada en el jardín secreto de Versalles

En la majestuosa residencia de Versalles, donde la realeza francesa paseaba
entre fuentes de mármol y laberintos de setos, existe un rincón especial: **El
Jardín de las Flores Encantadas**. Este jardín, diseñado en dos hileras
perfectamente simétricas, alberga flores de exquisita belleza, cada una con un
nivel único de esplendor.

Cada mañana, Ada Byron, una botánica y matemática aficionada, se adentra en
este jardín con un desafío: recolectar el máximo esplendor floral sin romper la
armonía del diseño. Así, hay reglas estrictas que debe seguir:
1. Nunca puede tomar dos flores consecutivas de la misma hilera, pues los
   jardineros reales han dispuesto que cada flor debe tener su espacio.
2. No puede tomar dos flores que estén una frente a la otra en las dos hileras,
   ya que eso desequilibraría la simetría visual que Luis XIV tanto apreciaba.

Dado un jardín de $N$ columnas, donde cada flor tiene un valor de belleza
asociado, ayuda a Ada a encontrar el camino óptimo que le permita recolectar la
mayor cantidad de esplendor floral posible.

## Entrada
La entrada consta de varios casos de prueba.

Cada caso de prueba contiene:
- Un entero $N$ ($1 \leq N \leq 10$), el número de casos de prueba.
- Por cada caso de prueba (tantos como $N$):
    - Un entero $M$ ($1 \leq M \leq 1000000$ ), el número de columnas del
      jardín.
    - Una línea con $M$ enteros representando los valores de belleza de las
      flores en la hilera superior del jardín.
    - Una línea con $M$ enteros representando los valores de belleza de las
      flores en la hilera inferior del jardín.

## Salida
Un único entero, que representa el máximo esplendor floral que Ada puede
recolectar siguiendo las reglas establecidas.

## Entrada de ejemplo
```
2
4
20 2 5 27
1 8 9 1
5
3 2 5 10 7
1 8 4 3 9
```

## Salida de ejemplo
```
56
30
```

## Explicación
Ada sigue el siguiente camino óptimo para el caso 1:
- Toma la flor de la hilera **superior** en la **columna 1** (20).
- Toma la flor de la hilera **inferior** en la **columna 3** (9).
- Salta en diagonal a la flor de la hilera **superior** en la **columna 4** (27).
**Total:** 20 + 9 + 27 = 56


Ada sigue el siguiente camino óptimo para el caso 2:
- Toma la flor de la hilera **superior** en la **columna 1** (3).
- Salta en diagonal a la flor de la hilera **inferior** en la **columna 2** (8).
- Salta a la flor de la hilera **superior** en la **columna 4** (10).
- Salta en diagonal a la flor de la hilera **inferior** en la **columna 5** (9).
**Total:** 3 + 8 + 10 + 9 = 30

## Notas y restricciones
- Se garantiza que al menos una flor podrá ser recogida.
- El recorrido debe maximizar la belleza total cumpliendo con las reglas
  impuestas por la disposición del jardín.

**¡Ayuda a Ada Byron a maravillarse con el esplendor del Jardín de Versalles!**