def DFS(v):
    for i in range(count[v]):
        if visited[G[v][i]] == 0:
            DFS(G[v][i])

    visited[v] = 1
    print("%d" %v, end=' ')

import sys
sys.stdin = open("작업순서_input.txt")

for test_case in range(1, 11):
    V, E = map(int, input().split())            # 정점, 간선
    G = [[0] * (V + 1) for _ in range(V+1)]     # 인접행렬
    visited = [0] * (V + 1)
    count = [0] * (V + 1)
    data = list(map(int, input().split()))

    for i in range(E):
        u, v = data[i*2: i*2 + 2]
        G[v][count[v]] = u
        count[v] += 1           # 진입차수

    print("#%d" % test_case, end=' ')

    for i in range(1, V+1):
        if visited[i] == 0:
            DFS(i)

    print()