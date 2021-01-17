import sys
sys.stdin = open("D3_11315_input.txt", "r")

dx = [1, 0, - 1, 1] # 히, 우, 우상, 우하,
dy = [0, 1, 1, 1]

def dfs(x, y, cnt):
    global ans
    if cnt == 5:
        ans = "YES"


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 'o':
            # 한 방향으로만 갈 수 있도록 ex) while이라던가 방향을 고정하기...
            # 가로, 세로, 우상, 우하
            pass



T = int(input())
for test_case in range(T):
    N = int(input())
    data = [input() for _ in range(N)]
    ans = "NO"

    for i in range(N):
        for j in range(N):
            if data[i][j] == 'o':
                dfs(i, j, 0)
    print("#{} {}".format(test_case + 1, ans))