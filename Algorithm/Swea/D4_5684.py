import sys
sys.stdin = open("D4_5684_input.txt", "r")

T = int(input().replace('혻', ''))
for test_case in range(T):
    N, M = map(int, input().replace('혻', '').split())
    ans = 0

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * N

    for i in range(M):
        s, e, c = map(int, input().replace('혻', '').split())
        graph[s][e] = c
