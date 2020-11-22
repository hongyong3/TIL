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
#             if not N % i * i:
#                 if i not in arr:
#                     arr[i * i] = 1
#                 else:
#                     arr[i * i] += 1
#                 break
#         N //= i * i
#
#     for key, val in arr.items():
#         if val % 2:
#             ans *= key
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 1
    for i in range(1, N):
        if (i + 1) * (i + 1) > N and (i + 1) * (i + 1) % N == 0:
            ans = (i + 1) * (i + 1) // N
            break