# Problema H - Estrategia estelar

Tras varios siglos de desavenencias las tres grandes civilizaciones intergalácticas -los Terranis, los Zergerianos y los Protoses- han firmado una paz. Pero como lo bueno no podía durar mucho ha aparecido una enorme flota de la antigua civilización Xelgariana que amenaza la existencia del universo conocido. Para evitar ser destruidas, las flotas deben estar en constante movimiento con una mecánica un tanto peculiar que se explica luego. Además, sólo causan daño a la flota Xelgariana si todos atacan a la vez en posiciones concretas. Hoy precisamente se ha dado esa sincronización y han conseguido causar un daño significativo, pero no destruirlo del todo. ¿Cuál será el siguiente momento en el que se produzca la misma sincronización?

## Mecánica del movimiento
Cada flota tiene:
- Una posición en el espacio tridimensional $(x,y,z)$.
- Una velocidad en cada eje $(v_x,v_y,v_z)$.
- Una regla de actualización de velocidad que depende de la comparación de posiciones con las otras flotas.

En cada día:
- Se ajustan las velocidades en cada eje de forma independiente:
    - Si en un eje una flota tiene una coordenada menor que otra, su velocidad
      en ese eje aumenta en 1, y la otra disminuye en 1.
    - Si en un eje una flota tiene una coordenada mayor que otra, su velocidad
      en ese eje disminuye en 1, y la otra aumenta en 1.
    - Si las dos flotas tienen la misma coordenada en un eje, sus velocidades
      no cambian entre ellas.
- Se actualizan las posiciones sumando la velocidad actual a la posición en
  cada eje.

Este proceso continúa hasta que las tres flotas regresen simultáneamente a su
estado inicial (misma posición y velocidades actuales a 0).

## Entrada
Como entrada tendremos una primera línea con un número $N$ que indica
diferentes posibles posiciones iniciales de las flotas.

Luego habrá $N$ líneas con 9 valores, 3 por civilización, que representan su
posición. La velocidad inicial de cada civilización siempre es $(0,0,0)$. Cada
coordenada de las flotas están entre -100 y 100.

## Salida
Debería indicar $N$ números, uno por cada combinación de posiciones iniciales,
con el menor número de días necesario para que las tres civilizaciones estén en
la misma posición que la inicial y con velocidad a $(0,0,0)$. El número de días
puede oscilar entre $1$ y $10^{13}$.

## Entrada de ejemplo
```
2
1 0 2 2 1 0 3 0 4
-8 -3 2 12 7 -14 25 -20 6
```

## Salida de ejemplo
```
12
3261286
```