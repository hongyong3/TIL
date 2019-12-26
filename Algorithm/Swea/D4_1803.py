import sys
sys.stdin = open("D4_1803_input.txt", "r")

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
    N, M, v, e = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    print(data)
    graph, parent, rank, ans = list(range(1, N + 1)), {}, {}, 0
    for i in range(M):
        data[i] = [data[i][2], data[i][0], data[i][1]]
    for i in kruskal():
        ans += i[0]
    print("#{} {}".format(test_case + 1, ans))