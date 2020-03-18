import sys
sys.stdin = open("D2_4828_input.txt", "r")

# 예전 풀이
# T = int(input())
# for test_case in range(1, T + 1):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     for i in range(len(data) - 1, 0, -1):
#         for j in range(0, i):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#                 ans = data[-1] - data[0]
#     print("#{} {}".format(test_case, ans))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N - 1, 0, - 1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    print("#{} {}".format(test_case + 1, max(data) - min(data)))
    print("#{} {}".format(test_case + 1, data[- 1] - data[0]))