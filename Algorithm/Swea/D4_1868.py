import sys
sys.stdin = open("D4_1868_input.txt", "r")

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def boom(x, y):
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N and 0 <= ny < N) and data[nx][ny] != - 1:
            data[nx][ny] += 1

def dfs(x, y):
    data[x][y] = - 2
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N and 0 <= ny < N):
            if not data[nx][ny]:
                dfs(nx, ny)
            data[nx][ny] = - 2

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if data[x][y] == '*':
                data[x][y] = - 1
            else:
                data[x][y] = 0

    for x in range(N):
        for y in range(N):
            if data[x][y] == - 1:
                boom(x, y)

    for x in range(N):
        for y in range(N):
            if not data[x][y]:
                count += 1
                dfs(x, y)

    for x in range(N):
        for y in range(N):
            if data[x][y] > 0:
                count += 1
    print("#{} {}".format(test_case + 1, count))