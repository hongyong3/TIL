import sys
sys.stdin = open("1767_input.txt", "r")

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]  # 상 하 좌 우

def runCore(x, y, i, depth):    # 전선 길이구하는 함수
    global N
    count = 0
    while 1:
        x += dx[i]
        y += dy[i]
        if not (0 <= x < N and 0 <= y < N):
            return count
        if data[x][y] != 0:
            return 0
        count += 1
        data[x][y] = 99 + depth


def lineClear(x, y, i, depth):  # cell 초기화 시키는 함수
    global N
    while 1:
        x += dx[i]
        y += dy[i]
        if not (0 <= x < N and 0 <= y < N):
            return
        if data[x][y] != 99 + depth:
            return
        data[x][y] = 0

def dfs(depth, total, K):
    global count, maxCore, minSum

    if depth == count:
        if K == maxCore:
            minSum = min(minSum, total)
        elif K > maxCore:
            maxCore = K
            minSum = total
        return
    x, y = ans[depth]

    for i in range(4):
        lineCount = runCore(x, y, i, depth)
        if lineCount:
            dfs(depth + 1, total + lineCount, K + 1)
        lineClear(x, y, i, depth)   # 초기화
    dfs(depth + 1, total, K)

T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, count, maxCore, minSum = [], 0, 0, 999999999  # data[i][j] == 1, 코어의 수, 최대연결코어수, 전선의 길이 최소값

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if data[i][j]:
                ans.append([i, j])
                count += 1  # 코어의 수 // 전체 코어의 수는 아니라 가장자리를 제외한 코어의 수
    dfs(0, 0, 0)    # 코어 순서, 전선의 길이, 코어의 수
    print("#{} {}".format(test_case + 1, minSum))