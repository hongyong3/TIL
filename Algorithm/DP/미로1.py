import sys
sys.stdin = open("미로1_input.txt", "r")

def dfs(x, y):
    global data, visited
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 < new_x <= M and 0 < new_y <= M:
            if data[new_x][new_y] == 2:
                flag = 1
            if data[new_x][new_y] == 0:
                data[new_x][new_y] = 9
                dfs(new_x, new_y)
        return flag


for test_case in range(1):
    N = int(input())
    M = 16
    data = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0 for _ in range(M)] for _ in range(M)]
    x, y, flag = 1, 1, 0
    print("#{} {}".format(test_case+1, flag))