import sys
sys.stdin = open("D3_11315_input.txt", "r")

dx = [0, 1, 1, - 1, 0, - 1, 1, - 1] # 우 하 우하 상 좌 우상 좌하 좌상
dy = [1, 0, 1, 0, - 1, 1, - 1, - 1]
T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = "NO"
    chk = False

    for x in range(N):
        if chk:
            break
        for y in range(N):
            if chk:
                break
            if arr[x][y] == 'o':
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
                    while 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] != 'o':
                            break
                        else:
                            cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                        if cnt == 5:
                            ans = "YES"
                            chk = True
                            break
    print("#{} {}".format(test_case + 1, ans))