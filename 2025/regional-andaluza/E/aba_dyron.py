import time
import bisect

def solve_test_case():
    N_Q_line = input().strip()
    N, Q = map(int, N_Q_line.split())
    
    scores = list(map(int, input().split()))
    scores.sort()
    
    results = []
    # Para cada consulta, se usa bisect_left para encontrar la primera posición
    # donde la puntuación es mayor o igual que el valor de corte.
    for _ in range(Q):
        cutoff = int(input())
        idx = bisect.bisect_left(scores, cutoff)
        count = N - idx
        results.append(count)
    return results

def main():
    
    T = int(input().strip())
    all_results = []
    
    for _ in range(T):
        results = solve_test_case()
        all_results.extend(results)

    for result in all_results:
        print(result)

if __name__ == "__main__":
    main()
