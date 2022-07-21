import sys
sys.stdin = open("D1_14540_input.txt", "r")

T = int(input())
dp = [[0] * 1001 for _ in range(1001)]
mod = 1000000007
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif arr[i - 1][j - 1] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
    print("#{} {}".format(test_case + 1, dp[N][M]))