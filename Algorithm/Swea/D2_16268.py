import sys
sys.stdin = open("D2_16268_input.txt", "r")

dx = [- 1, 1, 0, 0, 0]
dy = [0, 0, 0, - 1, 1]
def dfs(x, y):
    temp = 0
    for k in range(5):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            temp += arr[nx][ny]
    return temp

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(dfs(i, j), ans)
    print("#{} {}".format(test_case + 1, ans))