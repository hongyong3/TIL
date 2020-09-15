import sys
sys.stdin = open("4248_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     data = list(map(int, input().split()))
#     dp = [0] * N
#
#     ans, s, temp = 0, 0, - 1
#     for i in range(N):
#         if temp == - 1 and data[i - 1] > data[i]:
#             temp = i
#
#         elif temp != - 1 and data[i - 1] > data[i]:
#             s = temp
#             temp = i
#
#         elif temp != - 1 and data[i - 1] <= data[i] and data[i - 2] > data[i]:
#             s = temp
#
#         l = i - s + 1
#         if l - K + 1 > 0:
#             dp[i] = (l - K + 1)
#
#     for i in range(N):
#         ans += dp[i]
#
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    dp = [0] * N
    s, temp = 0, - 1
    for i in range(N):
        if temp == - 1:
            if data[i - 1] > data[i]:
                temp = i

        else:
            if data[i] < data[i - 1]:
                s = temp
                temp = i
            elif data[i - 1] <= data[i] and data[i - 2] > data[i]:
                s = temp

        if i - s - K + 2 > 0:
            dp[i] = (i - s - K + 2)

    print(f"#{test_case + 1} {sum(dp)}")
    # print("#{} {}".format(test_case + 1, sum(dp)))