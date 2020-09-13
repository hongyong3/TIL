import sys
sys.stdin = open("D5_2891_input.txt", "r")

def printSudoku():
    print("#{}".format(test_case + 1))
    for i in range(6):
        for j in range(6):
            if mat[i][j][1] == 10:
                print(str(mat[i][j][0]), end =' ')
            else:
                print(str(mat[i][j][0]) + '/' + str(mat[i][j][1]), end =' ')
        print()


def getRow(i):
    if i == 0 or i == 1:
        return 0
    elif i == 2 or i == 3:
        return 2
    else:
        return 4


def getCol(j):
    if j <= 2:
        return 0
    else:
        return 3


def chk(r, c, p, number):
    row, col, box, dist = 1, 1, 1, 1

    for i in range(6):
        if mat[i][c][0] == number or mat[i][c][1] == number:
            row = 0
            break

    for j in range(6):
        if mat[r][j][0] == number or mat[r][j][1] == number:
            col = 0
            break

    rr = getRow(r)
    cc = getCol(c)

    for i in range(rr, rr + 2):
        for j in range(cc, cc  + 3):
            if mat[i][j][0] == number or mat[i][j][1] == number:
                box = 0
                break
        if not box:
            break

    if not p and mat[r][c][1] != 0:
        if number > mat[r][c][1]:
            dist = 0

    if p == 1:
        if mat[r][c][0] > number:
            dist = 0

    if row and col and box and dist:
        return 1
    else:
        return 0


def dfs(ind, cnt):
    if cnt == len(v):
        printSudoku()
        return
    x, y, p = v[ind][0], v[ind][1], v[ind][2]

    for k in range(1, 10):
        if p == 1 and k == 1:
            continue

        if check(x, y, p, k):
            if p == 0:
                mat[x][y][0] = k
            else:
                mat[x][y][1] = k

            dfs(ind + 1, cnt + 1)

            if p == 0:
                mat[x][y][0] = 0
            else:
                mat[x][y][1] = 0

T = int(input())
for test_case in range(T):
    data = [input().split() for _ in range(6)]
    mat = [[''] * 6 for _ in range(6)]
    v = []

    for i in range(6):
        for j in range(6):
            if len(data[i][j]) > 1:    # 분수
                if data[i][j][0] == '-':
                    t = 0
                    v.append([i, j, 0])
                else:
                    t = int(data[i][j][0])

                if data[i][j][2] == '-':
                    b = 0
                    v.append([i, j, 1])
                else:
                    b = int(data[i][j][2])

                mat[i][j] = [t, b]

            else:   # 정수
                if data[i][j] == '-':
                    mat[i][j] = [0, 10] # 10은 정수
                    v.append([i, j, 0])
                else:
                    mat[i][j] = [int(data[i][j]), 10]
    dfs(0, 0)