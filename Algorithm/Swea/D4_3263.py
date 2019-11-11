import sys
sys.stdin = open("D4_3263_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    count, dp, array = 0, [0] * N, [0] * N
    dp[0] = 1
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if array[j] < array[i] and dp[j] + 1> dp[i]:
                dp[i] = dp[j] + 1

    for i in range(1, N):
        if count < dp[i]:
            count = dp[i]
    print(count)
    # print(N - count)