import sys
sys.stdin = open("D3_10726_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    num = bin(M)[2:][:: - 1][:N]
    print("#{} {}".format(test_case + 1, "ON" if len(num) >= N and not num.count('0') else "OFF"))

# 다르게 생각해본것..
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     num = M - 2 ** N + 1
#     ans = "OFF"
#     if num % 2 == 0:
#         if num >= 0:
#             ans = "ON"
#     print("#{} {}".format(test_case + 1, ans))
#     # print("#{} {}".format(test_case + 1, "ON" if num >= 0 and not num % 2 else "ON"))