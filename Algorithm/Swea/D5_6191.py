import sys
sys.stdin = open("D5_6191_input.txt", "r")

# 점화식 fn = 1 + N * (N - 1) // 2
# if K > f(N):
#     ans = ')('
#
#
#
# arr = [0] * 44722
# arr[1] = 1
# for i in range(2, 44722):
#     arr[i] = arr[i - 1] + i
#
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#
#     if K > 1 + N * (N - 1) // 2:
#         ans = ')('
#     else:
#         e = 44722
#         # for i in range(e):
#         #     if N <= arr[i]:
#         #         e = i
#         #         break
#         # s = arr[e] - N
#         # ans = ')' * (e - s) + '(' + ')' * s + '(' * (e - 1)
#

mat = [[0 for _ in range(101)] for _ in range(101)]
mat[0][0] = 1

for r in range(0, 101):
    mat[0][r] = 1
for l in range(1, 101):
    for i in range(0, l):
        mat[l][l] += mat[i][l - 1]
    for r in range(l + 1, 101):
        mat[l][r] = mat[l][r - 1] + mat[l - 1][r]

def bracket(l, r, k):
    if mat[l][r] <= k:
        return ")("
    if l == 0:
        return ")" * r
    if k < mat[l - 1][r]:
        return "(" + bracket(l - 1, r, k)
    else:
        k -= mat[l - 1][r]
        return ")" + bracket(l, r - 1, k)

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    print("#{} {}".format(test_case + 1, bracket(N, N, K - 1)))