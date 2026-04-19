import sys

def resolver_dp(H, liquido, caps):
    # Inicializar DP con ceros, misma estructura que capacidades
    dp = []
    for i in range(H):
        dp.append([0.0] * ((i + 1) * (i + 1)))

    # Vertido inicial
    if H > 0:
        dp[0][0] = liquido

    # Propagar líquido nivel a nivel
    # Usar rangos y caché de variables para velocidad en Python
    for i in range(H - 1):
        lado_actual = i + 1
        lado_siguiente = i + 2
        
        dp_actual = dp[i]
        dp_siguiente = dp[i + 1]
        caps_actual = caps[i]

        for r in range(lado_actual):
            # Precalcular índices de fila para velocidad
            offset_actual = r * lado_actual
            offset_sig_r = r * lado_siguiente
            offset_sig_rp1 = (r + 1) * lado_siguiente

            for c in range(lado_actual):
                idx_actual = offset_actual + c
                
                sobrante = dp_actual[idx_actual] - caps_actual[idx_actual]

                if sobrante > 0:
                    cuarto = sobrante / 4.0
                    
                    # Distribución a las 4 copas inferiores
                    dp_siguiente[offset_sig_r + c] += cuarto
                    dp_siguiente[offset_sig_rp1 + c] += cuarto
                    dp_siguiente[offset_sig_r + (c + 1)] += cuarto
                    dp_siguiente[offset_sig_rp1 + (c + 1)] += cuarto
    return dp

def main():
    # Leer toda la entrada de golpe es mucho más rápido en Python
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    
    liquido_inicial = float(input_data[ptr])
    ptr += 1
    H = int(input_data[ptr])
    ptr += 1

    # 1. Leer Capacidades
    capacidades = []
    for i in range(H):
        num_copas_nivel = (i + 1) * (i + 1)
        # Slicing rápido para leer el nivel
        nivel_caps = [float(x) for x in input_data[ptr : ptr + num_copas_nivel]]
        capacidades.append(nivel_caps)
        ptr += num_copas_nivel

    # 2. Procesar con DP
    flujo_total = resolver_dp(H, liquido_inicial, capacidades)

    # 3. Responder Consultas
    if ptr < len(input_data):
        Q = int(input_data[ptr])
        ptr += 1
        
        salida = []
        for _ in range(Q):
            nivel = int(input_data[ptr])
            fila = int(input_data[ptr + 1])
            col = int(input_data[ptr + 2])
            ptr += 3

            idx = fila * (nivel + 1) + col
            # El volumen real es el mínimo entre lo que llegó y la capacidad
            contenido = min(capacidades[nivel][idx], flujo_total[nivel][idx])
            
            # Formatear a 6 decimales
            salida.append(f"{contenido:.6f}")
        
        # Imprimir todo junto al final es más rápido
        sys.stdout.write("\n".join(salida) + "\n")

if __name__ == "__main__":
    main()
    