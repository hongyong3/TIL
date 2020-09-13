import sys
sys.stdin = open("D4_3124_input.txt", "r")

# from heapq import *
#
# def find(u):
#     if par[u] == u:
#         return u
#     par[u] = find(par[u])
#     return par[u]
#
# def merge(u, v):
#     u = find(u)
#     v = find(v)
#     if p[u] < p[v]:
#         u, v = v, u
#     par[v] = u
#     if p[u] == p[v]:
#         p[u] += 1
#
#
# T = int(input())
# for test_case in range(T):
#     heap = []
#     V, E = map(int, input().split())
#     p = [1] * (V + 1)
#     par = [i for i in range(V+1)]
#     ans = 0
#     for _ in range(E):
#         A, B, C = map(int,input().split())
#         heappush(heap,(C, A, B))
#
#     while heap:
#         C, A, B = heappop(heap)
#         if find(A) != find(B):
#             merge(A, B)
#             ans += C
#     print("#{} {}".format(test_case + 1, ans))
#
# ###################################################################################
#
# import heapq
#
# def prim(v):
#     q = []
#     visited = [0] * (V + 1)
#     visited[v] = 1
#     d = 0
#     cnt = 1
#     for a in data[v]:
#         heapq.heappush(q, a)
#
#     while q:
#         c, v = heapq.heappop(q)
#         if not visited[v]:
#             visited[v] = 1
#             cnt += 1
#             d += c
#             for a in data[v]:
#                 heapq.heappush(q, a)
#         if cnt == V:
#             return d
#     return 0
#
# T = int(input())
# for test_case in range(T):
#     V, E = map(int, input().split())
#     data =[[] for _ in range(V + 1)]
#     for _ in range(E):
#         a, b, c = map(int, input().split())
#         data[a].append((c, b))
#         data[b].append((c, a))
#     print("#{} {}".format(test_case + 1, prim(1)))
#
# ###################################################################################
#
def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v, e):
    root1 = find(v)
    root2 = find(e)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    for v in graph:
        make_set(v)
    mst = []
    edges = data
    edges.sort()
    for edge in edges:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            mst.append(edge)
    return mst

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    graph, parent, rank, mat = list(range(1, V + 1)), {}, {}, 0
    data = [list(map(int, input().split())) for _ in range(E)]
    for i in range(E):
        data[i] = [data[i][2], data[i][0], data[i][1]]
    for i in kruskal():
        mat += i[0]
    print("#{} {}".format(test_case + 1, mat))