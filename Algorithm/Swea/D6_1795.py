import sys
sys.stdin = open("D6_1795_input.txt", "r")

def djikstra():
    dist[X] = 0
    q = []
    q.append([X, 0])
    while q:
        now, time = q.pop()
        if dist[now] > time:
            continue
        for i in range(len(graph[now])):
            there = graph[now][i][0]
            nextDist = graph[now][i][1] + time
            if dist[there] < nextDist:
                dist[there] = nextDist
                q.append([there, nextDist])

T = int(input())
for test_case in range(T):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [float('inf')] * (N + 1)
    ans = - 1
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([y, c])
    print(graph)
    djikstra()
    print(dist)