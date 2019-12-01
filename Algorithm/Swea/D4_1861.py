import sys
sys.stdin = open("D4_1861_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def dfs(x, y):
    global count, ans, num
    if count <= ans:
        count = ans
        return

    for _ in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if data[nx][ny] == data[x][y] + 1:
            count += 1


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, count, num = 0, 0, 0
    for i in range(N):
        for j in range(N):
            dfs(i, j)
    print(data)