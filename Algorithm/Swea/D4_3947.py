import sys
sys.stdin = open("D4_3947_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        i, j, d = map(int, input().split())
        data[i][j] = d
        # data[i][j] = data[j][i] = d

    for i in data:
        print(i)
    print()

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                # if i == j or i == k or j == k:
                #     continue
                data[i][j] = min(data[i][j], data[i][k] + data[k][j])

    for i in data:
        print(i)
    print()