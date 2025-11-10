# this task is solved using complicated method, that is not used at the first semester, so it is definetely optional XD

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def move_rook(T, step_w, step_k):
    n, m = len(T), len(T[0])
    DP = [[float('inf') for _ in range(m)] for _ in range(n)]

    i_start, i_end = (0, n) if step_w > 0 else (n-1, -1)
    j_start, j_end = (0, n) if step_k > 0 else (n-1, -1)
    DP[i_start][j_start] = 0

    for i in range(i_start, i_end, step_w):
        for j in range(j_start, j_end, step_k):
            # kolejne kolumny
            for k1 in range(j + step_k, j_end, step_k):
                if gcd(T[i][j], T[i][k1]) == 1:
                    DP[i][k1] = min(DP[i][k1], DP[i][j] + 1)

            # kolejne wiersze
            for k2 in range(i + step_w , i_end, step_w):
                if gcd(T[i][j], T[k2][j]) == 1:
                    DP[k2][j] = min(DP[k2][j], DP[i][j] + 1)

    return DP[i_end-step_w][j_end-step_k]


arr = [
            [1, 3, 5, 7, 11, 13, 17, 19, 23, 29],
            [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
            [5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
            [10, 11, 13, 17, 19, 23, 29, 31, 37, 41],
            [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
            [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
            [17, 19, 23, 29, 31, 37, 41, 43, 47, 53],
            [19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
            [23, 29, 31, 37, 41, 43, 47, 53, 59, 61],
            [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],
        ]

print("top left to bottom right: ", move_rook(arr, 1, 1))
print("top right to bottom left: ", move_rook(arr, 1, -1))