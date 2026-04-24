import sys

def es_solucion(carga_max, k, horas):
    """
    Función de verificación: O(n)
    Determina si se pueden repartir los tramos en k brigadas 
    sin que ninguna supere la carga_max.
    """
    carga = 0
    # Asignar carga de trabajo consecutivamente a las
    # brigadas sin superar carga_max por brigada.
    for hi in horas:
        carga += hi
        if carga > carga_max:
            k -= 1
            carga = hi
            
    # ¿Hay suficientes brigadas disponibles?
    return k > 0

def minCargaMax():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    i = 0
    while i < len(input_data):
        try:
            n = int(input_data[i])
            k = int(input_data[i + 1])
            i += 2
        except (IndexError, ValueError):
            break
        horas = []
        for _ in range(n):
            horas.append(int(input_data[i]))
            i += 1

        # Inicializar el intervalo de la solución [inf, sup]
        # inf: Máximo de horas de todos los tramos
        # sup: Suma de horas de todos los tramos
        inf = max(horas)
        sup = sum(horas)
        mCM = sup

        # Búsqueda de la solución óptima: O(N log(suma horas))
        while inf <= sup:
            carga_max = inf + (sup - inf) // 2
            if es_solucion(carga_max, k, horas):
                mCM = carga_max    # carga_max es solución, intentar algo menor
                sup = carga_max - 1
            else:
                inf = carga_max + 1 # No es solución, necesitamos mayor carga de trabajo

        sys.stdout.write(f"{mCM}\n")

if __name__ == "__main__":
    minCargaMax()