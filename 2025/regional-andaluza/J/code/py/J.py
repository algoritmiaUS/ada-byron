import sys

def max_cristales(n, m, grid):
    # Creamos una matriz auxiliar de igual tamaño
    dp = [[0] * m for _ in range(n)]

    # Inicializamos la primera celda
    dp[0][0] = grid[0][0]

    # Primera fila (el valor acumulado sólo puede venir de la celda a su izq)
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Primera columna (el valor acumulado sólo puede venir de la celda de arriba)
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Resto de la matriz, calculando el acumulado máximo de cada una.
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + max(
                dp[i - 1][j],      # desde arriba
                dp[i][j - 1],      # desde la izquierda
                dp[i - 1][j - 1]   # desde la diagonal
            )
    # Devolvemos el valor de la salida.
    return dp[n - 1][m - 1]

def main():
    # Lectura de la cantidad de casos de prueba
    N = int(sys.stdin.readline().strip())
    if not N:
        return

    for _ in range(N):
        # Lectura de las dimensiones de la matriz
        n, m = map(int, sys.stdin.readline().strip().split())
        
        # Lectura de la matriz
        grid = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            grid.append(row)
        
        # Obtener el resultado
        resultado = max_cristales(n, m, grid)
        print(resultado)

if __name__ == "__main__":
    main()
