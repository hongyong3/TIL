import sys
sys.stdin = open("D4_1251_input.txt", "r")

# from collections import deque
#
# def isCycle(L, pair):
#     tempL = []
#     for i in L:
#         tempL.append(list(i))
#
#     myStack = deque([])
#     visitedNode = []
#     for i in tempL:
#         if pair[1] in i:
#             myStack.extend([pair[1]])
#             break
#
#     while myStack:
#         Node = myStack.pop()
#         visitedNode.extend([Node])
#         throwL = []
#         for i in tempL:
#             if Node in i:
#                 if pair[2] in i:
#                     return True
#                 throwL.append(i)
#                 if i[1] == Node:
#                     myStack.extend([i[2]])
#                 else:
#                     myStack.extend([i[1]])
#         for i in throwL:
#             tempL.remove(i)
#     return False
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(2)]
#     E = float(input())
#     ans = 0
#     kruscalL = []
#     graph = []  # 거리, 노드1 노드2
#
#     for i in range(N):
#         for j in range(i + 1, N):
#             distance = pow(data[0][i] - data[0][j], 2) + pow(data[1][i] - data[1][j], 2) ** (1.0 / 2.0)
#             graph.append([distance, i, j])
#     graph.sort()
#
#     for i in range(len(graph)):
#         if not isCycle(kruscalL, graph[i]):
#             kruscalL.append(graph[i])
#             ans += E * pow(graph[i][0], 2)
#
#         if len(kruscalL) == N - 1:
#             break
#     print("#{} {}".format(test_case + 1, round(ans)))

def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return  parent[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(edges):
    for v in range(N):
        make_set(v)
    mst = []
    for  edge in edges:
        distance, v, u = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return mst


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    parent = {}
    rank = {}
    edges = []  # 거리, 노드1, 노드2
    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            edges.append((pow(data[0][i] - data[0][j], 2) + pow(data[1][i] - data[1][j], 2), i, j))
    edges.sort()
    for i in range(len(kruskal(edges))):
        ans += kruskal(edges)[i][0] * E

    print("#{} {}".format(test_case + 1, round(ans)))