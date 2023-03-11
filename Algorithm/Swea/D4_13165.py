import sys
sys.stdin = open("D4_13165_input.txt", "r")

def dfs(n, val):
    global ans
    if n == N:
        ans = min(ans, val)
        return
    for i in range(N + 1):
        if graph[n][i]:
            if val + graph[n][i] < ans:
                dfs(i, val + graph[n][i])


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    ans = float('inf')
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    for x in range(1, N + 1):
        if graph[0][x]:
            dfs(x, graph[0][x])
    print("#{} {}".format(test_case + 1, ans))