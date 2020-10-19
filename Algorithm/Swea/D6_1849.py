import sys
sys.stdin = open("D6_1849_input.txt", "r")

from collections import defaultdict

def union(a, b, w):
    pa = find(a)
    pb = find(b)

    if pa == pb:
        return

    diff = weight[b] - weight[a]

    if rank[pa] > rank[pb]:
        pa, pb = pb, pa
        w = - w
        diff = - diff

    weight[pa] = w + diff
    parent[pa] = pb

    if rank[pa] == rank[pb]:
        rank[pb] += 1

def find(a):
    if not parent[a]:
        return a

    pa = parent[a]
    parent[a] = find(pa)
    weight[a] += weight [pa]

    return parent[a]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    parent = defaultdict(int)
    weight = defaultdict(int)
    rank = defaultdict(int)
    ans = []

    for _ in range(M):
        data = input()
        if data[0] == '!':
            a, b, w = map(int, data.split()[1:])
            union(a, b, w)
        else:
            a, b = map(int, data.split()[1:])
            if find(a) == find(b):
                ans.append(weight[a] - weight[b])
            else:
                ans.append("UNKNOWN")
    print("#{}".format(test_case + 1), *ans)