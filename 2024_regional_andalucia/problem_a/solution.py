def max_earnings(n, m, c0, d0, chorizos):
    # Inicializar dp con cero para todas las capacidades de masa desde 0 hasta n
    dp = [0] * (n + 1)

    # Iterar sobre cada tipo de chorizo
    for ai, bi, ci, di in chorizos:
        # Procesar de atrás hacia adelante para evitar usar un bollo más de una vez
        for j in range(n, ci - 1, -1):
            # Calcular cuántos bollos con este chorizo podemos hacer con masa j
            max_bollos = min(ai // bi, j // ci)
            # Actualizar dp para cada cantidad de masa posible
            for k in range(1, max_bollos + 1):
                dp[j] = max(dp[j], dp[j - k * ci] + k * di)

    # Procesar los bollos sin relleno
    for j in range(c0, n + 1):
        dp[j] = max(dp[j], dp[j - c0] + d0)

    # La respuesta es el máximo valor en dp
    return max(dp)

# Lectura de entrada
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
c0 = int(data[2])
d0 = int(data[3])

chorizos = []
index = 4
for _ in range(m):
    ai = int(data[index])
    bi = int(data[index + 1])
    ci = int(data[index + 2])
    di = int(data[index + 3])
    chorizos.append((ai, bi, ci, di))
    index += 4

# Llamar a la función para obtener la máxima ganancia posible
result = max_earnings(n, m, c0, d0, chorizos)
print(result)
