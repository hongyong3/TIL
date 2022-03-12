import sys
sys.stdin = open("D2_12712_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]
dxi = [- 1, - 1, 1, 1]
dyj = [- 1, 1, - 1, 1]
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            plus = cross = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    nx = i + p * dx[k]
                    ny = j + p * dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        plus += arr[nx][ny]
                    else:
                        break
                for c in range(1, M):
                    nxi = i + c * dxi[k]
                    nyj = j + c * dyj[k]
                    if 0 <= nxi < N and 0 <= nyj < N:
                        cross += arr[nxi][nyj]
                    else:
                        break
            ans = max(ans, plus, cross)
    print("#{} {}".format(test_case + 1, ans))