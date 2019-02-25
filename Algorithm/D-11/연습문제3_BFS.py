def bfs(v):
    global G, V
    visited = [0] * (V+1)
    queue = []
    queue.append(v)
    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(V+1):
                if arr[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


import sys
sys.stdin = open("연습3_input.txt", "r")
V, E = map(int, input().split())

data = list(map(int, input().split()))
arr = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화

for i in range(0, len(data), 2):
    arr[data[i]][data[i+1]] = 1
    arr[data[i+1]][data[i]] = 1

for i in range(V+1): # 입력확인
    print("{} {}".format(i, arr[i]))

bfs(1)