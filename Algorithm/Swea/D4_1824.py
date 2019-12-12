import sys
sys.stdin = open("D4_1824_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]


def solve(x, y, dir, depth):
    global memory, R, C
    ans = 0

    if data[x][y] == '>' or (data[x][y] == '_' and memory == 0):
        dir = 3
    elif data[x][y] == '<' or (data[x][y] == '_'):
        dir = 2
    elif data[x][y] == '^' or (data[x][y] == '|'):
        dir = 0
    elif data[x][y] == 'v' or (data[x][y] == '|' and memory == 0):
        dir = 1
    elif data[x][y] == '+':
        memory = (memory + 1) % 16
    elif data[x][y] == '-':
        if memory == 0:
            memory = 15
        else:
            memory = memory - 1
    elif data[x][y] == '@':
        return True

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx == 0:
        nx = R
    elif nx == R + 1:
        nx = 1

    if ny == 0:
        ny = R
    elif ny == C + 1:
        ny = 1

    if data[x][y] == '?':
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if nx == 0:
                nx = R
            elif nx == R + 1:
                nx = 1

            if ny == 0:
                ny = R
            elif ny == C + 1:
                ny = 1

            ans = max(solve(nx, ny, i, depth + 1), ans)

        return ans

    else:
        return max(solve(nx, ny, dir, depth + 1), ans)

T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    data = [list(input()) for _ in range(R)]
    memory = int(data[0][0])
    solve(0, 1, 0, 0)


    print("#{} {}".format(test_case + 1, "YES"))
    print("#{} {}".format(test_case + 1, "NO"))