import sys
sys.stdin = open("D6_1268_input.txt", "r")

T = int(input())
for test_case in range(T):
    R, N, K = map(int, input().split())
    data = [[] for _ in range(N)]
    item = [list(map(int, input().split())) for _ in range(N)]
    A = [0] * (2 * N + 1)
    B = [0] * (2 * N + 1)
    C = [0] * (N + 1)
    mat = 0

    for i in range(N):
        x1, y1 = item[i]
        for j in range(N):
            if i != j:
                x2, y2 = item[j]
                a = x2 - x1
                b = y2 - y1
                k = 1
                if not a:
                    k, t1 = 0, 0
                else:
                    t1 = 1 if a > 0 else - 1
                if not b:
                    k, t2 = 0, 0
                else:
                    t2 = 1 if b > 0 else - 1
                if k:
                    k = a / b
                if not (k, t1, t2) in data[i]:
                    data[i].append((k, t1, t2))

    for i in range(N):
        p = len(data[i])
        mat += p
        A[i + 1] = p

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[j] = ((A[j] * K + j) % N) + 1
            A[N + j] = ((A[j] * j + K) % N) + 1
        A.sort()
        B[0] = 1
        for j in range(1, 2 * N + 1):
            B[j] = ((B[j - 1] * A[j] + j) % N) + 1
        C[i] = B[2 * N]

    print("#{} {} {}".format(test_case + 1, mat, sum(C)))