import sys
sys.stdin = open("D5_4740_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

def delete():
    pass

def up(arr):
    chk = False
    if len(set(data[0])) > 1:
        return
    for i in range(N - 1):
        for j in range(M):
            data[i][j] = data[i + 1][j]
    for i in range(M):
        data[- 1][i] = arr[i]
        if arr[i] == '#':
            chk = True

    if chk:
        for i in range(M):
            

def left():
    for i in range(N):
        for j in range(M):
            if data[i][j] == '#':
                for k in range(j + 1, M):
                    if data[i][k] != '#':
                        data[i][j], data[i][k] = data[i][k], data[i][j]
                        break


def right():
    for i in range(N):
        for j in range(M - 1, - 1, - 1):
            if data[i][j] == '#':
                for k in range(j - 1, - 1, - 1):
                    if data[i][k] != '#':
                        data[i][j], data[i][k] = data[i][k], data[i][j]
                        break


T = int(input())
for test_case in range(1):
    N, M, Q = map(int, input().split())
    data = [list(map(str, input())) for _ in range(N)]

    for _ in range(Q):
        q = list(map(str, input()))
        if q == 'D':
            pass
        elif q == 'L':
            left()
        elif q == 'R':
            right()
        else:
            up(q[2:])

    for i in data:
        print(''.join(i))
    print()