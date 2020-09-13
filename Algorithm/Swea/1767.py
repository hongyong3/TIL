import sys
sys.stdin = open("1767_input.txt", "r")
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]  # 상 하 좌 우

def runCore(x, y, i, EA):
    global N
    count = 0
    while 1:
        x += dx[i]
        y += dy[i]
        if not (0 <= x < N and 0 <= y < N):
            return count
        if data[x][y] != 0:
            return
        count += 1
        data[x][y] = 99 + EA

def cellClear(x, y, i, EA):
    global N
    while 1:
        x += dx[i]
        y += dy[i]
        if not (0 <= x < N and 0 <= y < N):
            return
        if data[x][y] != 99 + EA:
            return
        data[x][y] = 0

def dfs(EA, length, core):
    global count, maxCore, minLength
    if EA == count:
        if core == maxCore:
            minLength = min(minLength, length)
        elif core > maxCore:
            maxCore = core
            minLength = length
        return
    x, y = mat[EA]
    for i in range(4):
        lineCount = runCore(x, y, i, EA)
        if lineCount:
            dfs(EA + 1, length + lineCount, core + 1)
        cellClear(x, y, i, EA)
    dfs(EA + 1, length, core)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat, count, maxCore, minLength = [], 0, 0, 999999999  # data[i][j] == 1, 코어의 수, 최대연결코어수, 전선의 길이 최소값

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if data[i][j]:
                mat.append([i, j])
                count += 1  # 코어의 수 // 전체 코어의 수는 아니라 가장자리를 제외한 코어의 수
    dfs(0, 0, 0)    # 코어 순서, 전선의 길이, 코어의 수
    print("#{} {}".format(test_case + 1, minLength))