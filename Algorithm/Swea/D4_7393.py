import sys
sys.stdin = open("D4_7393_input.txt", "r")


# Runtime Error..
dp = [[[0] * 1024 for _ in range(10)] for _ in range(105)]
mod = 1000000000

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0

    for j in range(1, 10):
        dp[1][j][1 << (9 - j)] = 1

    for i in range(2, N + 1):
        for j in range(10):
            for k in range(1, 1024):
                if not (k & (1 << (9 - j))):
                    continue

                if j != 0:
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][k]) % mod
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][k ^ 1 << (9 - j)]) % mod

                if j != 9:
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j + 1][k]) % mod
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j + 1][k ^ 1 << (9 - j)]) % mod

    for j in range(10):
        ans = (ans + dp[N][j][1023]) % mod

    print("#{} {}".format(test_case + 1, ans))