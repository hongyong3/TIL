import sys
sys.stdin = open("D5_11388_input.txt", "r")

mod = 1000000007
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


T = int(input())
for test_case in range(T):
    N, G = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans, dp = 0, [0] * 1001

    for i in arr:
        if not i % G:
            for j in range(1001):
                if dp[j]:
                    g = gcd(i, j)
                    dp[g] = (dp[g] + dp[j]) % mod
        dp[i] += 1
    print("#{} {}".format(test_case + 1, dp[G]))