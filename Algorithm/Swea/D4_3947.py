import sys
sys.stdin = open("D4_3947_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        i, j, d = map(int, input().split())
        data[i][j] = d

    for i in data:
        print(i)
    print()