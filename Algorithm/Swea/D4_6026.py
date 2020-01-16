import sys
sys.stdin = open("D4_6026_input.txt", "r")

def factorial(m):
    ans = 1
    for i in range(1, m + 1):
        ans *= i
    return ans

def partition_memo(n, m):
    if n == m or m == 1:
        memo[n][m] = 1

    if not memo[n][m]:
        memo[n][m] = m * partition_memo(n - 1, m) + partition_memo(n - 1, m - 1)
    return memo[n][m]

memo = [[0] * 101 for _ in range(101)]
T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    print("#{} {}".format(test_case + 1, partition_memo(N, M) * factorial(M) % 1000000007))