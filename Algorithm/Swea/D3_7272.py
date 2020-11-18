import sys
sys.stdin = open("D3_7272_input.txt", "r")

# zero = "CEFGHIJKLMNSTUVWXYZ"
# one = "ADOPQR"
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(str, input().split())
#     ans = "DIFF"
#     if len(N) == len(M):
#         for i in range(len(N)):
#             if (N[i] in zero and M[i] in zero) or (N[i] in one and M[i] in one) or (N[i] == 'B' and M[i] == 'B'):
#                 continue
#             else:
#                 ans = "DIFF"
#                 break
#         else:
#             ans = "SAME"
#     print("#{} {}".format(test_case + 1, ans))

alpha = [0] * 26
for i in "ADOPQR":
    alpha[ord(i) - 65] = 1
alpha[ord('B') - 65] = 2

T = int(input())
for test_case in range(T):
    N, M = map(str, input().split())
    ans = "DIFF"
    if len(N) == len(M):
        for i in range(len(N)):
            if alpha[ord(N[i]) - 65] != alpha[ord(M[i]) - 65]:
                break
        else:
            ans = "SAME"
    print("#{} {}".format(test_case + 1, ans))