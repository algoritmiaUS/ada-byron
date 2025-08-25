import heapq

class Cociente:
    def __init__(self, cliente, gasto, divisor):
        self.cliente = cliente
        self.gasto = gasto
        self.divisor = divisor

    def __lt__(self, other):
        # Orden decreciente para el montículo
        cociente_self = self.gasto // self.divisor
        cociente_other = other.gasto // other.divisor
        return cociente_self > cociente_other or \
               (cociente_self == cociente_other and self.gasto > other.gasto)

def repartir_vales(m, n):
    vales = [0] * m  # Número de vales de cada cliente
    mayores_cocientes = []  # Montículo de máximos

    # Inicialización con los gastos de los m clientes.
    gastos = list(map(int, input().split()))
    for k in range(m):
        heapq.heappush(mayores_cocientes, Cociente(k, gastos[k], 1))

    # Seleccionar los n mayores cocientes
    for _ in range(n):
        # Asignar vale al cliente con mayor cociente
        mayor = mayores_cocientes[0]
        vales[mayor.cliente] += 1
        # Añadir nuevo cociente y eliminar el mayor
        mayor.divisor += 1
        heapq.heapreplace(mayores_cocientes, mayor)

    print(' '.join(map(str, vales)))

if __name__ == "__main__":
    while True:
        n_cli, n_vales = map(int, input().split())
        if n_cli == 0 or n_vales == 0:
            break
        repartir_vales(n_cli, n_vales)
