from math import gcd

def leer_estado():
    N = int(input())
    f = []
    for _ in range(N):
        l = list(map(int, input().split()))
        f.append([[l[0], l[1], l[2]], [l[3], l[4], l[5]], [l[6], l[7], l[8]]])

    return f

def mcm(a, b):
    return a * b // gcd(a, b)

def obtener_ciclo_eje(posiciones):
    posiciones_iniciales = posiciones[:]
    velocidades = [0] * len(posiciones)
    pasos = 0

    while True:
        # Actualizar velocidades según las reglas
        for i in range(len(posiciones)):
            for j in range(i + 1, len(posiciones)):
                if posiciones[i] < posiciones[j]:
                    velocidades[i] += 1
                    velocidades[j] -= 1
                elif posiciones[i] > posiciones[j]:
                    velocidades[i] -= 1
                    velocidades[j] += 1

        # Actualizar posiciones
        for i in range(len(posiciones)):
            posiciones[i] += velocidades[i]
        pasos += 1
        if posiciones == posiciones_iniciales and all(v == 0 for v in velocidades):
            return pasos

def calcular_dias_para_repeticion(flotas):
    ciclos = []
    for eje in range(3):  # x, y, z
        posiciones = [flota[eje] for flota in flotas]
        ciclos.append(obtener_ciclo_eje(posiciones[:]))
    return mcm(ciclos[0], mcm(ciclos[1], ciclos[2]))

if __name__ == "__main__":
    flotas = leer_estado()
    for f in flotas:
        print(calcular_dias_para_repeticion(f))
