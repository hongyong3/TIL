import sys
sys.stdin = open("D3_1206_input.txt", "r")

# 이전 풀이
# T = 10
# for tc in range(10):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     for i in range(2,len(data)-1):
#         if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
#             ans += data[i] - max(data[i-1], data[i-2], data[i+1], data[i+2])
#     print("#{} {}".format(tc+1, ans))

# 방법 1
# for test_case in range(10):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     for i in range(2, N - 2):
#         if data[i] > data[i - 2] and data[i] > data[i - 1] and data[i] > data[i + 1] and data[i] > data[i + 2]:
#             ans += data[i] - max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
#     print("#{} {}".format(test_case + 1, ans))

# 방법 2
# for test_case in range(10):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     i = 2
#     while i < N - 2:
#         if data[i] == max(data[i - 2 : i + 3]):
#             ans += data[i] - max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
#             i += 3
#         else:
#             i += 1
#     print("#{} {}".format(test_case + 1, ans))