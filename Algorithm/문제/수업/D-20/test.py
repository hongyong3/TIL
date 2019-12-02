# import sys
# sys.stdin = open("최소 이동 거리_input.txt", "r")
#
# def dijkstra(K, V, graph):
#     global inf
#     # s는 해당 노드를 방문 했는지 여부를 저장하는 변수이다
#     visited = [False] * V
#     # d는 memoization을 위한 array이다. d[i]는 정점 K에서 i까지 가는 최소한의 거리가 저장되어 있다.
#     d = float('inf')
#     # d[K - 1] = 0
#
#     while True:
#         m = inf
#         N = -1
#
#         # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
#         # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
#         for j in range(V):
#             if not visited[j] and m > d:
#                 m = d
#                 N = j
#
#         # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
#         # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.
#         if m == inf:
#             break
#
#         # N번 노드를 '방문'한다.
#         # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는 노드가 있는지 확인하고,
#         # 더 빨리 갈 수 있다면 해당 노드(노드의 번호 j라고 하자)의 d[j]를 업데이트 해준다.
#         visited[N] = True
#
#         for j in range(V):
#             if visited[j]: continue
#             via = d + graph[N][j]
#             if d > via:
#                 d = via
#
#     return d
#
# T = int(input())
# for test_case in range(T):
#     V, E = map(int, input().split())
#     K = 0
#     inf = 9876543210
#     graph = [[inf]*V for _ in range(V)]
#
#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         graph[u-1][v-1] = w
#
#     print(dijkstra(K, V, graph))
#     # for d in dijkstra(K, V, graph):
#     #     print(d if d != INF else "INF")

def floydwarshall(graph):
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = float('inf')
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u

    for t in graph:
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v]  # route new path through t

    return dist, pred