import sys
sys.stdin = open("D2_5186_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(T):
#     N = float(input())
#     ans = []
#     while len(ans) <= 13:
#         if N*2 >= 1:
#             ans.append(1)
#             N = N*2 - 1
#             if len(ans) > 12:
#                 print("#{}".format(test_case + 1), end=" ")
#                 print("overflow")
#         elif 0 < N*2 < 1:
#             N = N*2
#             ans.append(0)
#             continue
#             if len(ans) > 12:
#                 print("#{}".format(test_case+1), end= " ")
#                 print("overflow")
#         elif N == 0:
#             print("#{}".format(test_case+1), end=" ")
#             for i in range(len(ans)):
#                 print(ans[i], end="")
#             print()
#             break

def binary(n):
    global mat
    if len(ans) >= 13:
        ans = 'overflow'
        return
    n *= 2
    if n > 1:
        ans += '1'
        binary(n - 1)
    elif n == 1:
        ans += '1'
        return
    else:
        ans += '0'
        binary(n)

T = int(input())
for test_case in range(T):
    N = float(input())
    mat = ''
    binary(N)
    print("#{} {}".format(test_case + 1, mat))