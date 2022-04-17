import sys
sys.stdin = open("D5_13550_input.txt", "r")

# 2808 / 1799854 Runtime Error
# T = int(input())
# for test_case in range(T):
#     a, d, n = map(int, input().split())
#     if n % 2:
#         a1 = a
#         an = a + (n - 1) * d
#         am = (a1 + an) // 2
#         m = am
#         for i in range(n // 2, 0, - 1):
#             am *= (m + i * d) * (m - i * d)
#             am %= 1000003
#     else:
#         a2 = a + d
#         an = a + (n - 1) * d
#         am = (a2 + an) // 2
#         m = am
#         for i in range(n // 2 - 1, 0, - 1):
#             am *= (m + i * d) * (m - i * d)
#             am %= 1000003
#         am *= a
#         am %= 1000003
#     print("#{} {}".format(test_case + 1, am))


# 306 / 1799854 Runtime Error
# mod = 1000003
# T = int(input())
# for test_case in range(T):
#     a, d, n = map(int, input().split())
#     x = a + (n // 2) * d
#     if n % 2:   # 홀수
#         ans = x
#         for i in range(1, n // 2 + 1):
#             ans *= (x * x - i * i * d * d) % mod
#             ans %= mod
#     else:   # 짝수
#         ans = a * x
#         for i in range(1, n // 2):
#             ans *= (x * x - i * i * d * d) % mod
#             ans %= mod
#     print("#{} {}".format(test_case + 1, ans))


# 36 / 1799854 Runtime Error
# T = int(input())
# for test_case in range(T):
#     a, d, n = map(int, input().split())
#     x = a + n // 2 * d
#     ans = x
#     idx = n // 2 + 1 if n % 2 else n // 2
#     for i in range(1, idx):
#         ans *= (x ** 2 - i * i * d * d)
#         ans %= 1000003
#     print("#{} {}".format(test_case + 1, ans))


# 0 / 1799854 Runtime Error
# T = int(input())
# arr = []
# for test_case in range(T):
#     a, d, n = map(int, input().split())
#     n %= 1000003
#     if n % 2:
#         a1 = a
#         an = a + (n - 1) * d
#         am = (a1 + an) // 2
#         m = am
#         for i in range(n // 2, 0, - 1):
#             am *= (m + i * d) * (m - i * d)
#             am %= 1000003
#     else:
#         a2 = a + d
#         an = a + (n - 1) * d
#         am = (a2 + an) // 2
#         m = am
#         for i in range(n // 2 - 1, 0, - 1):
#             am *= (m + i * d) * (m - i * d)
#             am %= 1000003
#         am *= a
#         am %= 1000003
#     arr.append(("#{} {}".format(test_case + 1, am)))
#
# for i in arr:
#     print(i)

# 2808 / 1799854 Runtime Error
mod = 1000003
T = int(input())
for test_case in range(T):
    a, d, n = map(int, input().split())
    n %= mod
    if n % 2:
        a1 = a
        an = a + (n - 1) * d
        am = (a1 + an) // 2
        m = am
        for i in range(n // 2, 0, - 1):
            am *= (m + i * d) * (m - i * d) % mod
            am %= mod
    else:
        a2 = a + d
        an = a + (n - 1) * d
        am = (a2 + an) // 2
        m = am
        for i in range(n // 2 - 1, 0, - 1):
            am *= (m + i * d) * (m - i * d) % mod
            am %= mod
        am *= a
        am %= 1000003
    print("#{} {}".format(test_case + 1, am % mod))

T = int(input())
for test_case in range(T):
    a, d, n = map(int, input().split())
    n %= 1000003
    if n % 2:
        a1 = a
        an = a + (n - 1) * d
        am = (a1 + an) // 2
        m = am
        for i in range(n // 2, 0, - 1):
            am *= (m + i * d) * (m - i * d)
            am %= 1000003
    else:
        a2 = a + d
        an = a + (n - 1) * d
        am = (a2 + an) // 2
        m = am
        for i in range(n // 2 - 1, 0, - 1):
            am *= (m + i * d) * (m - i * d)
            am %= 1000003
        am *= a
        am %= 1000003
    print("#{} {}".format(test_case + 1, am))