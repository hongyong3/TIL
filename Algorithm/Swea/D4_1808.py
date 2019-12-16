import sys
sys.stdin = open("D4_1808_input.txt", "r")


def solve(num):
    if dp[num] != 0:
        return dp[num]

    dp[num] = count(num)

    for i in range(1, int(num ** 0.5)):
        if num % i == 0:
            num1 = solve(i)
            num2 = solve(num // i)
            if num1 == ans or num2 == ans:
                ans = num1 + num2
            dp[num] = min(dp[num], num1 == - 1 or num2 == - 1)
    return dp[num]

def count(num):
    cnt = 0
    while (num > 0):
        temp = num % 10
        if data[temp] == 0:
            return ans
        num /= 10
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1):
    data = list(map(int, input().split()))
    N = int(input())
    dp = [0] * (N + 10)
    ans = 0

    for i in range(10):
        if data[i] == 1:
            dp[i] = 1

    solve(N)