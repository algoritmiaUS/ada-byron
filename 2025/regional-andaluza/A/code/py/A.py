def es_potencia_de_2(n):
    return (n & (n - 1)) == 0

def contar_combates(n):
    combates = 0
    while n > 1:
        if es_potencia_de_2(n):
            combates += n - 1
            n = 1  
        else:
            combates += n // 2
            n = n // 2
            if n % 2 == 1 and n != 1:
                n += 1
    return combates

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(contar_combates(N))
