import sys
sys.stdin = open("D4_6026_input.txt", "r")

memo = [[0] * 101 for _ in range(101)]

def partition_memo(n, m):
    if n == m or m == 1:
        memo[n][m] = 1

    if not memo[n][m]:
        memo[n][m]= m * partition_memo(n - 1, m) + partition_memo(n - 1, m - 1)
    return memo[n][m]



T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    partition_memo(N, M)
    # print("#{} {}".format(test_case + 1, ))