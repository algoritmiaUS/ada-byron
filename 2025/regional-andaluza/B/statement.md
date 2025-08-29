# Problema B - ¡Ataque Alienígena!

En un remoto observatorio astronómico, un grupo de científicos ha detectado una
serie de misteriosas señales provenientes del espacio profundo. Después de
meses de análisis, han llegado a una conclusión sorprendente: ¡las señales son
códigos alienígenas con información encriptada sobre futuros ataques a la
Tierra!

Los científicos han logrado interceptar $N$ códigos alienígenas, cada uno
compuesto por una secuencia de números con dígitos del $0$ al $9$. Los
científicos han desarrollado un lema técnico para identificar cuándo será el
próximo ataque a la Tierra, basado en cuántos de esos códigos verifican un
prefijo determinado.

Tu tarea es desarrollar un programa que pueda responder a $Q$ consultas. Cada
consulta proporcionará un prefijo, y tu programa deberá determinar cuántos
códigos alienígenas en la lista comienzan con ese prefijo. Esto permitirá a los
científicos predecir el próximo ataque.

## Entrada
Cada archivo de entrada consta de múltiples casos. En cada caso, la primera
línea contiene dos enteros $N$ y $Q$ ( $1 \leq N,Q \leq 10^5$ ), el número de
códigos alienígenas y el número de consultas, respectivamente.

Las siguientes $N$ líneas contienen cada una un _string_ $s_i$ ($1 \leq |s_i|
\leq 10$ ), un código alienígena. Cada $s_i$ está compuesto únicamente por
dígitos del $0$ al $9$.

Las siguientes $Q$ líneas contienen cada una un _string_ $p_j$ ($1 \leq |p_j|
\leq 10$), representando el prefijo para cada consulta. Cada $p_j$ está
compuesto únicamente por dígitos del $0$ al $9$.

**Nota:** el archivo de entrada finaliza después de las $Q$ líneas de consulta
del último caso. **No hay ningún marcador especial** al final.

## Salida
Para cada caso se empezará con una línea `"Case X:"` (donde `X` es un número
empezando en $1$ que indica el caso que resuelve). A continuación (siguiente
línea) para cada una de las $Q$ consultas, imprime en una línea separada un
único entero que representa la cantidad de códigos alienígenas que comienzan
con el prefijo dado.

## Entrada de ejemplo
```
5 3
91234
87654
91245
12345
98765
912
876
111
2 2
4321
4378
43
44
```

## Salida de ejemplo
```
Case 1:
2
1
0
Case 2:
2
0
```