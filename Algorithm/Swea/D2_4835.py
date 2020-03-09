import sys
sys.stdin = open("D2_4835_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(1, T + 1):
#     ans = 0
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     x_min = 432443544560
#     x_max = 0
#     for i in range(N-M+1):
#         x = 0
#         for j in range((M)):
#             x += data[i+j]
#         if x_min > x:
#             x_min = x
#         if x_max < x:
#             x_max = x
#     ans = x_max - x_min
#     print("#{} {}".format(test_case, ans))

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    maxAns, minAns = 0, float('inf')
    for i in range(M, N + 1):
        temporaryNum = sum(data[i - M : i])
        if maxAns < temporaryNum:
            maxAns = temporaryNum
        if minAns > temporaryNum:
            minAns = temporaryNum
    print("#{} {}".format(test_case + 1, maxAns - minAns))