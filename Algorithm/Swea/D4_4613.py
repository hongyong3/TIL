import sys
sys.stdin = open("D4_4613_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    W, B, R, mat = [0] * N, [0] * N, [0] * N, 0

    for i in range(N):
        W[i], B[i], R[i] = data[i].count('W'), data[i].count('B'), data[i].count('R')

    for i in range(1, N - 1):
        for j in range(i, N - 1):
            count = [0, 0, 0]   # W, B, R
            for k in range(i):
                count[0] += W[k]
            for k in range(i, j + 1):
                count[1] += B[k]
            for k in range(j + 1, N):
                count[2] += R[k]
            mat = max(mat, sum(count))
    mat = (N * M) - mat
    print("#{} {}".format(test_case + 1, mat))