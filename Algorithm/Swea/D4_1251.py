import sys
sys.stdin = open("D4_1251_input.txt", "r")

# 내 풀이 1
# def make_set(v):
#     parent[v] = v
#     rank[v] = 0
#
# def find(v):
#     if parent[v] != v:
#         parent[v] = find(parent[v])
#     return  parent[v]
#
# def union(v, u):
#     root1 = find(v)
#     root2 = find(u)
#
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#             if rank[root1] == rank[root2]:
#                 rank[root2] += 1
#
# def kruskal():
#     for v in range(N):
#         make_set(v)
#     # mst = []
#     mst = 0
#     for edge in edges:
#         if find(edge[1]) != find(edge[2]):
#             union(edge[1], edge[2])
#             # mst.append(edge[0])
#             mst += edge[0]
#     # return sum(mst)
#     return mst
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(2)]
#     E = float(input())
#     parent = {}
#     rank = {}
#     edges = []  # 거리, 노드1, 노드2
#
#     for i in range(N):
#         for j in range(i + 1, N):
#             edges.append((pow(data[0][i] - data[0][j], 2) + pow(data[1][i] - data[1][j], 2), i, j))
#     edges.sort()
#     print("#{} {}".format(test_case + 1, round(kruskal() * E)))


#############################################################################

# 다른사람 풀이
# def find(x):
#     if parent[x] == x:
#         return x
#     else:
#         parent[x] = find(parent[x])
#         return parent[x]
#
#
# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x != y:
#         parent[y] = x
#         return True
#     else:
#         return False
#
#
# def calc(nxt, now):
#     return (a[nxt][1] - a[now][1]) ** 2 + (a[nxt][0] - a[now][0]) ** 2
#
#
# for t in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     a = list(zip(a, b))
#     parent = [0] * (n)
#     for i in range(n):
#         parent[i] = i
#
#     d = []
#     for i in range(n):
#         for j in range(i, n):
#             if i == j:
#                 continue
#             d.append((i, j, calc(i, j)))
#     d = sorted(d, key=lambda x: x[2])
#     ans = 0
#     for x, y, cur in d:
#         if not union(x, y):
#             continue
#         else:
#             ans += cur
#     k = float(input())
#     print('#{} {}'.format(t + 1, round(ans * k)))


#############################################################################

# 내 풀이 2
def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]

def union(v, e):
    v = find(v)
    e = find(e)

    if v != e:
        parent[e] = v
        return True
    return False

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    parent = list(range(N))
    edges = []
    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            edges.append((pow(data[0][i] - data[0][j], 2) + pow(data[1][i] - data[1][j], 2), i, j))
    # edges.sort()
    edges = sorted(edges, key = lambda x : x[0])

    for distance, v, e in edges:
        if not union(v, e):
            continue
        ans += distance
    print("#{} {}".format(test_case + 1, round(ans * E)))