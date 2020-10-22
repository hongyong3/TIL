import sys
sys.stdin = open("D5_4740_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

def bfs(x, y, c, num):
    q = [(x, y)]
    visited[x][y] = num
    cnt = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and data[nx][ny] == c:
                    visited[nx][ny] = num
                    q.append((nx, ny))
                    cnt += 1
    return cnt


def delete():
    num, maxValue = 1, 0
    arr = []
    for i in range(N):
        for j in range(M):
            if data[i][j] != '#' and not visited[i][j]:
                temp = bfs(i, j, data[i][j], num)
                if temp > maxValue:
                    maxValue = temp
                    arr = [num]
                elif temp == maxValue:
                    arr.append(num)
                num += 1

    for k in range(len(arr)):
        for i in range(N):
            for j in range(M):
                if visited[i][j] == arr[k]:
                    data[i][j] = '#'
    drop()


def drop():
    for i in range(N - 1, - 1, - 1):
        for j in range(M):
            if data[i][j] == '#':
                for i in range(N - 1, 0, - 1):
                    data[i][j], data[i - 1][j] = data[i - 1][j], data[i][j]


def up(arr):
    chk = False
    if len(set(data[0])) > 1:
        return
    for i in range(N - 1):
        for j in range(M):
            data[i][j] = data[i + 1][j]
    for j in range(M):
        data[- 1][j] = arr[j]
        if arr[j] == '#':
            chk = True
    if chk:
        drop()


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
    visited = [[0] * M for _ in range(N)]

    for i in data:
        print(''.join(i))
    print()

    for _ in range(Q):
        q = list(map(str, input()))
        if q[0] == 'D':
            delete()
        elif q[0] == 'L':
            print(1)
            left()
        elif q[0] == 'R':
            right()
        else:
            up(q[2:])

    for i in data:
        print(''.join(i))