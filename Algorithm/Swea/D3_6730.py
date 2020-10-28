import sys
sys.stdin = open("D3_6730_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans1, ans2 = 0, 0
    for i in range(N - 1):
        if data[i + 1] > data[i]:
            if data[i + 1] - data[i] > ans1:
                ans1 = data[i + 1] - data[i]
        else:
            if data[i] - data[i + 1] > ans2:
                ans2 = data[i] - data[i + 1]
    print("#{} {} {}".format(test_case + 1, ans1, ans2))

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans1, ans2 = 0, 0
#     for i in range(N - 1):
#         temp = data[i + 1] - data[i]
#         if temp > ans1:
#             ans1 = temp
#         if temp < ans2:
#             ans2 = temp
#     print("#{} {} {}".format(test_case + 1, ans1, - ans2))