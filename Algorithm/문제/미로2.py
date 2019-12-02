import sys
sys.stdin = open("미로2_input.txt", "r")

def bfs(x, y):
    global data, visited
    Q = []
    Q.append((x, y))
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while len(Q) != 0:
        x, y = Q.pop(0)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if visited[new_x][new_y] == 1: continue
            if data[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                Q.append((new_x, new_y))
            if data[new_x][new_y] == 3:
                return 1
    return 0

def findStart(data):
    for x in range(M):
        for y in range(M):
            if data[x][y] == 2:
                return x, y

for test_case in range(10):
    N = int(input())
    M = 100
    data = [[int(x) for x in input()] for _ in range(M)]
    visited = [[0 for _ in range(M)] for _ in range(M)]

    sx, sy = findStart(data)
    print("#{} {}".format(test_case+1, bfs(sx, sy)))