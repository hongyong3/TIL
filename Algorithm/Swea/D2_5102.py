import sys
sys.stdin = open("D2_5102_input.txt", "r")

def bfs(graph, s):
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        s = q.pop(0)
        for i in range(1, V + 1):
            if graph[s][i] and not visited[i]:
                q.append(i)
                visited[i] = visited[s] + 1
    ans = 0
    if visited[G]:
        ans = visited[G] - 1
    print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j], graph[j][i] = 1, 1
    S, G = map(int, input().split())
    bfs(graph, S)