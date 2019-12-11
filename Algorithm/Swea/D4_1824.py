import sys
sys.stdin = open("D4_1824_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]


def solve(x, y):
    global memory, dir

    if data[x][y] == '>' or '<' or '^' or 'v':
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




T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    data = [list(input()) for _ in range(R)]
    memory = int(data[0][0])
    dir = 0
    # nx, ny = 0, 0
    solve(0, 1)


    print("#{} {}".format(test_case + 1, "YES"))
    print("#{} {}".format(test_case + 1, "NO"))