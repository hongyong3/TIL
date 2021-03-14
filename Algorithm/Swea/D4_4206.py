import sys
sys.stdin = open("D4_4206_input.txt", "r")

# 13 / 16
dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 3:
                return True
    return False

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    virArr, samArr = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
    vir, sam = [], []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                vir.append((i, j))
                virArr[i][j] = 1
            elif arr[i][j] == 3:
                sam.append((i, j, 0))
                samArr[i][j] = 1

    ans, chk = 0, False

    while True:
        if not vir and not sam:
            break
        # 삼성이
        for _ in range(len(sam)):
            x, y, cnt = sam.pop()
            if arr[x][y] == 2:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (0 <= nx < N and 0 <= ny < M):
                    ans = cnt + 1
                    chk = True
                    break
                if virArr[nx][ny]:
                    continue
                if samArr[nx][ny]:
                    continue
                if arr[nx][ny]:
                    continue
                samArr[nx][ny] = 1
                arr[nx][ny] = 3
                sam.append((nx, ny, cnt + 1))
        if chk:
            break
        # 바이러스
        for _ in range(len(vir)):
            x, y = vir.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if virArr[nx][ny]:
                    continue
                if arr[nx][ny] == 1:
                    continue
                virArr[nx][ny] = 1
                arr[nx][ny] = 2
                vir.append((nx, ny))

    if chk:
        print("#{} {}".format(test_case + 1, ans))
    else:
        if check():
            print("#{} CANNOT ESCAPE".format(test_case + 1))
        else:
            print("#{} ZOMBIE".format(test_case + 1))