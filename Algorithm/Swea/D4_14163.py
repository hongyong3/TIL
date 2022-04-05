import sys
sys.stdin = open("D4_14163_input.txt", "r")

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x] += 1

def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    for i in range(M):
        union(data[2 * i], data[2 * i + 1])
    ans = 0
    for i in range(1, N + 1):
        if i == parent[i]:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))