import sys
sys.stdin = open("구슬 굴리기_input.txt", "r")

X, Y = map(int, input().split())
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
field = [(list(map(int, input()))) for _ in range(Y)]

def iswall(y, x):
    if Y-1 >= y > -1 and X-1 >= x > -1:
        return True
    else:
        return False

def movement(y, x, m):
    global cnt
    while True:
        ny = dy[move[m]] + y
        nx = dx[move[m]] + x
        if iswall(ny, nx) and field[ny][nx] != 1:
            if field[ny][nx] != 2:
                field[ny][nx] = 2
                x = nx
                y = ny
                start[0][0], start[0][1] = y, x
                cnt += 1
            else:
                x = nx
                y = ny
                start[0][0], start[0][1] = y, x
        else:
            break
    return cnt

cnt = 1
N = int(input())
move = list(map(int, input().split()))
start = []
for y in range(Y):
    for x in range(X):
        if field[y][x] == 2:
            start.append([y,x])

for m in range(N):
    movement(start[0][0], start[0][1], m)

print(cnt)