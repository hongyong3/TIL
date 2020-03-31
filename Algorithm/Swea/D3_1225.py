import sys
sys.stdin = open("D3_1225_input.txt", "r")

# 이전 풀이
# def solve(data):
#     while True:
#         for i in range(1, 6):
#             data[0] = data[0] - i
#             if data[0] < 1:
#                 data[0] = 0
#                 data.append(data.pop(0))
#                 return
#             data.append(data.pop(0))
#
# for test_case in range(10):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = 0
#     if min(data) > 15:
#         ans = min(data) // 15
#     for i in range(len(data)):
#         data[i] = data[i] - ((ans - 1) * 15)
#     solve(data)
#     print("#{}".format(test_case + 1), *data)

for test_case in range(10):
    N = int(input())
    data = list(map(int, input().split()))