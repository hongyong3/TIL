import sys
sys.stdin = open("D4_12005_input.txt", "r")

# Runtime Error
# T = int(input())
# for test_case in range(T):
#     k, m = map(int, input().split())
#     if m + 1 == (k ^ 1) + 1:
#         print("#{} {}".format(test_case + 1, 1))
#         continue
#     else:
#         n, cnt = 2, 0
#         while True:
#             cnt = 0
#             if not n % 2:
#                 if n % 3:
#                     fnm = n + 2 * m - 1
#                 else:
#                     cnt = 0
#                     for i in range(n + 1, pow(10, 18), 2):
#                         if i % 2 and i % 3:
#                             cnt += 1
#                         if cnt == m:
#                             fnm = i
#                             break
#             else:
#                 for i in range(n + 1, pow(10, 18)):
#                     if i % n:
#                         cnt += 1
#                     if cnt == m:
#                         fnm = i
#                         break
#             if fnm == (n ^ k) + n:
#                 print("#{} {}".format(test_case + 1, n))
#                 break
#             n += 1

# Fail
# T = int(input())
# for test_case in range(T):
#     k, m = map(int, input().split())
#     if m + 1 == (k ^ 1) + 1:
#         print("#{} {}".format(test_case + 1, 1))
#         continue
#     else:
#         n, cnt = 2, 0
#         while n < 50:
#             cnt = 0
#             if not n % 2:
#                 if n % 3:
#                     fnm = n + 2 * m - 1
#                 else:
#                     cnt = 0
#                     for i in range(n + 1, pow(10, 18), 2):
#                         if i % 2 and i % 3:
#                             cnt += 1
#                         if cnt == m:
#                             fnm = i
#                             break
#             else:
#                 for i in range(n + 1, pow(10, 18)):
#                     if i % n:
#                         cnt += 1
#                     if cnt == m:
#                         fnm = i
#                         break
#             if fnm == (n ^ k) + n:
#                 break
#             n += 1
#     if n == 50:
#         n = - 1
#     print("#{} {}".format(test_case + 1, n))


# 와... 못 풀겠다...
# Runtime Error
T = int(input())
for test_case in range(T):
    k, m = map(int, input().split())
    ans = - 1
    if m + 1 == (k ^ 1) + 1:
        print("#{} {}".format(test_case + 1, 1))
        continue
    else:
        n, cnt = 2, 0
        while n < k * 2:
            cnt = 0
            if not n % 2:
                if n % 3:
                    fnm = n + 2 * m - 1
                else:
                    cnt = 0
                    for i in range(n + 1, pow(10, 18), 2):
                        if i % 2 and i % 3:
                            cnt += 1
                        if cnt == m:
                            fnm = i
                            break
            else:
                for i in range(n + 1, pow(10, 18)):
                    if i % n:
                        cnt += 1
                    if cnt == m:
                        fnm = i
                        break
            if fnm == (n ^ k) + n:
                ans = n
                break
            n += 1
    print("#{} {}".format(test_case + 1, ans))