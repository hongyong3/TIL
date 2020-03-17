import sys
sys.stdin = open("D2_4871_input.txt", "r")

def dfs(n):
    visited[n] = 1
    for i in range(V + 1):
        if graph[n][i] == 1 and not visited[i]:
            dfs(i)
    if visited[G] == 1:
        return 1
    return 0

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1
    S, G = map(int, input().split())
    print("#{} {}".format(test_case + 1, dfs(S)))