import sys

def num_to_list(n):
    ls = []
    while n > 0:
        ls.append(n % 10)
        n = n // 10
    return ls

def sum_acc(ls):
    acc =0
    i = len(ls)
    for n in ls:
        acc+= n**i
    return acc

def main():
    while True:
        n = int(input())
        if n <= 0:
            break

        ls = num_to_list(n)
        suma = sum_acc(ls)

        res = ""
        if suma == n:
            print("SEGURO")
        else:
            print("INSEGURO")


if __name__ == "__main__":
    main()