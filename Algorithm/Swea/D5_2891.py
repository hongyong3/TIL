import sys
sys.stdin = open("D5_2891_input.txt", "r")

def printSudoku():
    for i in range(6):
        for j in range(6):
            if ans[i][j][1] == 10:
                ans[i][j][0] = ' '
            else:
                ans[i][j][0] = '/'
                ans[i][j][1] = ' '
        print('\n')


def getRow(i):
    if not i or i == 1:
        return 0
    elif i == 2 or i == 3:
        return 2
    else:
        return 4


def getCol(j):
    if not j or j == 1 or j == 2:
        return 0
    else:
        return 3


def chk(r, c, p, number):
    row, col, box, dist = 1, 1, 1, 1

    for i in range(6):
        if ans[i][c][0] == number or ans[i][c][1] == number:
            row = 0
            break

    for j in range(6):
        if ans[r][j][0] == number or ans[r][j][1] == number:
            col = 0
            break

    rr = getRow(r)
    cc = getCol(c)

    for i in range(rr, rr + 2):
        for j in range(cc, cc  + 3):
            if ans[i][j][0] == number or ans[i][j][1] == number:
                box = 0
                break
        if not box:
            break

    if not p and ans[r][c][1] != 0:
        if number > ans[r][c][1]:
            dist = 0

    if p == 1:
        if ans[r][c][0] > number:
            dist = 0

    if row and col and box and dist:
        return 1
    else:
        return 0


def dfs(ind, cnt):
    if cnt == len(v):
        printSudoku()
        return
    # x, y, p = v.pop()
    x, y, p = v[ind][0], v[ind][1], v[ind][2]

    for k in range(1, 10):
        if not p and k == 1:
            continue

        if chk(x, y, p, k):
            if not p:
                ans[x][y][0] = k
            else:
                ans[x][y][1] = k

            dfs(ind + 1, cnt + 1)

            if not p:
                ans[x][y][0] = 0
            else:
                ans[x][y][1] = 0

T = int(input())
for test_case in range(1):
    data = [input().split() for _ in range(6)]
    ans = [[''] * 6 for _ in range(6)]

    v = []
    for i in range(6):
        for j in range(6):
            if len(data[i][j]) == 3:    # 분수
                t, b = 0, 0 # 0은 빈칸
                if data[i][j][0] == '-':
                    v.append([i, j, 0])
                else:
                    t = int(data[i][j][0])

                if data[i][j][2] == '-':
                    v.append([i, j, 0])
                else:
                    b = int(data[i][j][2])
                ans[i][j] = [t, b]

            else:   # 정수
                if data[i][j] == '-':
                    ans[i][j] = [0, 10] # 10은 정수
                    v.append([i, j, 0])
                else:
                    ans[i][j] = [int(data[i][j]), 10]
    dfs(0, 0)