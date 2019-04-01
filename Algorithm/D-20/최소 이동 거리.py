import sys
sys.stdin = open("최소 이동 거리_input.txt", "r")

def Dijkstra(G, r):
    D = [9876543210] * (N + 1)
    P = [-1] * (N + 1)
    visited = [0] * (N + 1)
    D[r] = 0

    for _ in range(N):
        minindex = -1
        min = 9876543210
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minindex = i
        visited[minindex] = 1
        print(D)
        print(G)
        for v, val in G[minindex]:
            if not visited[v] and D[minindex] + val < D[v]:
                D[v] = D[minindex] + val
                P[v] = minindex



T = int(input())
for test_case in range(1):
    N, E = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
    for i in graph:
        print(*i)
    print("#{} {}".format(test_case+1, Dijkstra(graph, 0)))

# def Dijkstra(K, V, graph):
#     global inf
#     visited = [False] * V
#     d = [inf] * V
#     d[K - 1] = 0
#     while True:
#         m = inf
#         N = -1
#         for j in range(V):
#             if not visited[j] and m > d[j]:
#                 m = d[j]
#                 N = j
#         if m == inf:
#             break
#         visited[N] = True
#         for j in range(V):
#             if visited[j]: continue
#             via = d[N] + graph[N][j]
#             if d[j] > via:
#                 d[j] = via
#     return d
#
# T = int(input())
# for test_case in range(T):
#     N, E = map(int, input().split())
#     inf = 9876543210
#     graph = [[inf] * (N + 1) for _ in range(N + 1)]
#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         graph[u - 1][v - 1] = w
#         print(u, v, w)
#     print(graph)
    # print(data)
    # print("#{} {}".format(test_case+1, Dijkstra(0, N, graph)))