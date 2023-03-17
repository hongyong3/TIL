import sys
sys.stdin = open("D2_9490_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N):
        for y in range(M):
            temp = arr[x][y]
            num = arr[x][y]
            for k in range(1, num + 1):
                for l in range(4):
                    nx = x + dx[l] * k
                    ny = y + dy[l] * k
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]

            ans = max(ans, temp)
    print("#{} {}".format(test_case + 1, ans))