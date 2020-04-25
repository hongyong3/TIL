import sys
sys.stdin = open("D5_1265_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, P = map(int, input().split())
#     mok, nam = N // P, N % P
#     data = [0] * P
#     ans = 1
#
#     for i in range(P):
#         data[i] = mok
#
#     while nam:
#         data[nam] += 1
#         nam -= 1
#
#     for i in data:
#         ans *= i
#
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, P = map(int, input().split())
    s, r = N // P, N % P
    ans = s ** (P - r) * (s + 1) ** r
    print("#{} {}".format(test_case + 1, ans))