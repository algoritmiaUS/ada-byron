# Problema C - La biblioteca de Renatia

En la Biblioteca de Renatia, la excelencia en el estudio depende no solo del
conocimiento, sino también de la adecuada iluminación de sus puestos de
estudio. Debido a la antigüedad y compleja estructura del edificio, cada una de
sus plantas se encuentra fragmentada por gruesas paredes de piedra mágica que
impiden que la luz se propague libremente, aunque los alumnos sí que pueden
atravesarlas.

Para resolver este problema, se han fabricado unos faroles especiales. Cada
farol se puede colocar en una casilla vacía de la biblioteca y activarse en uno
de dos modos:
- **Modo horizontal:** La luz se extiende a la izquierda y derecha a lo largo
  de la misma fila, deteniéndose en cuanto se encuentra una pared o se alcanza
el borde de la planta.
- **Modo vertical:** La luz se extiende hacia arriba y hacia abajo en la misma
  columna, hasta topar con una pared o llegar al límite de la planta.

Los puestos de estudio están representados por el carácter `T`. Estos deben ser
iluminados (es decir, quedar dentro del alcance de al menos un farol) para que
los estudiantes puedan trabajar sin problemas. Las casillas vacías que no
contienen un puesto de estudio se representan con `O`, y las paredes con `X`.
Cada una de las casillas vacías es lo suficientemente grande como para poder
colocar uno o dos faroles, y los puestos de estudio poseen una mesa para
faroles, por lo que también es posible colocar hasta dos faroles en ellos. El
objetivo es determinar el mínimo número de faroles que deben colocarse para
iluminar todos los puestos de estudio.

## Entrada
La entrada comienza con una línea que contiene un entero $N$ ($1 \leq N \leq
10^6$ ), el número de casos de prueba. Cada caso de prueba se describe de la
siguiente forma:
- Una línea con dos enteros $R$ y $C$ ($1 \leq R,C \leq 10^4$ ), que
  representan el número de filas y columnas del caso de prueba,
respectivamente.
- $R$ líneas con $C$ caracteres cada una que describen la planta del caso de
  prueba. Cada carácter puede ser:
  * `X`: una pared.
  * `T`: un puesto de estudio que debe ser iluminado.
  * `O`: una casilla vacía.

## Salida
Para cada caso de prueba, imprime una única línea que contenga un entero: el
número mínimo de faroles necesarios para iluminar todos los puestos de estudio.

## Entrada de ejemplo
```
3
2 3
TOO
TOT
4 5
OOOXT
OOOXX
XXOOO
TXOOO
4 5
XXTXT
OTOXX
XXOOO
OOTOO
```

## Salida de ejemplo
```
2
2
3
```