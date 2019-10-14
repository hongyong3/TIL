import sys
sys.stdin = open("D4_6109_input.txt", "r")

def upGame(x, y):
    ny = y - 1
    if ny >= 0:
        if data[ny][x] > 0:
            if data[ny][x] == data[y][x]:
                data[ny][x] == data[y][x] * 2
                data[y][x] = - 1
                return
            else:
                return
        elif data[ny][x] == - 1:
            data[ny][x] = data[y][x]
            data[y][x] = 0
            return
        else:
            data[ny][x] = data[y][x]
            data[y][x] = 0
            upGame(x, ny)
def downGame(x, y):
    ny = y + 1
    if ny < int(N):
        if data[ny][x] > 0:
            if data[ny][x] == data[y][x]:
                data[ny][x] == data[y][x] * 2
                data[y][x] = - 1
                return
            else:
                return
        elif data[ny][x] == - 1:
            data[ny][x] = data[y][x]
            data[y][x] = 0
            return
        else:
            data[ny][x] = data[y][x]
            data[y][x] = 0
            upGame(x, ny)
def leftGame(x, y):
    nx = x - 1
    if nx >= 0:
        if data[y][nx] > 0:
            if data[y][nx] == data[y][x]:
                data[y][nx] == data[y][x] * 2
                data[y][x] = - 1
                return
            else:
                return
        elif data[y][nx] == - 1:
            data[y][nx] = data[y][x]
            data[y][x] = 0
            return
        else:
            data[y][nx] = data[y][x]
            data[y][x] = 0
            upGame(nx, y)
def rightGame(x, y):
    nx = x + 1
    if nx < int(N):
        if data[y][nx] > 0:
            if data[y][nx] == data[y][x]:
                data[y][nx] == data[y][x] * 2
                data[y][x] = - 1
                return
            else:
                return
        elif data[y][nx] == - 1:
            data[y][nx] = data[y][x]
            data[y][x] = 0
            return
        else:
            data[y][nx] = data[y][x]
            data[y][x] = 0
            upGame(nx, y)

T = int(input())
for test_case in range(T):
    N, S = map(str, input().split())
    data = [list(map(int, input().split())) for _ in range(int(N))]
    if S == 'up':
        for j in range(int(N)):
            for i in range(int(N)):
                if data[j][i]:
                    upGame(i, j)
    if S == 'down':
        for j in range(int(N) - 1, - 1, - 1):
            for i in range(int(N)):
                if data[j][i]:
                    downGame(i, j)
    if S == 'left':
        for i in range(int(N)):
            for j in range(int(N)):
                if data[j][i]:
                    leftGame(i, j)
    if S == 'right':
        for i in range(int(N) - 1, - 1, - 1):
            for j in range(int(N)):
                if data[j][i]:
                    rightGame(i, j)

    for i in range(int(N)):
        for j in range(int(N)):
            if data[i][j] == - 1:
                data[i][j] = 0

    print("#{}".format(test_case + 1))
    for i in range(int(N)):
        print(' '.join(map(str, data[i])))