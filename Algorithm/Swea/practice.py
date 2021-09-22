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

# T = int(input())
# for test_case in range(T):
#     A, B, C, D = map(int, input().split())
#     ans = 0
#     if B <= C:
#         ans = 0
#     elif A <= C and C < B and B <= D:
#         ans = B - C
#     elif A <= C and D <= B:
#         ans = D - C
#
#     elif D <= A:
#         ans = 0
#     elif C <= A and A < D and D <= B:
#         ans = A - D
#     elif C <= A and B <= D:
#         ans = B - A
#     print("#{} {}".format(test_case + 1, ans))

# T = int(input())
# ans = []
# for test_case in range(T):
#     A, B, C, D = map(int, input().split())
#     if B <= C:
#         ans.append("#{} {}".format(test_case + 1, 0))
#     elif A <= C and C < B and B <= D:
#         ans.append("#{} {}".format(test_case + 1, B - C))
#     elif A <= C and D <= B:
#         ans.append("#{} {}".format(test_case + 1, D - C))
#     elif D <= A:
#         ans.append("#{} {}".format(test_case + 1, 0))
#     elif C <= A and A < D and D <= B:
#         ans.append("#{} {}".format(test_case + 1, A - D))
#     elif C <= A and B <= D:
#         ans.append("#{} {}".format(test_case + 1, B - A))
# for i in ans:
#     print(i)

# T = int(input())
# for _ in range(T):
#     A, B, C, X, Y = map(int, input().split())
#     ans = 0
#     if A + B >= C * 2:
#         temp = min(X, Y)
#         ans += temp * C * 2
#         X -= temp
#         Y -= temp
#         if X:
#             if A >= C * 2:
#                 ans += C * X * 2
#             else:
#                 ans += A * X
#         if Y:
#             if B >= C * 2:
#                 ans += C * Y * 2
#             else:
#                 ans += B * Y
#     else:
#         ans += A * X + B * Y
#     print(ans)

# R, C = map(int, input().split())
# arr = [[0] * C for _ in range(R)]
# flag = True
# for i in range(C - 1, - 1, - 1):
#     temp1 = list(map(int, input().split()))
#     for j in range(R):
#         arr[j][i] = temp1[j]
#
# for x in range(R):
#     temp2 = list(map(int, input().split()))
#     if arr[x] != temp2:
#         flag = False
#
# if flag:
#     print('''|>___/|        /}
# | O < |       / }
# (==0==)------/ }
# | ^  _____    |
# |_|_/     ||__|''')
# else:
#     print('''|>___/|     /}
# | O O |    / }
# ( =0= )""""  \\
# | ^  ____    |
# |_|_/    ||__|''')

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     arr.sort(reverse = True, key = lambda x: (x[0] / x[1], - x[1]))
#     print(arr[0][1])

# n = input()
# ans = 0
# for i in n:
#     i = int(i)
#     ans += i ** 5
# print(ans)
# n = int(input())
# arr = [0] * (n + 1)
# data = list(map(int, input().split()))
# for i in data:
#     arr[i] += 1
# for i in range(n - 1, - 1, - 1):
#     if arr[i] == i:
#         ans = i
#         break
# else:
#     ans = - 1
# print(ans)

# A, B, C, M = map(int, input().split())
# work, tired = 0, 0
# for i in range(1, 25):
#     if tired + A <= M:
#         tired += A
#         work += B
#     else:
#         tired -= C
#         if tired < 0:
#             tired = 0
# print(work)

# a : 1, b : 2, c : 1, d : 2
# a, b, c, d = 1, 2, 1, 2
# if a <= c < b <= d:
#     print(True)

# boj 1292
# arr = []
# n = 1
# while n < 45:
#     arr += [n] * n
#     n += 1
# arr += [45] * 11
# A, B = map(int, input().split())
# print(sum(arr[A - 1 : B]))

# boj 10992
# n = int(input())
# for i in range(n):
#     if i == 0:
#         print(' ' * (n - 1) + '*')
#     elif i == n - 1:
#         print('*' * (2 * n - 1))
#     else:
#         print(' ' * (n - 1 - i) + '*' + ' ' * (2 * i - 1) + '*')

# boj 14487
# n = int(input())
# arr = list(map(int, input().split()))
# ans = sum(arr) - max(arr)
# print(ans)

# boj 5532
# l = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# x = a // c if a / c == a // c else a // c + 1
# y = b // d if b / d == b // d else b // d + 1
# print(l - max(x, y))

# boj 9654
# print('''SHIP NAME      CLASS          DEPLOYMENT IN SERVICE
# N2 Bomber      Heavy Fighter  Limited    21
# J-Type 327     Light Combat   Unlimited  1
# NX Cruiser     Medium Fighter Limited    18
# N1 Starfighter Medium Fighter Unlimited  25
# Royal Cruiser  Light Combat   Limited    4  ''')

# boj 1459
# x, y, w, s = map(int, input().split())
# temp1 = (x + y) * w
# temp2 = max(x, y) * s if (x + y) % 2 == 0 else (max(x, y) - 1) * s + w
# temp3 = min(x, y) * s + abs(x - y) * w
# print(min(temp1, temp2, temp3))

# boj 1439
# s = input()
# ans = 0
# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         ans += 1
# print((ans + 1) // 2)

# boj 1977
# arr = []
# for i in range(1, 101):
#     if i ** 2 <= 10000:
#         arr.append(i ** 2)
#
# M = int(input())
# N = int(input())
# total = 0
# ans = float('inf')
# for i in arr:
#     if M <= i <= N:
#         total += i
#         if ans > i:
#             ans = i
#     if i > N:
#         break
# if not total:
#     print(- 1)
# else:
#     print(total)
#     print(ans)

# boj 11004
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[K - 1])

# boj 10991
# n = int(input())
# for i in range(n):
#     print(' ' * (n - 1 - i) + '* ' * i + '*')

# boj 2985
# A, B, C = map(int, input().split())
# if A + B == C:
#     print(str(A) + '+' + str(B) + '=' + str(C))
# elif A - B == C:
#     print(str(A) + '-' + str(B) + '=' + str(C))
# elif A * B == C:
#     print(str(A) + '*' + str(B) + '=' + str(C))
# elif A // B == C:
#     print(str(A) + '/' + str(B) + '=' + str(C))
# elif A == B + C:
#     print(str(A) + '=' + str(B) + '+' + str(C))
# elif A == B - C:
#     print(str(A) + '=' + str(B) + '-' + str(C))
# elif A == B * C:
#     print(str(A) + '=' + str(B) + '*' + str(C))
# elif A == B / C:
#     print(str(A) + '=' + str(B) + '/' + str(C))

# boj 2530
# H, M, S = map(int, input().split())
# D = int(input())
# S += D % 60
# D //= 60
# if S >= 60:
#     S -= 60
#     M += 1
# M += D % 60
# D //= 60
# if M >= 60:
#     M -= 60
#     H += 1
# H += D % 24
# if H >= 24:
#     H -= 24
# print(H, M, S)

# boj 1668
# n = int(input())
# arr = [int(input()) for _ in range(n)]
# ans1, ans2 = 1, 1
# tro1, tro2 = arr[0], arr[- 1]
# for i in range(1, n):
#     temp = arr[i]
#     if tro1 < temp:
#         tro1 = temp
#         ans1 += 1
# for j in range(n - 2, - 1, - 1):
#     temp = arr[j]
#     if tro2 < temp:
#         tro2 = temp
#         ans2 += 1
# print(ans1)
# print(ans2)

# boj 11943
# A, B = map(int, input().split())
# C, D = map(int, input().split())
# print(min(A + D, B + C))

# boj 1932
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# k = 2
# for i in range(1, n):
#     for j in range(k):
#         if j == 0:
#             arr[i][j] += arr[i - 1][j]
#         elif i == j:
#             arr[i][j] += arr[i - 1][j - 1]
#         else:
#             arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
#     k += 1
# print(max(arr[n - 1]))

# boj 16395
# n, k = map(int, input().split())
# arr = []
# for i in range(1, n + 1):
#     arr.append([1] * i)
#
# for i in range(2, n):
#     for j in range(1, i):
#         arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
# print(arr[n - 1][k - 1])

# boj 3184
# from collections import deque
# import sys
# input = sys.stdin.readline
# dx = [- 1, 1, 0, 0] # 상하좌우
# dy = [0, 0, - 1, 1]
#
# def bfs(x, y):
#     global o, v
#     q = deque()
#     q.append((x, y))
#     to, tv = 0, 0
#     if arr[x][y] == 'o':
#         to += 1
#     elif arr[x][y] == 'v':
#         tv += 1
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and arr[nx][ny] != '#':
#                 if arr[nx][ny] == 'o':
#                     to += 1
#                 if arr[nx][ny] == 'v':
#                     tv += 1
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#     if to and tv:
#         if to > tv:
#             v -= tv
#         else:
#             o -= to
#
# r, c = map(int, input().split())
# arr = []
# o, v = 0, 0
# visited = [[0] * c for _ in range(r)]
# for i in range(r):
#     temp = list(input().rstrip())
#     o += temp.count('o')
#     v += temp.count('v')
#     arr.append(temp)
#
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] in 'ov' and visited[i][j] == 0:
#             visited[i][j] = 1
#             bfs(i, j)
# print(o, v)

# boj 11320
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print((a // b) ** 2)

# boj 20112
# n = int(input())
# arr = [input() for _ in range(n)]
# ans = "YES"
# for i in range(n):
#     if ans == "NO":
#         break
#     for j in range(i, n):
#         if i != j:
#             if arr[i][j] != arr[j][i]:
#                 ans = "NO"
#                 break
# print(ans)

# boj 20352
# n = int(input())
# pi = 3.14159265359
# r = (n / pi) ** 0.5
# print(2 * pi * r)

# boj 18398
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     for _ in range(n):
#         a, b = map(int, input().split())
#         print(a + b, a * b)

# boj 11170
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     ans = 0
#     for i in range(n, m + 1):
#         ans += str(i).count('0')
#     print(ans)

# boj 5361
# price = [350.34, 230.90, 190.55, 125.30, 180.90]
# t = int(input())
# for _ in range(t):
#     arr = list(map(int, input().split()))
#     ans = 0
#     for i in range(5):
#         ans += price[i] * arr[i]
#     print("${}".format(format(ans, ".2f")))

# boj 1225
# a, b = input().split()
# A, B = 0, 0
# for i in a:
#     A += int(i)
# for j in b:
#     B += int(j)
# print(A * B)

# boj 15813
# n = int(input())
# s = input()
# ans = 0
# for i in s:
#     ans += ord(i) - 64
# print(ans)

# boj 4766
arr = []
while True:
    s = float(input().rstrip())
    if s == 999:
        break
    arr.append(s)
a = arr[0]
for i in arr[1:]:
    print(format(i - a, ".2f"))
    a = i