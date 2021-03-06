import sys
sys.stdin = open("D6_1260_input.txt", "r")

def search(x, y):
    global mat
    dx, dy = 0, 0
    while x + dx < N and data[x + dx][y]:
        dx += 1
    while y + dy < N and data[x][y + dy]:
        dy += 1

    for i in range(x, x + dx):
        for j in range(y, y + dy):
            data[i][j] = 0
    mat.append(dx)
    mat.append(dy)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    n, s, mat = 0, [], []

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                search(i, j)

    while mat:
        for i in range(len(mat) // 2):
            if mat.count(mat[2 * i]) == 1:
                s.append([mat.pop(2 * i), mat.pop(2 * i)])
                n += 1
                break

    dp = [[0] * n for i in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            x = i + j
            dp[j][x] = float('inf')
            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])
    print("#{} {}".format(test_case + 1, dp[0][- 1]))