import sys
sys.stdin = open("practice_input.txt", "r")

import sys
input = sys.stdin.readline

# boj 11365
# while True:
#     s = input().rstrip()
#     if s == "END":
#         break
#     print(s[:: - 1])

# boj 20254
# ur, tr, uo, to = map(int, input().split())
# print(56 * ur + 24 * tr + 14 * uo + 6 * to)

# n = int(input())
# a = b = 100
# for _ in range(n):
#     x, y = map(int, input().split())
#     if x > y:
#         b -= x
#     elif x < y:
#         a -= y
# print(a)
# print(b)

# boj 21300
# print(5 * sum(list(map(int, input().split()))))

# boj 2864
# a, b = input().split()
# minA = maxA = minB = maxB = ''
# for i, j in zip(a, b):
#     if i in '56':
#         minA += '5'
#         maxA += '6'
#     else:
#         minA += i
#         maxA += i
#
#     if j in '56':
#         minB += '5'
#         maxB += '6'
#     else:
#         minB += j
#         maxB += j
# print(int(minA) + int(minB), int(maxA) + int(maxB))

# boj 2863
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# arr = [a / c + b / d, c / d + a / b, d / b + c / a, b / a + d / c]
# print(arr.index(max(arr)))

# boj 13420
# t = int(input())
# for _ in range(t):
#     arr = input().split()
#     if arr[1] == '+':
#         ans = int(arr[0]) + int(arr[2])
#     elif arr[1] == '-':
#         ans = int(arr[0]) - int(arr[2])
#     elif arr[1] == '*':
#         ans = int(arr[0]) * int(arr[2])
#     else:
#         ans = int(arr[0]) // int(arr[2])
#     if ans == int(arr[4]):
#         print("correct")
#     else:
#         print("wrong answer")

# n = int(input())
# for i in range(1, n):
#     print((n - i) * ' ' + i * '*')
# print(n * '*')
# for i in range(n - 1, 0, - 1):
#     print((n - i) * ' ' + i * '*')

# boj 19532
# a, b, c, d, e, f = map(int, input().split())
# print((c * e - b * f) // (a * e - b * d), (c * d - a * f) // (b * d - a * e))\

# boj 13558
# n = int(input())
# presum = [0] * 60100
# sufsum = [0] * 60100
# arr = [1] * 101010
# ans = [0] * 101010
# res = 0
# arr[0] = arr[1] = arr[2] = 0
# presum[arr[1]] = 1
# data = list(map(int, input().split()))
# for i in range(2, n):
#     for j in range(1, 2 * arr[i] + 1):
#         ans[i] += presum[j] * sufsum[2 * arr[i] - j]
#
#     presum[arr[i]] += 1
#     sufsum[arr[i + 1]] -= 1
#     res += ans[i]
# print(res)

# boj 10610
# n = input()
# arr = [0] * 10
# num, ans = 0, ''
# for i in n:
#     arr[int(i)] += 1
#     num += int(i)
#
# if not arr[0] or num % 3:
#     print(- 1)
# else:
#     for i in range(10):
#         if arr[i]:
#             ans += str(i) * arr[i]
#     else:
#         print(ans[:: - 1])

# boj 2953
# ans = score = 0
# for i in range(1, 6):
#     temp = sum(list(map(int, input().split())))
#     if score < temp:
#         score = temp
#         ans = i
# print(ans, score)

# boj 3943
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     ans = n
#     while True:
#         if n == 1:
#             break
#         if n % 2:
#             n = n * 3 + 1
#         else:
#             n //= 2
#         if n > ans:
#             ans = n
#     print(ans)

# print(".  .   .\n|  | _ | _. _ ._ _  _\n|/\|(/.|(_.(_)[ | )(/.")

# v = int(input())
# s = input()
# a, b = s.count('A'), s.count('B')
# if a > b:
#     print('A')
# elif a < b:
#     print('B')
# else:
#     print("Tie")

# boj 2921
# memo = [0, 3]
# num = 3
# for i in range(2, 1001):
#     num += (2 * i) * (2 * i + 1) // 2 - i * (i - 1) // 2
#     memo.append(num)
# n = int(input())
# print(memo[n])

# boj 3046
# r1, s = map(int, input().split())
# print(2 * s - r1)

# print(len(input()))

# alpha = [0] * 26
# s = input()
# for i in s:
#     alpha[ord(i) - 97] += 1
# print(*alpha)

# n, m = map(int, input().split())
# print(n // m)
# print(n % m)

# boj 2783
# x, y = map(int, input().split())
# z = 1000 / y
# ans = x * z
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     c = 1000 / b
#     temp = a * c
#     if ans > temp:
#         ans = temp
# print(round(ans, 2))

# boj 9086
# t = int(input())
# for _ in range(t):
#     s = input().rstrip()
#     print(s[0] + s[- 1])

# boj 22341
# n, c = map(int, input().split())
# a, b = n, n
# for _ in range(c):
#     x, y = map(int, input().split())
#     if x >= a or y >= b:
#         continue
#     garo = x * b
#     sero = a * y
#     if garo >= sero:
#         a = x
#         ans = garo
#     else:
#         b = y
#         ans = sero
# print(ans)

# boj 9437
# while True:
#     data = input().split()
#     if len(data) == 2:
#         n, p = int(data[0]), int(data[1])
#         mid = n // 2
#         arr = []
#         if p > mid:
#             diff = p - mid
#             if p % 2:
#                 arr.append(mid - diff)
#                 arr.append(mid - diff + 1)
#                 arr.append(p + 1)
#             else:
#                 arr.append(mid - diff + 1)
#                 arr.append(mid - diff + 2)
#                 arr.append(p - 1)
#         else:
#             diff = mid - p
#             if p % 2:
#                 arr.append(p + 1)
#                 arr.append(mid + diff)
#                 arr.append(mid + diff + 1)
#             else:
#                 arr.append(p - 1)
#                 arr.append(mid + diff + 1)
#                 arr.append(mid + diff + 2)
#     else:
#         break
#     print(*arr)

# boj 17502
# n = int(input())
# s = list(input())
# for i in range(n):
#     if s[i] == '?':
#         if s[:: - 1][i] != '?':
#             s[i] = s[:: - 1][i]
#         else:
#             s[i] = 'a'
# print(''.join(s))

# boj 15829
# l = int(input())
# s = input()
# ans, r, m = 0, 31, 1234567891
# for i in range(l):
#     ans += (ord(s[i]) - 96) * pow(r, i) % m
# print(ans % m)

# boj 5235
# t = int(input())
# for _ in range(t):
#     arr = list(map(int, input().split()))
#     even, odd = 0, 0
#     for i in arr[1:]:
#         if i % 2:
#             odd += i
#         else:
#             even += i
#     if even > odd:
#         print("EVEN")
#     elif even < odd:
#         print("ODD")
#     else:
#         print("TIE")

# boj 16195
# mod = 1000000009
# dp = [[0] * 1002 for _ in range(1002)]
# dp[1][1] = dp[2][1] = dp[3][1] = 1
#
# for i in range(1, 1001):
#     for j in range(2, 1001):
#         if i - 1 > 0 and j <= i:
#             dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
#         if i - 2 > 0 and j <= i - 1:
#             dp[i][j] = (dp[i][j] + dp[i - 2][j - 1]) % mod
#         if i - 3 > 0 and j <= i - 2:
#             dp[i][j] = (dp[i][j] + dp[i - 3][j - 1]) % mod
#
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     ans = 0
#     for i in range(1, m + 1):
#         ans = (ans + dp[n][i]) % mod
#     print(ans)

# boj 18258
# import sys
# input = sys.stdin.readline
# from collections import deque
# n = int(input())
# q = deque()
# for _ in range(n):
#     com = input().split()
#     if com[0] == "push":
#         q.append(com[1])
#     elif com[0] == "pop":
#         print(q.popleft()) if q else print(- 1)
#     elif com[0] == "size":
#         print(len(q))
#     elif com[0] == "empty":
#         print(0) if q else print(1)
#     elif com[0] == "front":
#         print(q[0]) if q else print(- 1)
#     elif com[0] == "back":
#         print(q[- 1]) if q else print(- 1)

# boj 15724
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]
# k = int(input())
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])

# boj 11648
# n = input()
# ans = 0
# while int(n) > 9:
#     temp = 1
#     for i in n:
#         temp *= int(i)
#     n = str(temp)
#     ans += 1
# print(ans)
# boj 10815
# import sys
# input = sys.stdin.readline
# n = int(input())
# num = set(map(int, input().split()))
# m = int(input())
# card = list(map(int, input().split()))
# for i in card:
#     print(1, end = ' ') if i in num else print(0, end = ' ')

# boj 10810
# n, m = map(int, input().split())
# arr = [0] * n
# for _ in range(m):
#     i, j, k = map(int, input().split())
#     for idx in range(i - 1, j):
#         arr[idx] = k
# print(*arr)

# boj 4375
# while True:
#     try:
#         x = int(input())
#     except EOFError:
#         break
#     if x == 1:
#         print('1')
#         continue
#     num = 1
#     cnt = 1
#     while True:
#         num = num * 10 + 1
#         cnt += 1
#         if (num % x) == 0:
#             print(cnt)
#             break

# boj 2776
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     narr = set(map(int, input().split()))
#     m = int(input())
#     marr = list(map(int, input().split()))
#     for i in marr:
#         if i in narr:
#             print(1)
#         else:
#             print(0)

# boj 5032
# e, f, c = map(int, input().split())
# e += f
# ans = 0
# while True:
#     ans += e // c
#     e = e // c + e % c
#     if e < c:
#         break
# print(ans)

# boj 1652
# n = int(input())
# arr = [input().rstrip() for _ in range(n)]
# ans1, ans2 = 0, 0
# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if arr[i][j] == '.':
#             cnt += 1
#         else:
#             if cnt >= 2:
#                 ans1 += 1
#                 cnt = 0
#             else:
#                 cnt = 0
#     if cnt >= 2:
#         ans1 += 1
#
# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if arr[j][i] == '.':
#             cnt += 1
#         else:
#             if cnt >= 2:
#                 ans2 += 1
#                 cnt = 0
#             else:
#                 cnt = 0
#     if cnt >= 2:
#         ans2 += 1
# print(ans1, ans2)

# boj 9655
# print("SK" if int(input()) % 2 else "CY")

# boj 1550
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# s = input().rstrip()[:: - 1]
# ans = 0
# temp = 1
# for i in s:
#     ans += temp * num.index(i)
#     temp *= 16
# print(ans)

# boj 11466
# h, w = map(int, input().split())    # w < h로
# if h < w:
#     w, h = h, w
# if h >= 3 * w:
#     print(w)
# elif h >= 1.5 * w:
#     print(h / 3)
# else:
#     print(w / 2)

# boj 1264
# while True:
#     s = input().rstrip().lower()
#     if s == '#':
#         break
#     print(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u'))

# boj 17103
# import sys
# input = sys.stdin.readline
# prime = [1] * 1000001
# prime[0] = prime[1] = 0
# for i in range(2, int(1000000 ** 0.5) + 1):
#     if prime[i]:
#         for j in range(i + i, 1000001, i):
#             if prime[j]:
#                 prime[j] = 0
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     ans = 0
#     for i in range(n // 2 + 1):
#         if prime[i] and prime[n - i]:
#             ans += 1
#     print(ans)

# boj 2480
# arr = sorted(list(map(int, input().split())))
# setArr = set(arr)
# if len(setArr) == 3:
#     print(100 * arr[2])
# elif len(setArr) == 2:
#     if arr[0] == arr[1]:
#         print(1000 + 100 * arr[0])
#     else:
#         print(1000 + 100 * arr[2])
# else:
#     print(10000 + 1000 * arr[0])

# boj 14264
# l = int(input())
# print(pow(3, 0.5) * pow(l, 2) / 4)

# boj 17413
# s = input()
# ans, temp, chk = '', '', False
#
# for i in s:
#     if i == ' ':
#         if not chk:
#             ans += temp[:: - 1] + i
#             temp = ''
#         else:
#             ans += i
#     elif i == '<':
#         chk = True
#         ans += temp[:: - 1] + i
#         temp = ''
#     elif i == '>':
#         chk = False
#         ans += i
#     else:
#         if chk:
#             ans += i
#         else:
#             temp += i
# ans += temp[:: - 1]
# print(ans)

# boj 9012
# t = int(input())
# for _ in range(t):
#     S = input()
#     ans = "NO"
#     if len(S) % 2:
#         print(ans)
#     else:
#         s, chk = [], True
#         for i in S:
#             if i == '(':
#                 s.append(i)
#             else:
#                 if s:
#                     s.pop()
#                 else:
#                     chk = False
#                     break
#         if not s and chk:
#             ans = "YES"
#         print(ans)

# boj 18141
# def chk():
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 x = (arr[i] - arr[j]) / arr[k]
#                 y = (arr[i] - arr[k]) / arr[j]
#                 z = (arr[j] - arr[k]) / arr[i]
#                 if not(x == int(x) and y == int(y) and z == int(z)):
#                     return False
#     return True
#
# n = int(input())
# arr = list(map(int, input().split()))
# print("yes" if chk() else "no")

# swea no.1
# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     ans = (A + B) % 24
#     print("#{} {}".format(test_case + 1, ans))

# swea no.2
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

# SWEA No.1
T = int(input())
for test_case in range(T):
    N = int(input())
    A0, B0, C0 = map(int, input().split())
    A1, B1, C1 = map(int, input().split())
    ans = 0