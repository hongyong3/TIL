import sys
sys.stdin = open("D4_12369_input.txt", "r")

# 19 / 20...
# T = int(input())
# for test_case in range(T):
#     S, N = input().split()
#     N, l = int(N), len(S)
#     total, temp = 0, 1
#     ans, arr = '', []
#
#     while True:
#         temp *= l
#         if N >= total + temp:
#             arr.append(temp)
#             total += temp
#         else:
#             diff = N - total
#             break
#
#     idx = len(arr)
#     if diff:
#         idx += 1
#     if idx == 1 and diff == 0:
#         ans = S
#     else:
#         for i in arr[:: -1]:
#             if diff == i:
#                 ans += S[0]
#                 diff -= i
#             else:
#                 mok, nam = diff // i, diff % i
#                 diff -= mok * i
#                 if mok == l or nam == 0:
#                     ans += S[- 1]
#                 else:
#                     ans += S[mok]
#         if diff == l:
#             ans += S[- 1]
#         else:
#             if len(ans) != idx:
#                 ans += S[diff - 1]
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    S, N = input().split()
    N, l = int(N), len(S)
    ans = ''
    if l == 1:
        print("#{} {}".format(test_case + 1, S * N))
        continue
    digit, temp = 1, l
    while True:
        digit += 1
        if temp + l ** (digit) >= N:
            break
        temp += l ** digit

    for i in range(digit - 1, - 1, - 1):
        idx = 0
        while temp + l ** i < N:
            temp += l ** i
            idx += 1
        ans += S[idx]
    print("#{} {}".format(test_case + 1, ans))