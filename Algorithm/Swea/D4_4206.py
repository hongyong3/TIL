import sys
sys.stdin = open("D4_4206_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

def check():
    for i in arr:
        if 3 in i:
            return True
    return False

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    samArr, sam = [[0] * M for _ in range(N)], []
    virArr, vir = [[0] * M for _ in range(N)], []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 3:
                sam.append((i, j, 0))
                samArr[i][j] = 1
            elif arr[i][j] == 2:
                vir.append((i, j))
                virArr[i][j] = 1

    ans, chk = 0, False

    while True:
        lv, ls = len(vir), len(sam)
        if not lv and not ls:
            break
        for _ in range(ls):
            x, y, time = sam.pop(0)
            if arr[x][y] == 2:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (0 <= nx < N and 0 <= ny < M):
                    ans = time + 1
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
                sam.append((nx, ny, time + 1))
        if chk:
            break
        for _ in range(lv):
            x, y = vir.pop(0)
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