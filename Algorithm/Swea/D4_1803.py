import sys
sys.stdin = open("D4_1803_input.txt", "r")

# def make_set(v):
#     parent[v] = v
#     rank[v] = 0
#
# def find(v):
#     if parent[v] != v:
#         parent[v] = find(parent[v])
#     return parent[v]
#
# def union(v, e):
#     root1 = find(v)
#     root2 = find(e)
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#             if rank[root1] == rank[root2]:
#                 rank[root2] += 1
#
# def kruskal():
#     for v in graph:
#         make_set(v)
#     mst = []
#     edges = data
#     edges.sort()
#     for edge in edges:
#         if find(edge[1]) != find(edge[2]):
#             union(edge[1], edge[2])
#             mst.append(edge)
#     return mst
#
#
# T = int(input())
# for test_case in range(T):
#     N, M, v, e = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(M)]
#     print(data)
#     graph, parent, rank, ans = list(range(1, N + 1)), {}, {}, 0
#     for i in range(M):
#         data[i] = [data[i][2], data[i][0], data[i][1]]
#     for i in kruskal():
#         ans += i[0]
#     print("#{} {}".format(test_case + 1, ans))


from collections import deque
inf = 987654321

def SPFA(n):
    d = [inf for _ in range(N)]
    on = [False for _ in range(N)]
    cycle = [0 for _ in range(N)]
    d[n] = 0
    on[n] = 1
    q = deque([n])
    while q:
        now = q.popleft()
        on[now] = 0
        for next, value in edge[now]:
            if d[next] > d[now] + value:
                d[next] = d[now] + value
                if not on[next]:
                    cycle[next] += 1
                    on[next] = 1
                    q.append(next)
    for value in d[1:]:
        return value

T = int(input())
for test_case in range(T):
    N, M, s, e = map(int, input().split())
    edge = [[] for _ in range(N + 1)]
    graph = [[0] * (N) for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w
        edge[u - 1].append((v - 1, w))
    print("#{} {}".format(test_case + 1, SPFA(0)))
    for i in graph:
        print(i)
    print()