import sys
sys.stdin = open("미로1_input.txt", "r")

def dfs(x, y):
    global data, flag
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    data[x][y] = 9
    # visited[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < 0 or new_x == M: continue
        if new_y < 0 or new_y == M: continue
        if data[new_x][new_y] == 9: continue
        if data[new_x][new_y] == 1: continue
        if data[new_x][new_y] == 3:
            flag = 1
            return
        dfs(new_x, new_y)

def findStart(data):
    for x in range(M):
        for y in range(M):
            if data[x][y] == 2:
                return x, y

for test_case in range(10):
    N = int(input())
    M = 16
    flag = 0
    data = [[int(x) for x in input()] for _ in range(M)]
    visited = [[0 for _ in range(M)] for _ in range(M)]

    sx, sy = findStart(data)
    dfs(sx, sy)
    print("#{} {}".format(test_case+1, flag))