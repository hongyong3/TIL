import sys
sys.stdin = open("D6_5299_input.txt", "r")

# Bad Gate
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = 0
#
#     for b in range(2, N + 1):
#         num = N % b
#         x = N
#         chk = 1
#         while x:
#             if x % b != num:
#                 chk = 0
#                 break
#             x //= b
#         if chk:
#             ans = b
#             break
#
#     if not ans:
#         for i in range(1, N + 1):
#             if i * i <= N:
#                 if N % i:
#                     continue
#                 x = i
#                 base = N // x - 1
#                 if base > x:
#                     ans = base
#         ans = N + 1
#     print("#{} {}".format(test_case + 1, ans))

mul = [[0] * 28 for _ in range(32000)]
idxs = [0] * 28

for i in range(2, 1000000001):
    if i * i > 1000000000:
        break
    cnt = 0
    pd = i * i * i
    temp = i + 1 + i * i
    while temp <= 1000000000:
        mul[i][cnt] = temp
        idxs[cnt] = i
        cnt += 1
        temp += pd
        pd *= i

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0

    for b in range(1, N + 1):
        if b * b >= N:
            break
        if b + 1 > (N - b) // b:
            continue
        ans += (((N - b) // b) * (((N - b) // b) + 1)) // 2 - (b * (b + 1)) // 2

        for n in range(27):
            if mul[b + 1][n] * b > N:
                break
            l = b + 1
            r = idxs[n]
            cc = 0
            while l <= r:
                m = (l + r) // 2
                if mul[m][n] * b <= N:
                    cc = m
                    l = m + 1
                else:
                    r = m - 1
            if cc > 1:
                ans += (cc * (cc + 1)) // 2 - (b * (b + 1)) // 2
    print("#{} {}".format(test_case + 1, ans))