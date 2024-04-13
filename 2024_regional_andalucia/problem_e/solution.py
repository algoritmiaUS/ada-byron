
def solve(R, C):

    matrix = []
    for _ in range(R):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    Q = int(input())

    queries = []
    for _ in range(Q):
        query = [int(x) for x in input().split()]
        queries.append(query)

    sum_matrix = [[0] * (C + 1) for _ in range(R + 1)]

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            sum_matrix[i][j] = (
                matrix[i-1][j-1]
                + sum_matrix[i - 1][j]
                + sum_matrix[i][j-1]
                - sum_matrix[i-1][j-1]
            )

    max_vasos = -1
    max_id = -1

    for query in queries:
        id, r1, c1, r2, c2 = query
        total_vasos = (
            sum_matrix[r2][c2]
            - (sum_matrix[r1-1][c2] if r1 > 1 else 0)
            - (sum_matrix[r2][c1-1] if c1 > 1 else 0)
            + (sum_matrix[r1-1][c1-1] if r1 > 1 and c1 > 1 else 0)
        )

        if total_vasos > max_vasos or (total_vasos == max_vasos and id < max_id):
            max_vasos = total_vasos
            max_id = id

    print(max_id, max_vasos)


R, C = [int(x) for x in input().split()]

solve(R, C)
