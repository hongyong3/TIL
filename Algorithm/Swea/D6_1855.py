import sys
sys.stdin = open("D6_1855_input.txt", "r")

'''
LCA Algorithm(Lowest Common Ancestor)
- 최소 공통 조상을 찾는 알고리즘
- 두 정점 u, v에서 가장 가까운 공통 조상을 찾는 과정
- 세그먼트 트리를 이용하지 않고 DP를 이용하여 해결
- 시간 복잡도
    * LCA 알고리즘 시간 복잡도 O(logN)
    * 쿼리가 함께 존재할 경우 시간 복잡도 O(MlogN)
- 알고리즘 동작 과정
    * 첫 번째로 입력받은 정점과 간선을 이용하여 양방향 그래프를 생성
    * depth와 조상을 가지는 트리를 생성

'''

# def sparse():
#     for i in range(1, 21):
#         for j in range(N):
#             p[j][i] = p[p[j][i - 1]][i - 1]
#
#
# def lca(x, y):
#     if d[x] < d[y]:
#         d[x], d[y] = d[y], d[x]
#
#     for i in range(19, - 1, - 1):
#         if d[x] - d[y] >= (1 << i):
#             x = p[x][i]
#
#     if x == y:
#         return x
#
#     for i in range(19, - 1, - 1):
#         if p[x][i] != p[y][i]:
#             x = p[x][i]
#             y = p[y][i]
#
#     return p[x][0]
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     graph = [[] for _ in range(N + 3)]
#     chk = [0] * (N + 1)
#     d = [0] * (N + 1)
#     p = [[0] * 23 for _ in range(N + 3)]
#
#     j = 1
#     for i in data:
#         graph[i - 1].append(j)
#         j += 1
#
#     chk[0] = 1
#     q = [(0, 0)]
#
#     while q:
#         x, dep = q.pop(0)
#         d[x] = dep
#
#         for i in graph[x]:
#             nx = i
#             if not chk[nx]:
#                 chk[nx] = 1
#                 p[nx][0] = x
#                 q.append((nx, dep + 1))
#
#     sparse()
#
#     ans = 0
#     chk = [0] * (N + 1)
#     chk[0] = 1
#     q = [0]
#     vt = []
#
#     while q:
#         x = q.pop(0)
#         vt.append(x)
#
#         for i in graph[x]:
#             nx = i
#             if not chk[nx]:
#                 chk[nx] = 1
#                 q.append(nx)
#
#     for i in range(N - 1):
#         temp = lca(vt[i], vt[i + 1])
#         a = d[vt[i]] - d[temp]
#         b = d[vt[i + 1]] - d[temp]
#         ans += (a + b)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(N + 3)]  # 마지막 node의 자식까지 생각
    chk = [0] * N
    d = [0] * N
    p = [[0] * 23 for _ in range(N + 3)]
    j = 1

    for i in data:
        graph[i - 1].append(j)
        j += 1

    chk[0] = 1
    q = [(0, 0)]

    while q:
        node, depth = q.pop(0)
        d[node] = depth

        for i in graph[node]:
            v = i
            if not chk[v]:
                chk[v] = 1
                p[v][0] = node
                q.append((v, depth + 1))