def leer_estado():
    N = int(input())
    f = []
    for _ in range(N):
        l = list(map(int, input().split()))
        f.append([[l[0], l[1], l[2]], [l[3], l[4], l[5]], [l[6], l[7], l[8]]])

    return f

def actualizar_velocidades(pos, vel):
    for i in range(3):
        for j in range(i + 1, 3):
            for eje in range(3):
                if pos[i][eje] < pos[j][eje]:
                    vel[i][eje] += 1
                    vel[j][eje] -= 1
                elif pos[i][eje] > pos[j][eje]:
                    vel[i][eje] -= 1
                    vel[j][eje] += 1

def actualizar_posiciones(pos, vel):
    for i in range(3):
        for eje in range(3):
            pos[i][eje] += vel[i][eje]

def calcular_ciclo_completo(pos_inicial):
    pos = [p[:] for p in pos_inicial]
    vel = [[0, 0, 0] for _ in range(3)]
    pasos = 0
    while True:
        actualizar_velocidades(pos, vel)
        actualizar_posiciones(pos, vel)
        pasos += 1
        if pos == pos_inicial and all(v == [0,0,0] for v in vel):
            return pasos

if __name__ == "__main__":
    flotas = leer_estado()
    for f in flotas:
        print(calcular_ciclo_completo(f))
