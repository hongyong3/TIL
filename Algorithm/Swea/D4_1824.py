import sys
sys.stdin = open("D4_1824_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]


def solve(x, y):
    global memory, nx, ny

    if data[x][y] == '>' or '<' or '^' or 'v':
        if data[x][y] == '>':
            nx = x + dx[3]
            ny = y + dy[3]
        elif data[x][y] == '<':
            nx = x + dx[2]
            ny = y + dy[2]
        elif data[x][y] == '^':
            nx = x + dx[0]
            ny = y + dy[0]
        elif data[x][y] == 'v':
            nx = x + dx[1]
            ny = y + dy[1]
        solve(nx, ny)

    




T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    data = [list(input()) for _ in range(R)]
    memory = int(data[0][0])
    nx, ny = 0, 0
    solve(0.1)


    print("#{} {}".format(test_case + 1, "YES"))
    print("#{} {}".format(test_case + 1, "NO"))