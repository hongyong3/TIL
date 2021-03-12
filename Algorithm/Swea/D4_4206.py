import sys
sys.stdin = open("D4_4206_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    virArr, vir = [[0] * M for _ in range(N)], []
    samArr, sam = [[0] * M for _ in range(N)], []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                vir.append((i, j))
                virArr[i][j] = 1
            elif arr[i][j] == 3:
                sam.append((i, j, 0))
                samArr[i][j] = 1
    ans = 0
    chk = False
    while sam and vir:
        for _ in range(len(sam)):
            x, y, cnt = sam.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if not (0 <= nx < N and 0 <= ny < M):
                    ans = cnt + 1
                    chk = True
                    break

                if virArr[nx][ny] or samArr[nx][ny] or arr[nx][ny]:
                    continue

                arr[nx][ny] = 3
                samArr[nx][ny] = 1
                sam.append((nx, ny, cnt + 1))
        if chk:
            break

        for _ in range(len(vir)):
            x, y = vir.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                

