import sys
sys.stdin = open("D3_1873_input.txt", "r")

def start(i):
    if i == "S":
        shoot()
        return
    move(i)

def move(i):
    global x, y
    nx, ny = x, y
    if i == "U":
        nx -= 1
        dir = "^"
    if i == "D":
        nx += 1
        dir = "v"
    if i == "L":
        ny -= 1
        dir = "<"
    if i == "R":
        ny += 1
        dir = ">"

    if nx < 0: nx = 0
    if ny < 0: ny = 0
    if nx >= H: nx = H - 1
    if ny >= W: ny = W - 1

    if data[nx][ny] == ".":
        data[x][y] = "."
        data[nx][ny] = dir
        x, y = nx, ny
        return
    data[x][y] = dir

def shoot():
    global x, y
    nx, ny, dx, dy = x, y, 0, 0
    if data[x][y] == '^': dx = - 1
    if data[x][y] == 'v': dx = 1
    if data[x][y] == '<': dy = - 1
    if data[x][y] == '>': dy = 1

    while True:
        nx += dx
        ny += dy
        if not (0 <= nx < H and 0 <= ny < W): return
        if data[nx][ny] == "#": return
        if data[nx][ny] == "*":
            data[nx][ny] = "."
            return

T = int(input())
for test_case in range(T):
    H, W = map(int,input().split())
    data = [list(map(str, input())) for _ in range(H)]
    N, cmd = int(input()), str(input())
    x, y, dir = 0, 0, ""
    for i in range(H):
        for j in range(W):
            if data[i][j] == "<" or data[i][j] == ">" or data[i][j] == "v" or data[i][j] == "^":
                dir = data[i][j]
                x, y = i, j
                break
    for i in cmd:
        start(i)
    print("#{} ".format(test_case + 1), end="")
    for i in data:
        print(''.join(i))