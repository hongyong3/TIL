import sys
sys.stdin = open("D4_3124_input.txt", "r")

from heapq import *

def find(u):
    if par[u] == u:
        return u
    par[u] = find(par[u])
    return par[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    if p[u] < p[v]:
        u, v = v, u
    par[v] = u
    if p[u] == p[v]:
        p[u] += 1


T = int(input())
for test_case in range(T):
    heap = []
    V, E = map(int, input().split())
    p = [1] * (V + 1)
    par = [i for i in range(V+1)]
    ans = 0
    for _ in range(E):
        A, B, C = map(int,input().split())
        heappush(heap,(C, A, B))

    while heap:
        C, A, B = heappop(heap)
        if find(A) != find(B):
            merge(A, B)
            ans += C
    print("#{} {}".format(test_case + 1, ans))

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