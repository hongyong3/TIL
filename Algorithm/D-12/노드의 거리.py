def bfs(data, v):  # 1에서 가장 멀리 있는 정점을 찾으시오.
    global G
    queue=[]

    queue.append(v)  #enQueue하면서 방문처리
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if data[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
    result = 0
    if visited[G]:
        result = visited[G]-1

    print(f"#{test_case} {result}")


import sys
sys.stdin = open("노드의 거리_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V + 1)]
    for C in range(E):
        i, j = map(int, input().split())
        data[i][j] = 1
        data[j][i] = 1
    S, G = map(int, input().split())
    bfs(data, S)