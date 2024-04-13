n = int(input())

while n!=0:
    l = [int(x) for x in input().split()]
    l.sort()
    rep_actual = 1 # Repeticiones del número actual
    num_actual = l[0] # Numero actual

    rep_max = 0 # Maximo de repeticiones
    num_max = l[0] # Numero con más repeticiones

    for i in range(1,n):
        if l[i] == num_actual:
            rep_actual += 1
        else:
            if rep_actual > rep_max:
                num_max = num_actual
                rep_max = rep_actual
            num_actual = l[i]
            rep_actual = 1
    print(num_max)


    n = int(input())