import sys
sys.stdin = open("D4_7465_input.txt", "r")

def dfs(x):
    if not visited[x]:
        visited[x] = 1
        for i in range(N + 1):
            if graph[x][i] == 1 and not visited[i]:
                dfs(i)

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    visited, graph, mat = [0] * (N + 1), [[0] * (N + 1) for _ in range(N + 1)], 0
    print(data)
    for i in range(len(data)):
        graph[data[i][0]][data[i][1]] = graph[data[i][1]][data[i][0]] = 1
    for j in range(N + 1):
        if not visited[j]:
            dfs(j)
            for k in range(N + 1):
                if not visited[k]:
                    mat += 1
                    break
    print("#{} {}".format(test_case + 1, mat))