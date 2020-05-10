import sys
sys.stdin = open("D5_5521_input.txt", "r")

T = int(input().replace('혻', ''))
for test_case in range(1):
    N, M = map(int, input().replace('혻', '').split())
    data = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    visited[1] = 1
    ans = 0
    for _ in range(M):
        a, b = map(int, input().replace('혻', '').split())
        data[a][b], data[b][a] = 1, 1
    