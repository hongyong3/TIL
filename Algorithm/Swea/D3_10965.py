import sys
sys.stdin = open("D3_10965_input.txt", "r")

# Runtime error
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = 1
#     arr = dict()
#     while N >= 2:
#         for i in range(2, N + 1):
#             if not N % (i * i):
#                 if i not in arr:
#                     arr[i * i] = 1
#                 else:
#                     arr[i * i] += 1
#                 break
#         N //= (i * i)
#
#     for key, val in arr.items():
#         if val % 2:
#             ans *= key
#     print("#{} {}".format(test_case + 1, ans))

# Runtime Error 15002 // 100000
# ..??
T = int(input())
for test_case in range(1):
    N = int(input())
    a, b = 4, 2
    while a <= N:
        if not N % a:
            N //= a
        else:
            b += 1
            a = b * b
    print("#{} {}".format(test_case + 1, N))