import sys
sys.stdin = open("D4_3263_input.txt", "r")

############################################# O(Nlog(N)
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    mat, DP = N, [0] * (N + 1)
    for i in data:
        DP[i] = DP[i - 1] + 1
        mat = min(mat, N - DP[i])
    print("#{} {}".format(test_case + 1, mat))

############################################# O(N^2) 시간초과
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     count, dp = 0, [0] * N
#     dp[0] = 1
#     for i in range(1, N):
#         dp[i] = 1
#         for j in range(i):
#             if data[j] < data[i] and dp[j] + 1> dp[i]:
#                 dp[i] = dp[j] + 1
#
#     for i in range(1, N):
#         if count < dp[i]:
#             count = dp[i]
#     print("#{} {}".format(test_case + 1, N - count))