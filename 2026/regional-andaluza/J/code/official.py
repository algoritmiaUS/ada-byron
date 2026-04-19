import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return


    # Entrada: todos los P_i separado por espacios
    P = list(map(int, data))
    N = len(P)


    # FASE 1: Registro y cancelación 
    S = []                     # lista usada como pila
    i = 0

    while i < N:
        x = P[i]

        if x >= 0:
            # Llegada de proceso
            S.append(x)
            i += 1
        else:
            # Cancelación: acumular todos los negativos consecutivos
            total = -x
            j = i + 1
            while j < N and P[j] < 0:
                total += -P[j]
                j += 1

            # Eliminar total elementos desde el final
            if total >= len(S):
                S.clear()
            else:
                del S[-total:]

            # Continuar desde el primer valor no negativo
            i = j

    # FASE 2: Organización
    if not S:
        sys.stdout.write("NOPROCESO\n")
        return

    # Organización por bloques de 4: pares primero, luego impares
    E = []
    nS = len(S)
    i = 0

    while i < nS:
        end = min(i + 4, nS) 
            
        pares = []
        impares = []

        for j in range(i,end): 
            x = S[j]
            if x & 1 == 0:
                pares.append(x)
            else:
                impares.append(x)

            
        E.extend(pares)
        E.extend(impares)

        i += 4

    # ------------------ SALIDA ------------------
    sys.stdout.write(" ".join(map(str, E)) + "\n")


if __name__ == "__main__":
    main()