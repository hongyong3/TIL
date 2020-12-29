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
# T = int(input())
# for test_case in range(1):
#     N = int(input())
#     a, b = 4, 2
#
#     while a <= N:
#         if not N % a:
#             N //= a
#         else:
#             b += 1
#             a = b * b
#     print("#{} {}".format(test_case + 1, N))

num = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for j in num:
        if not i % j:
            break
    else:
        num.append(i)

ans = []
T = int(input())
for test_case in range(T):
    N = int(input())
    res = 1
    if N ** 0.5 != int(N ** 0.5):
        for i in num:
            cnt = 0
            while not N % i:
                N //= i
                cnt += 1
            if cnt % 2:
                res *= i
            if N == 1 or i > N:
                break
        if N > 1:
            res *= N
    ans.append("#{} {}".format(test_case + 1, res))
for i in ans:
    print(i)