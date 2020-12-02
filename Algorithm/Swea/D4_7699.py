import sys
sys.stdin = open("D4_7699_input.txt", "r")

dx = [1, 0, - 1, 0] # 하 우 상 좌
dy = [0, 1, 0, - 1]

def dfs(x, y, cnt):
    global ans
    if ans == 26:
        return ans
    if ans < cnt:
        ans = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not alpha[ord(data[nx][ny]) - 65] and not visited[nx][ny]:
                visited[nx][ny] = 1
                alpha[ord(data[nx][ny]) - 65] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0
                alpha[ord(data[nx][ny]) - 65] = 0
    return ans


T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    data = [input() for _ in range(R)]

    ans = 1
    alpha = [0] * 26
    alpha[ord(data[0][0]) - 65] = 1
    visited = [[0] * C for _ in range(R)]
    visited[0][0] = 1
    print("#{} {}".format(test_case + 1, dfs(0, 0, 1)))