import sys

def leer_varios_numeros():
    return list(map(int, input().split()))


def calcular_ARE(ventas):
    n = len(ventas)
    are = [1] * n  
    stack = []  
    
    # Recorremos cada día
    for i in range(n):
        
        while stack and ventas[stack[-1]] <= ventas[i]:
            stack.pop()  # Sacamos el último elemento de la pila
        
        are[i] = i - stack[-1] if stack else i + 1
        
        stack.append(i)
    
    return are

def main():
    while True:
        n = int(input())

        if n == 0:
            break

        ls = leer_varios_numeros()
        res = calcular_ARE(ls)
        print(' '.join(map(str, res)))
        # print(res)


        
        


if __name__ == "__main__":
    main()