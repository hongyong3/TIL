import sys
sys.stdin = open("D4_10571_input.txt", "r")

# dx = [1, 0] # 하 우
# dy = [0, 1]
#
# def dfs(x, y):
#     global visited
#     num = data[x][y]
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]

# runtime error...
T = int(input())
for test_case in range(2):
    N, M = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    ans = "YES"
    for i in range(N):
        num = data[i][0]
        visited[i][0] = 1
        for j in range(1, M):
            if data[i][j] == num:
                visited[i][j] = 1
            elif data[i][j] < num:
                visited[i][j] = 2

    for i in range(M):
        num = data[0][i]
        visited[0][i] = 1
        for j in range(1, N):
            if data[j][i] == num:
                visited[j][i] = 1
            elif data[j][i] < num:
                if visited[j][i] == 1:
                    pass
                elif visited[j][i] == 2:
                    visited[j][i] = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                ans = "NO"
                break
    print("#{} {}".format(test_case + 1, ans))