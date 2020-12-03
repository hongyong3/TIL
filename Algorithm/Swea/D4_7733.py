import sys
sys.stdin = open("D4_7733_input.txt", "r")

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, day, total = 1, 1, N * N
    visited = [[0] * N for _ in range(N)]

    while total:
        if N % 2:
            if ans == N * N // 2 + 1:
                break
        else:
            if ans == N * N // 2:
                break

        for x in range(N):
            for y in range(N):
                visited[x][y] = 0
                if data[x][y] == day:
                    data[x][y] = 0
                    total -= 1

        if not total:
            break

        temp = 0

        for x in range(N):
            for y in range(N):
                if data[x][y] and not visited[x][y]:
                    dfs(x, y)
                    temp += 1

        if ans < temp:
            ans = temp

        day += 1

    print("#{} {}".format(test_case + 1, ans))