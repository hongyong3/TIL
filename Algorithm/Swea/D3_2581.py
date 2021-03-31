import sys
sys.stdin = open("D3_2581_input.txt", "r")

arr = [[1] * 2 for _ in range(37)]
board = [[' '] * 6200 for _ in range(6200)]

def solve():
    x = y = idx = cnt = 1
    board[1][1] = '*'

    for k in range(2, 37):
        if idx == 1:
            x += cnt + 1
            for i in range(1, y + 1):
                board[i][x] = '*'
            cnt += 1
        elif idx == 2:
            y += 1
            for j in range(1, x + 1):
                board[y][j] = '*'
        elif idx == 3:
            for i in range(1, y + 1):
                for j in range(1, x + 1):
                    board[i + y][j] = board[i][j]
            y *= 2

        arr[k][0] = y
        arr[k][1] = x
        idx += 1
        if idx == 4:
            idx = 1


T = int(input())
solve()
for test_case in range(T):
    N = int(input())
    print("#{}".format(test_case + 1))
    for i in range(1, arr[N][0] + 1):
        for j in range(1, arr[N][1] + 1):
            print(board[i][j], end = '')
        print()