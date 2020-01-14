import sys
sys.stdin = open("D4_6026_input.txt", "r")

# def factorial(n):
#     if n == 1 :
#         return 1
#     else:
#         return n * factorial(n-1)
# T = int(input())
# for test_case in range(T):
#     M, N = map(int, input().split())
#     ans = 0
#     if M == N:
#         ans = factorial(M)
#     else:
#         ans = M ** N - factorial(M)
#     print("#{} {}".format(test_case + 1, ans % 1000000007))

# from collections import Counter
# def convert(n, base):
#     T = "0123456789ABCDEF"
#     q, r = divmod(n, base)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]
#
# T = int(input())
# for test_case in range(T):
#     M, N = map(int, input().split())
#     if N == M:
#         print("#{} {}".format(test_case + 1, 1))
#         continue
#     answer = pow(M, N)
#     for i in range(answer):
#         ans = pow(10, N) + int(convert(i, M))
#         if len(Counter(str(ans)[1:])) != M:
#             answer -= 1
#             answer %= 1000000007
#     print("#{} {}".format(test_case + 1, answer))

T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    if N == M:
        print("#{} {}".format(test_case + 1, 1))
        continue
    key = {}
    for i in range(M - 1, - 1, - 1):
        key[i] = i
    print(key)