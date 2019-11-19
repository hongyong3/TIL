import sys
sys.stdin = open("D4_3124_input.txt", "r")

# Kruskal 방법
#
# def findSet(x):
#     if x == p[x]: return x
#     else: return findSet(p[x])
#
# def mst():
#     global V
#     cnt = 0     #간선갯수
#     total = 0   #가중치의 합
#     i = 0       #제어변수
#     while cnt < V:                      # MST 구성을 위해 V개의 간선을 선택
#         p1 = findSet(edge[i][0])        # 두 노드의 대표원소 알아내기
#         p2 = findSet(edge[i][1])
#         if p1 != p2:                    # 사이클이 생성되지 않으면
#             total += edge[i][2]         # MST에 포함되므로 가중치 추가
#             cnt += 1                    # 간선 개수 증가
#             p[p2] = p1                  # 대표 원소 관리(union)
#         i += 1                          # 저장된 다음 간선으로 이동
#     return total                        # MST 완성 후 가중치 합 반환

# ###############################################################################################
#
# # Prim 방법
# #
# # def mst():
# #     total = 0
# #     u = 0       #시작점을 0으로
# #     D[u] = 0
# #
# #     for i in range(V+1):  # 가중치 최소값 찾기
# #         min = 987654321
# #         for v in range(V+1):
# #             if visit[v] == 0 and min > D[v]:
# #                 min = D[v]
# #                 u = v
# #
# #         visit[u] = 1       # 방문처리
# #         total += adj[PI[u]][u]
# #
# #         for v in range(V+1): #인접한 정점 업데이트
# #             if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
# #                 D[v] = adj[u][v]
# #                 PI[v] = u
# #
# #     return total
# #
# # for tc in range(1, T+1):
# #     V, E = map(int, input().split())
# #     adj = [[0]*(V+1) for _ in range(V+1)]
# #     D = [987654321]*(V+1)
# #     PI = list(range(V+1))
# #     visit = [0] * (V+1)
# #     for i in range(E):
# #         edge = list(map(int, input().split()))  #시작, 끝, 가중치
# #         adj[edge[0]][edge[1]] = edge[2]     #방향성 없음
# #         adj[edge[1]][edge[0]] = edge[2]
# #     print('#{} {}'.format(tc, mst()))
#
#
# ###############################################################################################
#
#
# # def findSet(x):
# #     if x == p[x]:
# #         return x
# #     return findSet(p[x])
# #
# # def mst():
# #     global V
# #     count, total, i = 0, 0, 0
# #     while count < V - 1:
# #         p1 = findSet(data[i][0])
# #         p2 = findSet(data[i][1])
# #         if p1 != p2:
# #             total += data[i][2]
# #             count += 1
# #             p[p2] = p1
# #         i += 1
# #     return total
# #
# # T = int(input())
# # for test_case in range(T):
# #     V, E = map(int, input().split())
# #     data = [list(map(int, input().split())) for _ in range(E)]
# #     data.sort(key=lambda x: x[2])
# #     p = list(range(V + 1))
# #     print("#{} {}".format(test_case + 1, mst()))
#
# ################################################################################
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