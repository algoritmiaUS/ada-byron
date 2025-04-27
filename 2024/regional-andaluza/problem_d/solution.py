
"""
Truco: en lugar de ir llevando en un conjunto los sobres comprados y recorrer N y ver si
esta en el sobre o no, tener una lista de booleanos que indique si el sobre ha sido
comprado o no. De esta forma podemos acceder en tiempo O(1) a si un sobre ha sido
comprado o no.
"""
 
N, S, P = map(int, input().split()) 
 
precios = list(map(int, input().split())) 
 
comprado = [False] * N 
precio_total = sum(precios) 
coste_minimo = precio_total 
 
for i in range(S): 
    dinero_actual = (i+1) * P 
    sobre = list(map(int, input().split())) 
 
    for j in sobre: 
        if not comprado[j - 1]: 
            comprado[j - 1] = True 
            precio_total -= precios[j - 1] 
        coste_actual = dinero_actual + precio_total 
        coste_minimo = min(coste_minimo, coste_actual) 

print(coste_minimo)
