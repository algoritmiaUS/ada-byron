# Problema G - En busca del genoma perdido

Tras unos recientes hallazgos en un laboratorio andaluz, se ha desatado una
carrera contrarreloj para descifrar secretos ocultos en el ADN. Los científicos
han descubierto que ciertas regiones, donde se concentra un elevado número de
las bases citosina (C) y guanina (G), y a la vez se limita la presencia de
adenina (A) y timina (T), podrían estar relacionadas con mecanismos de defensa
celular y adaptación a ambientes adversos. Debido al (extremo) clima veraniego
de esta región, sería muy interesante estudiar estas secuencias para poder
desarrollar nuevos tratamientos y herramientas que hagan los veranos más
soportables. El objetivo es analizar diversas secuencias de ADN para
identificar aquellas subsecuencias que cumplan simultáneamente las siguientes
condiciones:
1. Una abundancia marcada de los nucleótidos guanina (G) y citosina (C),
   fundamentales para la estabilidad estructural del ADN. Es imprescindible que
en cada región se encuentren al menos $N$ nucleótidos de guanina y al menos $N$
nucleótidos de citosina.
2. Una baja presencia de los nucleótidos adenina (A) y timina (T), que se ha
   observado podrían estar relacionados con una menor vulnerabilidad a ciertas
agresiones ambientales. Por ello, cada región debe contener menos de $M$
nucleótidos de adenina y menos de $M$ nucleótidos de timina.

Debido a la diversidad en el tamaño de las regiones de interés, los científicos
han decidido analizar todas aquellas subsecuencias contiguas cuya longitud se
encuentre en un intervalo variable, definido por un tamaño mínimo y un tamaño
máximo.

## Entrada
La entrada comienza con una línea que contiene un entero $O$ ($1 \leq O \leq
10^4$ ), el número de casos de prueba. Cada caso de prueba se describe de la
siguiente forma:
- Una línea con cinco enteros $L$, $K_{min}$, $K_{max}$, $N$ y $M$ ($1 \leq L
  \leq 10^6 \text{, } 1 \leq K_{min} \leq K_{max} \leq L \text{, } 0 \leq N
\leq K_{min} \text{, } 1 \leq M \leq K_{min} + 1$ ), donde:
    - $L$ es la longitud de la cadena de ADN.
    - $K_{min} y K_{max} definen el rango de tamaños de subsecuencias a
      analizar, ambos incluidos.
    - $N$ es el umbral mínimo requerido para cada uno de los nucleótidos G y C
      (la cantidad debe ser mayor o igual a $N$).
    - $M$ es el umbral máximo estricto permitido para cada uno de los
      nucleótidos A y T (la cantidad debe ser estrictamente menor que $M$).
- Una línea con una cadena de ADN de longitud $L$, compuesta únicamente por los
  caracteres 'A', 'C', 'G' y 'T'.

## Salida
Para cada caso de prueba, imprime una línea que contenga un entero: el número
de subsecuencias en la cadena de ADN que cumplen con las condiciones descritas.

## Entrada de ejemplo
```
2
10 3 5 1 2
ACGTGGCATG
8 2 4 1 2
GATTACAG
```

## Salida de ejemplo
```
16
1
```