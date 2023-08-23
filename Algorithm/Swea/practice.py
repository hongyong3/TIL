import sys
sys.stdin = open("practice_input.txt", "r")

# import sys
# input = sys.stdin.readline

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
# arr = []
# while True:
#     s = float(input().rstrip())
#     if s == 999:
#         break
#     arr.append(s)
# a = arr[0]
# for i in arr[1:]:
#     print(format(i - a, ".2f"))
#     a = i

# def showFile(filename):
#     global arr
#     f = open(filename, 'r', encoding='utf-8')
#     lines = f.readlines()
#     for line in lines:
#         arr.append(line.rstrip())
#     f.close()
#     arr.sort()
#
# n = 186
# arr = []
# showFile('practice_input.txt')
#
# for i in range(n):
#     print(arr[i])

# boj 1408
# a, b, c = map(int, input().split(':'))
# x, y, z = map(int, input().split(':'))
#
# if z >= c:
#     z -= c
# else:
#     z = 60 + z - c
#     y -= 1
# if z < 10:
#     z = '0' + str(z)
# else:
#     z = str(z)
#
# if y >= b:
#     y -= b
# else:
#     y = 60 + y - b
#     x -= 1
# if y < 10:
#     y = '0' + str(y)
# else:
#     y = str(y)
#
# x -= a
# if x < 10:
#     x = '0' + str(x)
# else:
#     x = str(x)
# print("{}:{}:{}".format(x, y, z))

# boj 6131
# n = int(input())
# ans = 0
# for b in range(1, 500):
#     for a in range(b + 1, 501):
#         if a ** 2 == b ** 2 + n:
#             ans += 1
#         elif a ** 2 > b ** 2 + n:
#             break
# print(ans)

# boj 10599
# while True:
#     a, b, c, d = map(int, input().split())
#     if a == b == c == d == 0:
#         break
#     print(abs(b - c), abs(d - a))

# boj 17388
# arr = list(map(int, input().split()))
# score = sum(arr)
# uni = ["Soongsil", "Korea", "Hanyang"]
# if score >= 100:
#     print("OK")
# else:
#     print(uni[arr.index(min(arr))])

# boj 3986
# import sys
# input = sys.stdin.readline
# n = int(input())
# words = [list(input().rstrip()) for _ in range(n)]
# ans = 0
# for word in words:
#     stack = []
#     while word:
#         w = word.pop()
#         if not stack:
#             stack.append(w)
#         else:
#             if stack[- 1] == w:
#                 stack.pop()
#             else:
#                 stack.append(w)
#     if not stack:
#         ans += 1
# print(ans)

# boj 2167
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

# boj 8595#
# import sys
# input = sys.stdin.readline
# n = int(input())
# s = input().rstrip()
# num = [str(i) for i in range(10)]
# ans, cnt, hidden = 0, 0, 0
#
# for i in s[:: - 1]:
#     if hidden >= 1000000:
#         hidden = 0
#         cnt = 0
#     elif i in num:
#         ans += int(i) * (10 ** cnt)
#         cnt += 1
#     else:
#         cnt = 0
#         hidden = 0
# print(ans)

# boj 9325
# t = int(input())
# for _ in range(t):
#     ans = int(input())
#     n = int(input())
#     for _ in range(n):
#         q, p = map(int, input().split())
#         ans += q * p
#     print(ans)

# boj 21735
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(1 << m):
#     x, b = 1, 0
#     for j in range(m):
#         if i & (1 << j):
#             b += 1
#             x >>= 1
#         if j + b >= n:
#             break
#         x += arr[j + b]
#     ans = max(ans, x)
# print(ans)

# boj 14652
# n, m, k = map(int, input().split())
# print(k // m, k % m)

# boj 5692
# import sys
# while True:
#     n = sys.stdin.readline().rstrip()[:: - 1]
#     ans = 0
#     fact = [1, 2, 6, 24, 120]
#     if n == '0':
#         break
#     for i in range(len(n)):
#         ans += int(n[i]) * fact[i]
#     print(ans)

# boj 20499
# K, D, A = map(int, input().split('/'))
# print("hasu") if K + A <D or D == 0 else print("gosu")

# boj 14470
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# ans = 0
# if A <= 0:
#     ans += abs(A) * C + D
#     A = 0
# ans += (B - A) * E
# print(ans)

# boj 3460
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = bin(n)[2:][:: - 1]
#     for i in range(len(a)):
#         if a[i] == '1':
#             print(i, end = ' ')

# boj 1676
# n = int(input())
# num = 1
# for i in range(1, n + 1):
#     num *= i
# num = str(num)[:: - 1]
# ans = 0
# for i in num:
#     if i == '0':
#         ans += 1
#     else:
#         break
# print(ans)

# boj 23027
# s = input()
# A, B, C = s.count('A'), s.count('B'), s.count('C')
# ans = ''
# if A:
#     for i in s:
#         if i in 'BCDF':
#             ans += 'A'
#         else:
#             ans += i
# elif not A and B:
#     for i in s:
#         if i in 'CDF':
#             ans += 'B'
#         else:
#             ans += i
# elif not A and not B and C:
#     for i in s:
#         if i in 'DF':
#             ans += 'C'
#         else:
#             ans += i
# else:
#     ans = 'A' * len(s)
# print(ans)

# boj 2935
# a = int(input())
# col = input()
# b = int(input())
# if col == '+':
#     print(a + b)
# else:
#     print(a * b)

# boj 14712
# import sys
# input = sys.stdin.readline
# def dfs(cnt):
#     global ans
#     if cnt == n * m:
#         ans += 1
#         return
#     x = cnt // m + 1
#     y = cnt % m + 1
#     dfs(cnt + 1)
#     if arr[x - 1][y] == 0 or arr[x][y - 1] == 0 or arr[x - 1][y - 1] == 0:
#         arr[x][y] = 1
#         dfs(cnt + 1)
#         arr[x][y] = 0
# n, m = map(int, input().rstrip().split())
# arr = [[0] * (m + 1) for _ in range(n + 1)]
# ans = 0
# dfs(0)
# print(ans)

# boj 2615
# dx = [1, 1, 0, - 1] # 하 우하 우 우상
# dy = [0, 1, 1, 1]
# def dfs():
#     for x in range(19):
#         for y in range(19):
#             if arr[x][y]:
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     cnt = 1
#
#                     if not (0 <= nx < 19 and 0 <= ny < 19):
#                         continue
#
#                     while 0 <= nx < 19 and 0 <= ny < 19 and arr[x][y] == arr[nx][ny]:
#                         cnt += 1
#
#                         if cnt == 5:
#                             if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19:
#                                 if arr[nx][ny] == arr[nx + dx[k]][ny + dy[k]]:
#                                     break
#                             if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and arr[x][y] == arr[x - dx[k]][y - dy[k]]:
#                                 break
#                             return arr[x][y], x + 1, y + 1
#
#                         nx += dx[k]
#                         ny += dy[k]
#
#     return 0, - 1, - 1
#
#
# arr = [list(map(int, input().split())) for _ in range(19)]
# color, x, y = dfs()
# if not color:
#     print(color)
# else:
#     print(color)
#     print(x, y)

# boj 18108
# n = int(input())
# print(n - 543)

# boj 4564
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     ans = [n]
#     while len(str(n)) > 1:
#         temp = 1
#         for i in str(n):
#             temp *= int(i)
#         ans.append(temp)
#         n = temp
#     print(*ans)

# boj 1236
# def sol(n, q):
#     ans = ''
#     while n:
#         n, mod = divmod(n, q)
#         ans += str(mod)
#     return ans[:: - 1]
# t = int(input())
# print(sol(t, 9))

# boj 1373
# print(oct(int(input(), 2))[2:])

# boj 20492
# n = int(input())
# print(int(0.78 * n), int(0.8 * n + 0.2 * 0.78 * n))

# boj 5217
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     ans = []
#     for i in range(1, n // 2 + 1):
#         if i == n - i or n - i == 0:
#             pass
#         else:
#             ans.append((i, n - i))
#     if not ans:
#         print("Pairs for {}: ".format(n))
#     else:
#         print("Pairs for {}: ".format(n), end='')
#         for i in ans[: - 1]:
#             print(*i, end = ', ')
#         if ans:
#             print(*ans[- 1])

# boj 17173
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = set()
# for i in range(2, n + 1):
#     for j in arr:
#         if not i % j:
#             ans.add(i)
# print(sum(ans))

# boj 2506
# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# score = 1
# for i in arr:
#     if i:
#         ans += score
#         score += 1
#     else:
#         score = 1
# print(ans)

# boj 14909
# arr = list(map(int, input().split()))
# ans = 0
# for i in arr:
#     if i > 0:
#         ans += 1
# print(ans)

# boj 23080
# k = int(input())
# s = input()
# ans = ''
# for i in range(0, len(s), k):
#     ans += s[i]
# print(ans)

# boj 6588
# import sys
# input = sys.stdin.readline
# num = 100001
# arr = [1] * num
# for i in range(2, int((num - 1) ** 0.5) + 1):
#     if arr[i]:
#         for k in range(i + i, num, i):
#             arr[k] = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     chk = 0
#     for i in range(3, len(arr) + 1):
#         if arr[i] and arr[n - i]:
#             print("{} = {} + {}".format(n, i, n - i))
#             chk = 1
#             break
#     if chk == 0:
#         print("Goldbach's conjecture is wrong.")

# boj 13301
# n = int(input())
# a1, a2 = 4, 6
# ans = 0
# if n == 1:
#     ans = a1
# elif n == 2:
#     ans = a2
# else:
#     for i in range(2, n):
#         ans = a1 + a2
#         a1 = a2
#         a2 = ans
# print(ans)

# boj 17614
# import sys
# input = sys.stdin.readline
# n = int(input())
# ans = 0
# for i in range(1, n + 1):
#     ans += str(i).count('3') + str(i).count('6') + str(i).count('9')
# print(ans)

# boj 10179
# t = int(input())
# for _ in range(t):
#     n = float(input())
#     print("${}".format(format(0.8 * n, ".2f")))

# boj 10214
# t = int(input())
# for _ in range(t):
#     scoreY, scoreK = 0, 0
#     for i in range(9):
#         y, k = map(int, input().split())
#         scoreY += y
#         scoreK += k
#     if scoreY > scoreK:
#         print("Yonsei")
#     elif scoreY < scoreK:
#         print("Korea")
#     else:
#         print("Draw")

# boj 2580
# import sys
# input = sys.stdin.readline
# def dfs(n):
#     global flag
#     if flag:
#         return
#     if n == len(chk):
#         for i in arr:
#             print(*i)
#         flag = 1
#         return
#     r, c = chk[n]
#     cases = makeCases(r, c)
#
#     for case in cases:
#         arr[r][c] = case
#         dfs(n + 1)
#         arr[r][c] = 0
#
#
# def makeCases(x, y):
#     num = [i for i in range(1, 10)]
#
#     for k in range(9):
#         if arr[x][k] in num:
#             num.remove(arr[x][k])
#         if arr[k][y] in num:
#             num.remove(arr[k][y])
#
#     x1 = (x // 3) * 3
#     y1 = (y // 3) * 3
#
#     for r in range(x1, x1 + 3):
#         for c in range(y1, y1 + 3):
#             if arr[r][c] in num:
#                 num.remove(arr[r][c])
#     return num
#
#
# arr = [list(map(int, input().split())) for _ in range(9)]
# chk = [(x, y) for x in range(9) for y in range(9) if arr[x][y] == 0]
# flag = 0
# dfs(0)

# boj 1926
# import sys
# input = sys.stdin.readline
#
# dx = [- 1, 1, 0, 0] # 상하좌우
# dy = [0, 0, - 1, 1]
#
# def bfs(x, y):
#     temp = 1
#     q = [(x, y)]
#     while q:
#         x, y = q.pop()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if arr[nx][ny] and not visited[nx][ny]:
#                     temp += 1
#                     visited[nx][ny] = 1
#                     q.append((nx,ny))
#     return temp
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# cnt, ans = 0, 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] and not visited[i][j]:
#             cnt += 1
#             visited[i][j] = 1
#             ans = max(ans, bfs(i, j))
# print(cnt)
# print(ans)

# boj 9663
# 백트레킹 필요할듯...
# import sys
# input = sys.stdin.readline
# def chk(x):
#     for i in range(1, x):
#         if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
#             return False
#     return True
#
# def dfs(idx):
#     global ans
#     if idx > n:
#         ans += 1
#     else:
#         for i in range(1, n + 1):
#             arr[idx] = i
#             if chk(idx):
#                 dfs(idx + 1)
# n = int(input())
# arr = [[0] * 16 for _ in range(16)]
# ans = 0
# dfs(1)
# print(ans)

# boj 15781
# n, m = map(int, input().split())
# a = max(list(map(int, input().split())))
# b = max(list(map(int, input().split())))
# print(a + b)

# boj 17256
# ax, ay, az = map(int, input().split())
# cx, cy, cz = map(int, input().split())
# print(cx - az, cy // ay, cz - ax)

# boj 9093
# t = int(input())
# for _ in range(t):
#     s = input().split()
#     ans = ''
#     for i in s:
#         ans += i[:: - 1] + ' '
#     print(ans[: - 1])

# boj 11123
# import sys
# sys.setrecursionlimit(10000)
#
# dx = [- 1, 1, 0, 0] # 상하좌우
# dy = [0, 0, - 1, 1]
# def dfs(x, y):
#     arr[x][y] = '.'
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '#':
#             dfs(nx, ny)
#
# t = int(input())
# for _ in range(t):
#     h, w = map(int, input().split())
#     arr = [list(input()) for _ in range(h)]
#     ans = 0
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '#':
#                 dfs(i, j)
#                 ans += 1
#     print(ans)

# boj 13275
# A = [0] * 200002
# def solve(word, n):
#     r, p = 0, 0
#     for i in range(n):
#         if i <= r:
#             A[i] = min(A[2 * p - i], r - i)
#         else:
#             A[i] = 0
#         while (i - A[i] - 1 >= 0 and i + A[i] + 1 < n and word[i - A[i] - 1] == word[i + A[i] + 1]):
#             A[i] += 1
#         if r < i + A[i]:
#             r = i + A[i]
#             p = i
#
# s = input()
# words = ''
# for i in s:
#     words += '#'
#     words += i
# words += '#'
# solve(words, len(words))
# ans = max(A[: len(words)])
# print(ans)

# boj 1235
# n = int(input())
# arr = [input().rstrip()[:: - 1] for _ in range(n)]
# ans = 0
# while True:
#     temp = set()
#     for i in arr:
#         temp.add(i[:ans])
#     if len(temp) == n:
#         break
#     ans += 1
# print(ans)

# boj 13699
# def solve():
#     arr[0] = 1
#     for i in range(1, 36):
#         for j in range(0, i):
#             arr[i] += arr[j] * arr[i - 1 - j]
#
# n = int(input())
# arr = [0] * 36
# arr[0] = 1
# solve()
# print(arr[n])

# boj 15814
# s = list(input())
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     s[a], s[b] = s[b], s[a]
# ans = ''
# for i in s:
#     ans += i
# print(ans)

# boj 16170
# from datetime import date
# today = date.today()
# print(today.year)
# print(today.month)
# print(today.day)

# boj 14563
# t = int(input())
# arr = list(map(int, input().split()))
# for i in arr:
#     num = 0
#     for j in range(1, i // 2 + 1):
#         if not i % j:
#             num += j
#     if num == i:
#         print("Perfect")
#     elif num > i:
#         print("Abundant")
#     else:
#         print("Deficient")

# boj 16561
# n = int(input())
# ans = 1
# temp = 2
# for i in range(9, n, 3):
#     ans += temp
#     temp += 1
# print(ans)

# boj 11328
# t = int(input())
# for _ in range(t):
#     a, b = input().split()
#     if sorted(a) == sorted(b):
#         print("Possible")
#     else:
#         print("Impossible")

# boj 2133
# n = int(input())
# dp = [0] * 50
# arr = [0] * 50
# dp[0] = 1
# dp[2] = 3
# for i in range(4, 31, 2):
#     arr[i] = arr[i - 2] + dp[i - 4]
#     dp[i] = dp[i - 2] * 3 + arr[i] * 2
# print(dp[n])

# boj 1964
# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = [0] * (n + 1)
# dp[0] = 5
# idx = 3
# for i in range(1, n + 1):
#     dp[i] = dp[i - 1] + idx * 3 - 2
#     idx += 1
# print(dp[n - 1] % 45678)

# boj 10989
# import sys
# input = sys.stdin.readline
# arr = [0 for x in range(10001)]
# n = int(input())
# for _ in range(n):
#     arr[int(input())] += 1
# for i in range(10001):
#     print('%s\n' % i * arr[i], end='')

# boj 7576
# from collections import deque
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# q = deque()
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             q.append((i, j, 0))
# while q:
#     x, y, cnt = q.popleft()
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         ncnt = cnt + 1
#
#         if 0 <= nx < n and 0 <= ny < m:
#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = 1
#                 q.append((nx, ny, ncnt))
#
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 0:
#             cnt = - 1
#             break
# print(cnt)

# boj 3187
# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def bfs(x, y):
#     sheep, wolf = 0, 0
#     if arr[i][j] == 'v':
#         wolf = 1
#     elif arr[i][j] == 'k':
#         sheep = 1
#
#     visited[i][j] = 1
#     q.append((i, j))
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] != '#':
#                 visited[nx][ny] = 1
#                 if arr[nx][ny] == 'v':
#                     wolf += 1
#                 elif arr[nx][ny] == 'k':
#                     sheep += 1
#                 q.append((nx, ny))
#
#     if sheep > wolf:
#         ans[0] += sheep
#     else:
#         ans[1] += wolf
#
# r, c = map(int, input().split())
# arr = [input().rstrip() for _ in range(r)]  # . 빈공간, # 울타리, v 늑대, k 양
# visited = [[0] * c for _ in range(r)]
# q = deque()
# ans = [0, 0]
#
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] != '#' and not visited[i][j]:
#             bfs(i, j)
# print(*ans)

# boj 10987
# s = input()
# ans = 0
# for i in s:
#     if i in 'aeiou':
#         ans += 1
# print(ans)

# boj 21919
# import sys
# input = sys.stdin.readline
# def findPrime(n):
#     sieve = [True] * n
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i]:
#             for j in range(i + i, n, i):
#                 sieve[j] = False
#     return [i for i in range(2, n) if sieve[i] == True]
#
# n = int(input())
# arr = set(map(int, input().split()))
# prime = findPrime(1000000)
# ans = 1
# for i in arr:
#     if i in prime:
#         ans *= i
# if ans == 1:
#     print(- 1)
# else:
#     print(ans)

# boj 2578
# def chk():
#     bingo = 0
#     # 가로
#     for i in visited:
#         if 0 not in i:
#             bingo += 1
#
#     # 세로
#     colVisited = list(map(list, zip(*visited)))
#     for i in colVisited:
#         if 0 not in i:
#             bingo += 1
#
#     # 대각선
#     l, r = 1, 1
#     for i in range(5):
#         if not visited[i][i]:
#              l = 0
#         if not visited[i][4 - i]:
#             r = 0
#     if l:
#         bingo += 1
#     if r:
#         bingo += 1
#
#     if bingo >= 3:
#         return True
#     return False
#
#
# arr = [list(map(int, input().split())) for _ in range(5)]
# mc = [list(map(int, input().split())) for _ in range(5)]
# visited = [[0] * 5 for _ in range(5)]
# ans = 0
#
# for call in mc:
#     while call:
#         num = call.pop(0)
#         flag = True
#         ans += 1
#         for i in range(5):
#             if not flag:
#                 break
#             for j in range(5):
#                 if arr[i][j] == num:
#                     visited[i][j] = 1
#                     flag = False
#                     break
#         if ans >= 5 and chk():
#             print(ans)
#             exit()

# boj 6996
# t = int(input())
# for _ in range(t):
#     a, b = input().split()
#     aAlpha = [0] * 26
#     bAlpha = [0] * 26
#     if len(a) != len(b):
#         print("{} & {} are NOT anagrams.".format(a, b))
#     else:
#         for i in range(len(a)):
#             aAlpha[ord(a[i]) - 97] += 1
#             bAlpha[ord(b[i]) - 97] += 1
#         if aAlpha == bAlpha:
#             print("{} & {} are anagrams.".format(a, b))
#         else:
#             print("{} & {} are NOT anagrams.".format(a, b))

# boj 21603
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# fk, fk2 = K % 10, (2 * K) % 10
# arr = []
# for i in range(1, N + 1):
#     fx = i % 10
#     if fx != fk and fx != fk2:
#         arr.append(i)
# print(len(arr))
# print(*arr)

# boj 23803
# n = int(input())
# for i in range(4 * n):
#     print('@' * n)
# for i in range(n):
#     print('@' * 5 * n)

# boj 23794
# n = int(input())
# print('@' * (2 + n))
# for i in range(n):
#     print('@' + ' ' * n + '@')
# print('@' * (2 + n))

# boj 23802
# n = int(input())
# for i in range(n):
#     print('@' * 5 * n)
# for i in range(4 * n):
#     print('@' * n)

# boj 23804
# n = int(input())
# for i in range(n):
#     print('@' * 5 * n)
# for i in range(3 * n):
#     print('@' * n)
# for i in range(n):
#     print('@' * 5 * n)

# boj 23805
# n = int(input())
# for _ in range(n):
#     print('@' * 3 * n + ' ' * n + '@' * n)
# for _ in range(3 * n):
#     print(('@' * n + ' ' * n) * 2 + '@' * n)
# for _ in range(n):
#     print('@' * n + ' ' * n + '@' * 3 * n)

# boj 23806
# n = int(input())
# for _ in range(n):
#     print('@' * 5 * n)
# for i in range(3 * n):
#     print('@' * n + ' ' * 3 * n + '@' * n)
# for _ in range(n):
#     print('@' * 5 * n)

# boj 23808
# n = int(input())
# for _ in range(2 * n):
#     print('@' * n + ' ' * 3 * n + '@' * n)
# for _ in range(n):
#     print('@' * 5 * n)
# for i in range(n):
#     print('@' * n + ' ' * 3 * n + '@' * n)
# for _ in range(n):
#     print('@' * 5 * n)

# boj 23809
# n = int(input())
# for _ in range(n):
#     print('@' * n + ' ' * 3 * n + '@' * n)
# for _ in range(n):
#     print('@' * n + ' ' * 2 * n + '@' * n)
# for _ in range(n):
#     print('@' * 3 * n)
# for _ in range(n):
#     print('@' * n + ' ' * 2 * n + '@' * n)
# for _ in range(n):
#     print('@' * n + ' ' * 3 * n + '@' * n)

# boj 23810
# n = int(input())
# for _ in range(n):
#     print('@' * 5 * n)
# for _ in range(n):
#     print('@' * n)
# for _ in range(n):
#     print('@' * 5 * n)
# for _ in range(2 * n):
#     print('@' * n)

# boj 23811
# n = int(input())
# cnt = 2
# while cnt:
#     for _ in range(n):
#         print('@' * 5 * n)
#     for _ in range(n):
#         print('@' * n)
#     cnt -= 1
# for _ in range(n):
#     print('@' * 5 * n)

# boj 23812
# n = int(input())
# for _ in range(2):
#     for _ in range(n):
#         print('@' * n + ' ' * 3 * n + '@' * n)
#     for _ in range(n):
#         print('@' * 5 * n)
# for _ in range(n):
#     print('@' * n + ' ' * 3 * n + '@' * n)

# boj 2667
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def bfs(x, y):
#     cnt = 1
#     q = [(x, y)]
#     while q:
#         x, y = q.pop(0)
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '1' and not visited[nx][ny]:
#                 arr[nx][ny] = '0'
#                 cnt += 1
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#     ans.append(cnt)
#
# n = int(input())
# arr = [list(input().rstrip()) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# ans = []
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == '1':
#             arr[i][j] = '0'
#             visited[i][j] = 1
#             bfs(i, j)
# print(len(ans))
# for i in sorted(ans):
#     print(i)

# boj 5426
# t = int(input())
# for _ in range(t):
#     s = input().rstrip()
#     n = int(len(s) ** 0.5)
#     arr = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             arr[i].append(s[n * i + j])
#     ans = ''
#     for i in range(n - 1, - 1, - 1):
#         for j in range(n):
#             ans += arr[j][i]
#     print(ans)

# boj 16675
# ML, MR, TL, TR = input().split()
#
# if ML != MR and TL != TR:
#     print("?")
#
# elif ML == MR and TL != TR:
#     if ML == 'S' and (TL == 'R' or TR == 'R'):
#         print("TK")
#     elif ML == 'P' and (TL == 'S' or TR == 'S'):
#         print("TK")
#     elif ML == 'R' and (TL == 'P' or TR == 'P'):
#         print("TK")
#     else:
#         print("?")
#
# elif ML != MR and TL == TR:
#     if TL == 'S' and (ML == 'R' or MR == 'R'):
#         print("MS")
#     elif TL == 'P' and (ML == 'S' or MR == 'S'):
#         print("MS")
#     elif TL == 'R' and (ML == 'P' or MR == 'P'):
#         print("MS")
#     else:
#         print("?")
#
# else:
#     if ML == 'S':
#         if TL == 'P':
#             print("MS")
#         if TL == 'S':
#             print("?")
#         if TL == 'R':
#             print("TK")
#     if ML == 'R':
#         if TL == 'P':
#             print("TK")
#         if TL == 'S':
#             print("MS")
#         if TL == 'R':
#             print("?")
#     if ML == 'P':
#         if TL == 'P':
#             print("?")
#         if TL == 'S':
#             print("TK")
#         if TL == 'R':
#             print("MS")

# boj 10569
# t = int(input())
# for _ in range(t):
#     v, e = map(int, input().split())
#     print(2 - v + e)

# boj 16953
# a, b = map(int, input().split())
# q = [(a, 0)]
# ans = 0
# while q:
#     x, cnt = q.pop(0)
#     if x == b:
#         ans = cnt + 1
#         break
#     if x * 2 <= b:
#         q.append((x * 2, cnt + 1))
#     if x * 10 + 1 <= b:
#         q.append((x * 10 + 1, cnt + 1))
# if ans:
#     print(ans)
# else:
#     print(- 1)

# boj 1086
# import sys, math
# input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)]
# k = int(input())
# nums = [[(j * 10 ** len(str(arr[i])) + arr[i]) % k for j in range(k)] for i in range(n)]
# dp = [[0] * k for _ in range(1 << n)]
# dp[0][0] = 1
#
# for b in range(1 << n):
#     for i in range(n):
#         if b & (1 << i):
#             continue
#         for j in range(k):
#             dp[b | (1 << i)][nums[i][j]] += dp[b][j]
# p = dp[(1 << n) - 1][0]
# q = sum(dp[(1 << n) - 1])
# g = math.gcd(p, q)
# print("{}/{}".format(p // g, q // g))

# boj 7572
# arr1, arr2 = "ABCDEFGHIJKL", "0123456789"
# n = int(input()) - 4
# print(arr1[n % 12] + arr2[n % 10])

# boj 16165
# n, m = map(int, input().split())
# dic = {}
# for _ in range(n):
#     girl = input().rstrip()
#     number = int(input())
#     if girl not in dic:
#         dic[girl] = []
#     for _ in range(number):
#         member = input().rstrip()
#         dic[girl].append(member)
#     dic[girl].sort()
#
# for _ in range(m):
#     name = input().rstrip()
#     quiz = int(input())
#     if quiz:
#         for k, val in dic.items():
#             if name in val:
#                 print(k)
#                 break
#     else:
#         for k, val in dic.items():
#             if name == k:
#                 for val in dic[k]:
#                     print(val)
#                 break

# boj 10768
# m = int(input())
# d = int(input())
# if m > 2:
#     print("After")
# elif m < 2:
#     print("Before")
# else:
#     if d > 18:
#         print("After")
#     elif d < 18:
#         print("Before")
#     else:
#         print("Special")

# T = int(input())
# for test_case in range(T):
#     arr = []
#     N = int(input())
#     l = len(str(N))
#     minNum = maxNum = N
#
#     for i in str(N):
#         arr.append(int(i))
#
#     for i in range(l):
#         for j in range(i + 1, l):
#             if i == 0 and arr[j] == 0:
#                 continue
#             arr[i], arr[j] = arr[j], arr[i]
#             num, cnt = 0, l - 1
#             for k in arr:
#                 num += k * pow(10, cnt)
#                 cnt -= 1
#             arr[i], arr[j] = arr[j], arr[i]
#             if num > maxNum:
#                 maxNum = num
#             if num < minNum:
#                 minNum = num
#     print("#{} {} {}".format(test_case + 1, minNum, maxNum))

# boj 4949
# while True:
#     words = input()
#     ans = 'yes'
#     if words[0] == '.':
#         break
#     s = []
#     for i in words:
#         if i in '([':
#             s.append(i)
#         elif i in ')]':
#             if i == ')':
#                 if not s or s[- 1] != '(':
#                     ans = 'no'
#                     break
#                 else:
#                     s.pop(- 1)
#             else:
#                 if not s or s[- 1] != '[':
#                     ans = 'no'
#                     break
#                 else:
#                     s.pop(- 1)
#     if s:
#         ans = 'no'
#     print(ans)

# boj 2553
# import sys
# input = sys.stdin.readline
# n = int(input())
# num = 1
# for i in range(2, n + 1):
#     num *= i
#
# while True:
#     if num % 10:
#         ans = num % 10
#         break
#     num //= 10
# print(ans)

# boj 13171
# mod = 1000000007
# a = int(input()) % mod
# x = int(input())
# ans = 1
# while x:
#     if x % 2:
#         ans = (ans * a) % mod
#     a = (a * a) % mod
#     x >>= 1
# print(ans)

# boj 2447
# def makeStar():
#     l = len(stars)
#     arr = []
#     for i in range(l * 3):
#         if i // l == 1:
#             arr.append(stars[i % l] + " " * l + stars[i % l])
#         else:
#             arr.append(stars[i % l] * 3)
#     return arr
#
# n = int(input())
# stars = ["***", "* *", "***"]
# cnt = 0
# while n > 3:
#     n //= 3
#     cnt += 1
#
# for i in range(cnt):
#     stars = makeStar()
#
# for star in stars:
#     print(star)

# boj 5596
# s = sum(list(map(int, input().split())))
# t = sum(list(map(int, input().split())))
# print(max(s, t))

# boj 9184
# import sys
# input = sys.stdin.readline
# arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]
# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if arr[a][b][c]:
#         return arr[a][b][c]
#     if a < b < c:
#         arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#         return arr[a][b][c]
#     arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b- 1, c - 1)
#     return arr[a][b][c]
#
# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == - 1:
#         break
#     ans = w(a, b, c)
#     print("w({}, {}, {}) = {}".format(a, b, c, ans))

# boj 16918
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def dfs():
#     bomb = []
#     for i in range(R):
#         for j in range(C):
#             arr[i][j] += 1
#             if arr[i][j] == 3:
#                 arr[i][j] = - 1
#                 bomb.append([i, j])
#     for x, y in bomb:
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < R and 0 <= ny < C:
#                 arr[nx][ny] = - 1
#
# import sys
# input = sys.stdin.readline
# R, C, N = map(int, input().split())
# arr = [[- 1] * C for _ in range(R)]
#
# for i in range(R):
#     data = input().rstrip()
#     for j in range(len(data)):
#         if data[j] == 'O':
#             arr[i][j] = 1
#
# if N != 1:
#     time = 1
#     while True:
#         dfs()
#         time += 1
#         if time == N:
#             break
#
# for i in arr:
#     s = ''
#     for j in i:
#         if j == - 1:
#             s += '.'
#         else:
#             s += 'O'
#     print(s)

# boj11444
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [0, 1]
# for i in range(2, n + 1):
#     arr.append(arr[i - 2] + arr[i - 1])
# print(arr[n] % 1000000007)

# boj 24086
# a = int(input())
# b = int(input())
# print(b - a)

# boj 14716
# dx = [- 1, 1, 0, 0, - 1, - 1, 1, 1] # 상하좌우대각
# dy = [0, 0, - 1, 1, - 1, 1, - 1, 1]
#
# def bfs(x, y):
#     q = [[x, y]]
#     while q:
#         x, y = q.pop()
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if arr[nx][ny] and not visited[nx][ny]:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#
#
# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(m)]
# visited = [[False] * n for _ in range(m)]
# ans = 0
# for i in range(m):
#     for j in range(n):
#         if arr[i][j] and not visited[i][j]:
#             ans += 1
#             visited[i][j] = True
#             bfs(i, j)
# print(ans)

# boj 10995
# n = int(input())
# for i in range(n):
#     print(' *' * n) if i % 2 else print('* ' * n)

# boj 2556
# n = int(input())
# for _ in range(n):
#     print('*' * n)

# boj 10990
# n = int(input())
# print(' ' * (n - 1) + '*')
# for i in range(1, n):
#     print(' ' * (n - 1 - i) + '*' + ' ' * (2 * i - 1) + '*')

# boj 10993
# def star(x, y, n):
#     r, c = 2 ** n - 1, 2 ** (n + 1) - 3 # 행, 열
#     if n == 1:
#         arr[x][y] = '*'
#         return
#     if n % 2:   # add
#         for i in range(r - 1, - 1, - 1):
#             arr[x + r - 1 - i][y + i] = '*'
#             arr[x + r - 1 - i][y + c - 1 - i] = '*'
#             if i == 0:
#                 for j in range(1, c - 1):
#                     arr[x + r - 1][y + j] = '*'
#         star(x + 2 ** (n - 1) - 1, y + 2 ** (n - 1), n - 1)
#     else:   # even
#         for i in range(r):
#             arr[x + i][y + i] = '*'
#             arr[x + i][y + c - 1 - i] = '*'
#             if i == 0:
#                 for j in range(1, c - 1):
#                     arr[x][y + j] = '*'
#         star(x + 1, y + 2 ** (n - 1), n - 1)
#
# n = int(input())
# r, c = 2 ** n - 1, 2 ** (n + 1) - 3  # 행, 열
# arr = [[' '] * c for _ in range(r)]
# star(0, 0, n)
# for i in arr:
#     print(''.join(i).rstrip())

# boj 10994
# def star(x, n):
#     if n == 1:
#         arr[x][x] = '*'
#         return
#     l = 4 * n - 3
#     for i in range(l):
#         arr[x + i][x] = '*'
#         arr[x + i][l - 1 + x] = '*'
#         if i == 0 or i == l - 1:
#             for j in range(1, l):
#                 arr[x + i][x + j] = '*'
#     star(x + 2, n - 1)
#
# n = int(input())
# l = 4 * n - 3
# arr = [[' '] * l for _ in range(l)]
# star(0, n)
# for i in arr:
#     print(''.join(i).rstrip())

# boj 10997
# def star(x, y, cnt):
#     if cnt == 1:
#         arr[x][y], arr[x + 1][y], arr[x + 2][y] = '*', '*', '*'
#         return
#     r, c = 4 * cnt - 1, 4 * cnt - 3
#     for i in range(r):
#         if i == 0 or i == r - 1:
#             for j in range(c):
#                 arr[x + i][j + y] = '*'
#         else:
#             arr[x + i][y] = '*'
#             arr[x + i][c + y - 1] = '*'
#     star(x + 2, y + 2, cnt - 1)
#
# def relocation(x, y, cnt):
#     if cnt == 1:
#         return
#     arr[x][y], arr[x + 1][y - 1] = arr[x + 1][y - 1], arr[x][y]
#     relocation(x + 2, y - 2, cnt - 1)
#
#
# n = int(input())
# if n == 1:
#     print("*")
# else:
#     r, c = 4 * n - 1, 4 * n - 3
#     arr = [[' '] * c for _ in range(r)]
#     star(0, 0, n)
#     relocation(1, - 1, n)
#     for i in arr:
#         print(''.join(i).rstrip())

# boj 13015
# n = int(input())
# r, c = 2 * n - 1, 4 * n - 3
# arr = [[' '] * c for _ in range(r)]
# for i in range(n):
#     arr[0][i] = arr[0][- 1 - i] = arr[- 1][i] = arr[- 1][- 1 - i] = '*'
# x = 1
# for i in range(1, r - 1):
#     arr[i][x] = arr[i][x + n - 1] = arr[i][- x - 1] = arr[i][- x - n] = '*'
#     if i < r // 2:
#         x += 1
#     else:
#         x -= 1
# for i in arr:
#     print(''.join(i).rstrip())

# boj 18883
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# num = 1
# for _ in range(n):
#     for _ in range(m):
#         if num % m:
#             print(num, end = ' ')
#         else:
#             print(num, end= '')
#         num += 1
#     print()

# boj 17247
# n, m = map(int, input().split())
# ax, ay, bx, by = 0, 0, 0, 0
# chk = False
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(m):
#         if data[j] and not chk:
#             ax, ay = i, j
#             chk = True
#         if data[j] and chk:
#             bx, by = i, j
# print(abs(bx - ax) + abs(by - ay))

# boj 2628
# c, r = map(int, input().split())
# n = int(input())
# garo, sero = [0, c], [0, r]
# ans = 0
# for _ in range(n):
#     div, num = map(int, input().split())    # div == 0 가로 div == 1 세로
#     if div: # 세로
#         garo.append(num)
#     else:   # 가로
#         sero.append(num)
#
# garo, sero = sorted(garo), sorted(sero)
# for i in range(1, len(garo)):
#     garoLen = garo[i] - garo[i - 1]
#     for j in range(1, len(sero)):
#         seroLen = sero[j] - sero[j - 1]
#         if ans < garoLen * seroLen:
#             ans = garoLen * seroLen
# print(ans)

# boj 4358
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# dic = defaultdict(int)
# cnt = 0
# while True:
#     s = input().rstrip()
#     if not s:
#         break
#     dic[s] += 1
#     cnt += 1
#
# for i in sorted(list(dic.keys())):
#     print('%s %.4f' % (i, dic[i] / cnt * 100))

# boj 4779
# def solve(s, e):
#     temp = e // 3
#     if temp == 0:
#         return
#
#     for i in range(s + temp, s + temp * 2):
#         arr[i] = ' '
#
#     solve(s, temp)
#     solve(s + temp * 2, temp)
#
# while True:
#     try:
#         n = int(input())
#         arr = ['-'] * pow(3, n)
#         solve(0, pow(3, n))
#         print(''.join(arr))
#     except EOFError:
#         break

# boj 1072
# x, y = map(int, input().split())
# if x == y == 0:
#     print(1)
# elif x == y:
#     print(- 1)
# else:
#     z = int((100 * y) / x)
#     if 99 - z == 0:
#         print(- 1)
#     else:
#         k = ((z + 1) * x - 100 * y) / (99 - z)
#         k = int(k) if k == int(k) else int(k) + 1
#         print(k)

# boj 1543
# words = input()
# s = input()
# l = len(s)
# i, ans = 0, 0
# while True:
#     if words[i : i + l] == s:
#         ans += 1
#         i += l
#     else:
#         i += 1
#     if i > len(words) - l:
#         break
# print(ans)

# boj 1476
# E, S, M = map(int, input().split())
# e = s = m = 1
# ans = 1
# while True:
#     if e == E and s == S and m == M:
#         break
#     else:
#         e += 1
#         s += 1
#         m += 1
#         if e == 16:
#             e = 1
#         if s == 29:
#             s = 1
#         if m == 20:
#             m = 1
#         ans += 1
# print(ans)

# boj 15903
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# while m:
#     arr[0] = arr[1] = arr[0] + arr[1]
#     arr = sorted(arr)
#     m -= 1
# print(sum(arr))

# boj 2563
# n = int(input())
# arr = [[0] * 100 for _ in range(100)]
# ans = 0
# for _ in range(n):
#     x, y = map(int, input().split())
#     for i in range(x, x + 10):
#         for j in range(y, y + 10):
#             if arr[i][j] == 0:
#                 arr[i][j] = 1
#                 ans += 1
# print(ans)

# boj 10769
# s = input()
# h, s = s.count(":-)"), s.count(":-(")
# if h > s:
#     print("happy")
# elif h < s:
#     print("sad")
# elif h == s == 0:
#     print("none")
# else:
#     print("unsure")

# boj 6359
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = [0] * (n + 1)
#     for i in range(2, n + 1):
#         for j in range(i, n + 1, i):
#             if arr[j]:
#                 arr[j] = 0
#             else:
#                 arr[j] = 1
#     print(arr[1:].count(0))

# boj 4562
# t = int(input())
# for _ in range(t):
#     x, y = map(int, input().split())
#     print("MMM BRAINS") if x >= y else print("NO BRAINS")

# boj 15312
# alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
# a = input()
# b = input()
# arr = []
# for x, y in zip(a, b):
#     arr.append(alpha[ord(x) - 65])
#     arr.append(alpha[ord(y) - 65])
# temp = []
# while len(arr) > 2:
#     temp = []
#     for i in range(len(arr) - 1):
#         tot = (arr[i] + arr[i + 1]) % 10
#         temp.append(tot)
#     arr = temp
# ans = arr[0] * 10 + arr[1]
# if ans < 10:
#     print('0' + str(ans))
# else:
#     print(ans)

# boj 2422
# n, m = map(int, input().split())
# graph = [[1] * (n + 1) for _ in range(n + 1)]
# ans = 0
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x][y] = graph[y][x] = 0
#
# for i in range(1, n - 1):
#     for j in range(i + 1, n):
#         if graph[i][j]:
#             for k in range(j + 1, n + 1):
#                 if graph[i][k] == 0 or graph[j][k] == 0:
#                     continue
#                 ans += 1
# print(ans)

# boj 14561
# t = int(input())
# for _ in range(t):
#     a, n = map(int, input().split())
#     s = ''
#     while a > 0:
#         s = str(hex(a % n)[2:]) + s
#         a //= n
#     print(1) if s == s[:: - 1] else print(0)

# boj 15969
# # 방법 1
# n = int(input())
# arr = list(map(int, input().split()))
# print(max(arr) - min(arr))
#
# # 방법 2
# n = int(input())
# arr = list(map(int, input().split()))
# maxNum, minNum = - 1, 1001
# for i in arr:
#     if maxNum < i:
#         maxNum = i
#     if minNum > i:
#         minNum = i
# print(maxNum - minNum)

# boj 1759
# def chk(password):
#     mo, ja = 0, 0
#     for i in password:
#         if i in "aeiou":
#             mo += 1
#         else:
#             ja += 1
#     return ja >= 2 and mo >= 1
#
# def solve(n, arr, password, idx):
#     if len(password) == n:
#         if chk(password):
#             print(password)
#         return
#     if idx == len(arr):
#         return
#     solve(n, arr, password + arr[idx], idx + 1)
#     solve(n, arr, password, idx + 1)
#
# l, c = map(int, input().split())
# arr = sorted(input().split())
# solve(l, arr, "", 0)

# boj 1212
# num = input()
# ans = ''
# for i in num:
#     n = int(i)
#     temp = ''
#
#     while n:
#         temp += str(n % 2)
#         n //= 2
#     if ans:
#         while len(temp) < 3:
#             temp = temp + '0'
#     ans += temp[:: - 1]
#
# print(ans) if ans else print(0)

# boj 11005
# notation = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n, b = map(int, input().split())
# ans = ''
# while n:
#     ans += notation[n % b]
#     n //= b
# print(ans[::- 1])

# boj 9610
# arr = [0] * 5
# n = int(input())
# for _ in range(n):
#     x, y = map(int, input().split())
#     if x > 0:
#         if y > 0:
#             arr[0] += 1
#         elif y < 0:
#             arr[3] += 1
#         else:
#             arr[4] += 1
#     elif x < 0:
#         if y > 0:
#             arr[1] += 1
#         elif y < 0:
#             arr[2] += 1
#         else:
#             arr[4] += 1
#     else:
#         arr[4] += 1
#
# for i in range(4):
#     print("Q{}: {}".format(i + 1, arr[i]))
# print("AXIS: {}".format(arr[4]))

# boj 1783
# n, m = map(int, input().split())
# if n == 1:
#     ans = 1
# elif n == 2:
#     ans = min(4, (m - 1) // 2 + 1)
# else:
#     ans = m - 2 if m >= 7 else min(4, m)
# print(ans)

# oneline
# n, m = map(int, input().split())
# print(1 if n == 1 else min(4, (m - 1) // 2 + 1) if n == 2 else m - 2 if m >= 7 else min(4, m))

# boj 1598
# a, b = map(int, input().split())
# a -= 1
# b -= 1
# print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))

# boj 10101
# a = int(input())
# b = int(input())
# c = int(input())
# l = set([a, b, c])
# if a + b + c == 180:
#     l = set([a, b, c])
#     print("Equilateral") if len(l) == 1 else print("Isosceles") if len(l) == 2 else print("Scalene")
# else:
#     print("Error")

# boj 5176
# t = int(input())
# for _ in range(t):
#     p, m = map(int, input().split())
#     visited = [0] * (m + 1)
#     ans = 0
#     for _ in range(p):
#         n = int(input())
#         if visited[n]:
#             ans += 1
#         else:
#             visited[n] = 1
#     print(ans)

# boj 4880
# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     if b - a == c - b:
#         print("AP {}".format(c + b - a))
#     else:
#         print("GP {}".format(c * (b // a)))

# boj 14920
# n = int(input())
# cnt = 1
# while n != 1:
#     if n % 2:
#         n = 3 * n + 1
#     else:
#         n //= 2
#     cnt += 1
# print(cnt)

# boj 13241
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# a, b = map(int, input().split())
# gcd = gcd(a, b)
# print(a * b // gcd)

# boj 17285
# s = input()
# ans = ''
# key = ord(s[0]) ^ ord("C")
# for i in s:
#     ans += chr(ord(i) ^ key)
# print(ans)

# boj 2511
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# Ascore, Bscore = 0, 0
# chk = 3
# for i, j in zip(A, B):
#     if i > j:
#         Ascore += 3
#         chk = 1
#     elif i < j:
#         Bscore += 3
#         chk = 2
#     else:
#         Ascore += 1
#         Bscore += 1
#
# print(Ascore, Bscore)
# if Ascore > Bscore:
#     print("A")
# elif Ascore < Bscore:
#     print("B")
# else:
#     if chk == 1:
#         print("A")
#     elif chk == 2:
#         print("B")
#     else:
#         print("D")

# boj 2622
# n = int(input())
# ans = 0
# for i in range(1, n):
#     if (3 * i >= n) and 2 * i < n:
#         ans += i - (n - i - 1) // 2
# print(ans)

# boj 11729
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, c)
#         hanoi(n - 1, b, a, c)
#
# n = int(input())
# print(2 ** n - 1)
# hanoi(n, 1, 2, 3)

# boj 14620
# dx = [0, - 1, 1, 0, 0]
# dy = [0, 0, 0, - 1, 1]
# def chk(x, y, flag):
#     if flag:
#         price = 0
#         for k in range(5):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             price += arr[nx][ny]
#         return price
#     else:
#         for k in range(5):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if visited[nx][ny]:
#                 return False
#         return True
#
# def dfs(idx, cnt, cost):
#     global ans
#     if cnt == 3:
#         if ans > cost:
#             ans = cost
#             return
#     for x in range(idx, n - 1):
#         for y in range(1, n - 1):
#             if chk(x, y, 0):
#                 for k in range(5):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     visited[nx][ny] = 1
#                 price = chk(x, y, 1)
#                 if ans > cost + price:
#                     dfs(idx, cnt + 1, cost + price)
#                 for k in range(5):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     visited[nx][ny] = 0
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# ans = float('inf')
# dfs(1, 0, 0)
# print(ans)

# boj 1236
# def chk(i, j):
#     for x in range(n):
#         visited[x][j] = 1
#     for y in range(m):
#         visited[i][y] = 1
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# arrT = list(zip(*arr))
# visited = [[0] * m for _ in range(n)]
# ans = 0
#
# for i in range(n):
#     if 'X' not in arr[i]:
#         for j in range(m):
#             visited[i][j] += 1
# for j in range(m):
#     if 'X' not in arrT[j]:
#         for i in range(n):
#             visited[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == 2:
#             ans += 1
# print(ans)

# swea 1
# T = int(input())
# for test_case in range(T):
#     so = se = 0
#     s = input()
#     ans = "YES"
#     for i in s:
#         if i == 'o':
#             so += 1
#             if so == 8:
#                 ans = "YES"
#                 break
#         else:
#             se += 1
#             if se == 8:
#                 ans = "NO"
#                 break
#     print("#{} {}".format(test_case + 1, ans))

# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# def sol(arr):
#     global chk
#     g1, g2, g3 = gcd(arr[0], arr[1]), gcd(arr[0], arr[2]), gcd(arr[1], arr[2])
#     if g1 == 1:
#         if g2 == 1:
#             if g3 == 1:
#                 res = 1
#             else:
#                 res = g3
#         else:
#             if g3 == 1:
#                 res = g2
#             else:
#                 res = g3
#     else:
#         if g2 == 1:
#             if g3 == 1:
#                 res = g1
#             else:
#                 res = max(g1, g3)
#         else:
#             res = max(g1, g2, g3)
#             chk = 1
#     return res
#
# T = int(input())
# for test_case in range(T):
#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     ans = arr[1]
#     chk = 0
#     if n > 2:
#         ans = sol(arr)
#         for i in arr[3:]:
#             if gcd(ans, i) == 1:
#                 if chk:
#                     chk = 0
#                 else:
#                     ans = 1
#                     break
#             else:
#                 if ans > gcd(ans, i):
#                     ans = gcd(ans, i)
#     print("#{} {}".format(test_case + 1, ans))

# boj 11931
# n = int(input())
# arr = sorted([int(input()) for _ in range(n)])[:: - 1]
# for i in arr:
#     print(i)

# boj 17608
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)][:: - 1]
# ans = 1
# num = arr[0]
# for i in arr[1:]:
#     if i > num:
#         ans += 1
#         num = i
# print(ans)

# boj 9656
# print('CY' if int(input()) % 2 else 'SK')

# boj 2605
# n = int(input())
# data = list(map(int, input().split()))
# arr = []
# idx = 1
# for i in data:
#     if i == 0:
#         arr.append(idx)
#     else:
#         arr.insert(- i, idx)
#     idx += 1
# print(*arr)

# boj 19539
# n = int(input())
# arr = list(map(int, input().split()))
# total = sum(arr)
# apple = sum(arr) // 3
# ans = 'NO'
# if not total % 3:
#     for i in arr:
#         apple -= i // 2
#     ans = 'NO' if apple > 0 else 'YES'
# print(ans)

# boj 1063
# d = {'R': (1, 0), 'L': (- 1, 0), 'B': (0, - 1), 'T': (0, 1),
#      'RT': (1, 1), 'LT': (- 1, 1), 'RB': (1, - 1), 'LB': (- 1, - 1)}
#
# def chk(x, y):
#     if 0 < x <= 8 and 0 < y <= 8:
#         return True
#     return False
#
# x, y, n = input().split()
# kx, ky, sx, sy = ord(x[0]) - 64, int(x[1]), ord(y[0]) - 64, int(y[1])
# s, y = '', ''
# for _ in range(int(n)):
#     val = input()
#     nkx, nky = kx + d[val][0], ky + d[val][1]
#     if chk(nkx, nky):
#         if (nkx, nky) == (sx, sy):
#             nsx, nsy = sx + d[val][0], sy + d[val][1]
#             if chk(nsx, nsy):
#                 kx, ky, sx, sy = nkx, nky, nsx, nsy
#         else:
#             kx, ky = nkx, nky
# k = chr(kx + 64) + str(ky)
# s = chr(sx + 64) + str(sy)
# print(k)
# print(s)

# boj 14720
# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# milk = 0
# for i in arr:
#     if milk == 0:
#         if i == 0:
#             ans += 1
#             milk += 1
#     elif milk == 1:
#         if i == 1:
#             ans += 1
#             milk += 1
#     else:
#         if i == 2:
#             ans += 1
#             milk = 0
# print(ans)

# boj 2742
# n = int(input())
# for i in range(n, 0, - 1):
#     print(i)

# boj 1300
# n = int(input())
# k = int(input())
# l, r = 1, n * n
#
# while l <= r:
#     m = (l + r) // 2
#
#     cnt = 0
#     for i in range(1, n + 1):
#         cnt += min(m // i, n)
#
#     if cnt >= k:
#         r = m - 1
#     else:
#         l = m + 1
# print(l)

# boj 10814
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for i in range(n):
#     age, name = input().split()
#     arr.append([int(age), name, i])
# arr.sort(key= lambda x: (x[0], x[2]))
# for i in arr:
#     print(i[0], i[1])

# boj 14697
# a, b, c, n = map(int, input().split())
# dp = [0] * (301)
# dp[a] = dp[b] = dp[c] = 1
# for i in range(a, n + 1):
#     for j in [a, b, c]:
#         if i >= j and dp[i - j]:
#             dp[i] = 1
# print(dp[n])

# boj 12833
# a, b, c = map(int, input().split())
# for _ in range(c % 2):
#     a ^= b
# print(a)

# boj 2022
# x, y, c = map(float, input().split())
# l, r = 0, min(x, y)
# while abs(l - r) > pow(10, - 6):
#     d = (l + r) / 2
#     h1 = (x * x - d * d) ** 0.5
#     h2 = (y * y - d * d) ** 0.5
#     h = (h1 * h2) / (h1 + h2)
#     if h > c:
#         l = d
#     else:
#         r = d
# print(format(d, ".3f"))

# boj 1864
# octopus = '-\(@?>&%'
# while True:
#     s = input()
#     if s == '#':
#         break
#     slen = len(s) - 1
#     ans = 0
#     for i in s:
#         if i in octopus:
#             temp = octopus.index(i)
#         else:
#             temp = - 1
#         ans += temp * (8 ** slen)
#         slen -= 1
#     print(ans)

# boj 10822
# print(sum(list(map(int, input().split(',')))))

# boj 22950
# n = int(input())
# m = input()
# k = int(input())
# cnt = 0
# if '1' not in m or k == 0:
#     print("YES")
#     exit(0)
# for i in m[:: - 1]:
#     if i == '1':
#         break
#     cnt += 1
# print("YES" if cnt >= k else "NO")

# boj 2346
# from collections import deque
# n = int(input())
# arr = list(map(int, input().split()))
# dq = deque()
# for idx, num in enumerate(arr, 1):
#     dq.append([idx, num])
# ans = []
# while dq:
#     idx, move = dq.popleft()
#     ans.append(idx)
#     if len(dq) == 1:
#         ans.append(dq.pop()[0])
#     else:
#         if move > 0:
#             for _ in range(move - 1):
#                 dq.append(dq.popleft())
#         else:
#             for _ in range(abs(move)):
#                 dq.appendleft(dq.pop())
# print(*ans)

# boj 1388
# def dfs(x, y, c):
#     if c == '-':
#         while True:
#             y += 1
#             if y == m:
#                 break
#             if arr[x][y] == c:
#                 visited[x][y] = 1
#             else:
#                 break
#     else:
#         while True:
#             x += 1
#             if x == n:
#                 break
#             if arr[x][y] == c:
#                 visited[x][y] = 1
#             else:
#                 break
#
# n, m = map(int, input().split())
# arr = [input() for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == '-' and not visited[i][j]:
#             ans += 1
#             dfs(i, j, '-')
#             visited[i][j] = 1
#         elif arr[i][j] == '|' and not visited[i][j]:
#             ans += 1
#             dfs(i, j, '|')
#             visited[i][j] = 1
# print(ans)

# boj 7567
# s = input()
# ans = 10
# temp = s[0]
# for i in s[1:]:
#     if temp == i:
#         ans += 5
#     else:
#         temp = i
#         ans += 10
# print(ans)

# boj 4677
# dx = [- 1, 1, 0, 0, 1, 1, - 1, - 1]
# dy = [0, 0, - 1, 1, - 1, 1, - 1, 1]
# def dfs(x, y):
#     for k in range(8):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if arr[nx][ny] == '@' and not visited[nx][ny]:
#                 visited[nx][ny] = 1
#                 dfs(nx, ny)
#
# while True:
#     n, m = map(int, input().split())
#     if n == m == 0:
#         break
#     arr = [input() for _ in range(n)]
#     ans = 0
#     visited = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == '@' and not visited[i][j]:
#                 visited[i][j] = 1
#                 dfs(i, j)
#                 ans += 1
#     print(ans)

# boj 1937
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def dfs(x, y):
#     if dp[x][y]:
#         return dp[x][y]
#     dp[x][y] = 1
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < n:
#             if arr[x][y] < arr[nx][ny]:
#                 dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
#     return dp[x][y]
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# ans = 0
#
# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dfs(i, j))
# print(ans)

# boj 2636
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def bfs():
#     visited = [[0] * m for _ in range(n)]
#     dq = deque()
#     dq.append((0, 0))
#     visited[0][0] = 1
#     cheese = 0
#
#     while dq:
#         x, y = dq.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny]:
#                     if arr[nx][ny] == 0:
#                         dq.append((nx, ny))
#                         visited[nx][ny] = 1
#                     else:
#                         visited[nx][ny] = 1
#                         arr[nx][ny] = 0
#                         cheese += 1
#     ans.append(cheese)
#     return cheese
#
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = []
# while True:
#     cnt = bfs()
#     if cnt == 0:
#         break
# print(len(ans) - 1)
# print(ans[- 2])

# boj 23348
# a, b, c = map(int, input().split())
# n = int(input())
# idx = 0
# arr = [0] * n
# while idx < n:
#     for i in range(3):
#         x, y, z = map(int, input().split())
#         arr[idx] += x * a + y * b + z * c
#     idx += 1
# print(max(arr))

# t = int(input())
# for _ in range(t):
#     n, d = map(int, input().split())
#     ans = 0
#     for _ in range(n):
#         v, f, c = map(int, input().split())
#         if v * (f / c) >= d:
#             ans += 1
#     print(ans)

# boj 2754
# credit = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
#           'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
#           'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
#           'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
#           'F': 0.0}
# print(credit[input()])

# boj 13022
# import sys
# s = input()
# idx = 0
# while idx < len(s):
#     for i in range(1, 14):
#         if idx + i * 4 > len(s):
#             print(0)
#             sys.exit(0)
#         if s[idx : idx + i] == 'w' * i:
#             if s[idx + i : idx + i * 2] == 'o'* i:
#                 if s[idx + i * 2: idx + i * 3] == 'l'* i:
#                     if s[idx + i * 3 : idx + i * 4] == 'f' * i:
#             idx += i * 4
#             break
# print(1)

# boj 13417
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(input().split())
#     s = arr[0]
#     l = r = ord(s)
#     for i in arr[1:]:
#         c = ord(i)
#         if l < c:
#             s += i
#             r = c
#         else:
#             s = i + s
#             l = c
#     print(s)

# boj 1051
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# ans = 1
# idx = 1
# for i in range(n):
#     for j in range(m):
#         temp = arr[i][j]
#         k = idx
#         while i + k < n and j + k < m:
#             if arr[i + k][j + k] == temp:
#                 if arr[i][j + k] == arr[i + k][j] == temp:
#                     if ans < (k + 1) ** 2:
#                         ans = (k + 1) ** 2
#                         idx = k
#             k += 1
# print(ans)

# boj 1780
# import sys
# input = sys.stdin.readline
# def dfs(x, y, n):
#     global ans
#     val = arr[x][y]
#     for nx in range(x, x + n):
#         for ny in range(y, y + n):
#             if arr[nx][ny] != val:
#                 for i in range(3):
#                     for j in range(3):
#                         dfs(x + i * n // 3, y + j * n // 3, n // 3)
#                 return
#
#     if val == - 1:
#         ans[0] += 1
#     elif val == 0:
#         ans[1] += 1
#     else:
#         ans[2] += 1
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = [0, 0, 0]
# dfs(0, 0, N)
# for i in ans:
#     print(i)

# boj 1145
# arr = sorted(list(map(int, input().split())))
# ans = arr[0]
# while True:
#     cnt = 0
#     for i in range(5):
#         if ans % arr[i] == 0:
#             cnt += 1
#     if cnt > 2:
#         break
#     ans += 1
# print(ans)

# boj 24510
# n = int(input())
# ans = 0
# for _ in range(n):
#     data = input()
#     cnt = data.count('for') + data.count('while')
#     if ans < cnt:
#         ans = cnt
# print(ans)

# boj 5524
# n = int(input())
# for _ in range(n):
#     print(input().lower())

# boj 15624
# def fib(n):
#     if n >= 2:
#         for i in range(2, n):
#             memo.append((memo[i - 1] + memo[i]) % 1000000007)
#     return memo[n]
#
# n = int(input())
# memo = [0, 1, 1]
# f1 ,f2, f3 = 0, 1, 1
# print(fib(n))

# boj 1526
# n = int(input())
# while True:
#     chk = True
#     for i in str(n):
#         if i not in '47':
#             chk = False
#             n -= 1
#     if chk:
#         print(n)
#         break

# boj 6322
# test_case = 0
# while True:
#     test_case += 1
#     chk = False
#
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     if test_case != 1:
#         print()
#     print("Triangle #{}".format(test_case))
#     if a == - 1:
#         temp = (c ** 2 - b ** 2)
#         if temp > 0:
#             ans1 = 'a'
#             ans2 = temp ** 0.5
#             ans = True
#             chk = True
#     if b == - 1:
#         temp = (c ** 2 - a ** 2)
#         if temp > 0:
#             ans1 = 'b'
#             ans2 = temp ** 0.5
#             chk = True
#     if c == - 1:
#         temp = (a ** 2 + b ** 2)
#         if temp > 0:
#             ans1 = 'c'
#             ans2 = temp ** 0.5
#             chk = True
#     if chk:
#         print("{} = {}".format(ans1, format(ans2, ".3f")))
#     else:
#         print("Impossible.")

# boj 1309
# n = int(input())
# dp = [1] * (n + 1)
# dp[1] = 3
# for i in range(2, n + 1):
#     dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
# print(dp[n])

# boj 3029
# h1, m1, s1 = map(int, input().split(':'))
# h2, m2, s2 = map(int, input().split(':'))
# h = h2 - h1
# m = m2 - m1
# s = s2 - s1
# if s < 0:
#     s += 60
#     m -= 1
# if m < 0:
#     m += 60
#     h -= 1
# if h < 0:
#     h += 24
# if h == m == s == 0:
#     print("24:00:00")
# else:
#     if h < 10:
#         h = '0' + str(h)
#     if m < 10:
#         m = '0' + str(m)
#     if s < 10:
#         s = '0' + str(s)
#     print("{}:{}:{}".format(h, m, s))

# boj 2851
# ans = int(input())
# arr = [int(input()) for _ in range(9)]
# for i in arr:
#     ans += i
#     if ans >= 100:
#         if ans - 100 > 100 - ans + i:
#             ans -= i
#         break
# print(ans)

# boj 2527
# for _ in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
#     rec1 = [abs(x1 + p1) / 2, abs(y1 + q1) / 2]
#     rec2 = [abs(x2 + p2) / 2, abs(y2 + q2) / 2]
#
#     dx1, dy1 = abs(rec1[0] - x1), abs(rec1[1] - y1)
#     dx2, dy2 = abs(rec2[0] - x2), abs(rec2[1] - y2)
#     xd, yd = abs(rec1[0] - rec2[0]), abs(rec1[1] - rec2[1])
#
#     if dx1 + dx2 == xd:
#         if dy1 + dy2 == yd:
#             print('c')
#         elif dy1 + dy2 < yd:
#             print('d')
#         else:
#             print('b')
#     elif dx1 + dx2 < xd:
#         print('d')
#     else:
#         if dy1 + dy2 == yd:
#             print('b')
#         elif dy1 + dy2 < yd:
#             print('d')
#         else:
#             print('a')

# boj 10867
# n = int(input())
# arr = sorted(set(map(int, input().split())))
# print(*arr)

# boj 14912
# n, d = input().split()
# ans = 0
# for i in range(1, int(n) + 1):
#     ans += str(i).count(d)
# print(ans)

# boj 14916
# n = int(input())
# if n == 1 or n == 3:
#     print(- 1)
# else:
#     ans = n // 5
#     n %= 5
#     if n == 1 or n == 4:
#         ans += 2
#     elif n == 2:
#         ans += 1
#     elif n == 3:
#         ans += 3
#     print(ans)

# boj 21919
# import sys
# input = sys.stdin.readline
# def findPrime(n):
#     for i in range(2, n):
#         if i * i > n:
#             break
#         if n % i == 0:
#             return False
#     return True
#
# n = int(input())
# arr = set(map(int, input().split()))
# ans = 1
# for i in arr:
#     if findPrime(i):
#         ans *= i
#
# if ans == 1:
#     print(- 1)
# else:
#     print(ans)

# boj 16173
# from collections import deque
#
# dx = [1, 0]
# dy = [0, 1]
#
# def bfs(x, y, val):
#     q = deque()
#     q.append((x, y, val))
#     while q:
#         x, y, val = q.popleft()
#         if arr[x][y] == - 1:
#             return True
#         for k in range(2):
#             nx = x + dx[k] * val
#             ny = y + dy[k] * val
#             if nx < n and ny < n:
#                 if not visited[nx][ny]:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny, arr[nx][ny]))
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# print("HaruHaru" if bfs(0, 0, arr[0][0]) else "Hing")

# boj 17212
# n = int(input())
# dp = [float('inf')] * (n + 1)
# dp[0] = 0
# for i in range(1, n + 1):
#     for coin in (7, 5, 2, 1):
#         if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
#             dp[i] = dp[i - coin] + 1
# print(dp[n])

# boj 4328
# def solve(num, b):
#     res = ''
#     while num >= b:
#         res += str(num % b)
#         num //= b
#     res += str(num)
#     return res[:: - 1]
#
# while True:
#     data = input()
#     if data == '0':
#         break
#     b, p, m = data.split()
#     b = int(b)
#     num1 = int(p, b)
#     print(solve(int(p, b) % int(m, b), b))

# boj 11723
# import sys
# input = sys.stdin.readline
# n = int(input())
# s = set()
# for _ in range(n):
#     data = input().split()
#     if len(data) == 1:
#         if data[0] == 'all':
#             s = set(i for i in range(1, 21))
#         else:
#             s = set()
#     else:
#         f, x = data[0], int(data[1])
#         if f == 'add':
#             s.add(x)
#         elif f == 'remove':
#             s.discard(x)
#         elif f == 'check':
#             print(1 if x in s else 0)
#         elif f == 'toggle':
#             s.discard(x) if x in s else s.add(x)

# boj 1748
# n = int(input())
# ans, i = 0, 1
# while i <= n:
#     ans += (n - i + 1)
#     i *= 10

# boj 2154
# n = int(input())
# s = ''
# for i in range(1, n + 1):
#     s += str(i)
# print(s.index(str(n)) + 1)

# boj 1194
# from collections import deque
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def bfs(x, y, c, cnt):
#     cnt = 0
#     q = deque()
#     q.append((x, y, c, cnt))
#     while q:
#         x, y, c, cnt = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#' and not visited[nx][ny][c]:
#                 if arr[nx][ny] == '.':
#                     visited[nx][ny][c] = 1
#                     q.append((nx, ny, c, cnt + 1))
#                 elif arr[nx][ny] == '1':
#                     return cnt + 1
#                 else:
#                     if arr[nx][ny] in 'ABCDEF':
#                         if c & 1 << (ord(arr[nx][ny]) - 65):
#                             visited[nx][ny][c] = 1
#                             q.append((nx, ny, c, cnt + 1))
#                     else:
#                     # elif arr[nx][ny] in 'abcdef':
#                         nc = c | (1 << ord(arr[nx][ny]) - 97)
#                         if not visited[nx][ny][nc]:
#                             visited[nx][ny][nc] = 1
#                             q.append((nx, ny, nc, cnt + 1))
#     return - 1
#
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == '0':
#             visited[i][j][0] = 1
#             arr[i][j] = '.'
#             print(bfs(i, j, 0, 0))
#             break

# boj 2665
# from collections import deque
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def bfs():
#     visited[0][0] = 0
#     q = deque()
#     q.append((0, 0, 0))
#     while q:
#         x, y, c = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if arr[nx][ny] == '0':
#                     if visited[nx][ny] > visited[x][y] + 1:
#                         visited[nx][ny] = visited[x][y] + 1
#                         q.append((nx, ny, visited[nx][ny]))
#                 else:
#                     if visited[nx][ny] > visited[x][y]:
#                         visited[nx][ny] = visited[x][y]
#                         q.append((nx, ny, visited[nx][ny]))
#
# n = int(input())
# arr = [list(input()) for _ in range(n)]
# visited = [[float('inf')] * n for _ in range(n)]
# bfs()
# print(visited[n - 1][n - 1])

# boj 2206
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def bfs():
#     q = deque()
#     q.append((0, 0, 0))
#     visited[0][0][0] = 1
#     while q:
#         x, y, c = q.popleft()
#         if x == n - 1 and y == m - 1:
#             return visited[x][y][c]
#
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][c]:
#                 if arr[nx][ny] == '0':
#                     q.append((nx, ny, c))
#                     visited[nx][ny][c] = visited[x][y][c] + 1
#
#                 if c == 0 and arr[nx][ny] == '1':
#                     q.append((nx, ny, 1))
#                     visited[nx][ny][1] = visited[x][y][c] + 1
#     return - 1
#
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
# print(bfs())

# boj 1343
# s = input()
# arr = []
# ans = ''
# temp = 0
# chk = 1
# for i in s:
#     if i != '.':
#         temp += 1
#     else:
#         if temp:
#             if temp % 2:
#                 print(- 1)
#                 chk = 0
#                 break
#             arr.append(temp)
#         arr.append(i)
#         temp = 0
# else:
#     if temp:
#         if temp % 2:
#             print(- 1)
#             chk = 0
#         arr.append(temp)
#
# if chk:
#     for i in arr:
#         if i == '.':
#             ans += i
#         else:
#             m, n = i // 4, i % 4
#             if n:
#                 ans += "AAAA" * m + "BB"
#             else:
#                 ans += "AAAA" * m
#     print(ans)

# boj 10159
# n = int(input())
# m = int(input())
# arr = [[0] * n for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[a - 1][b - 1] = 1
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if arr[i][k] and arr[k][j]:
#                 arr[i][j] = 1
#
# for i in range(n):
#     ans = - 1
#     for j in range(n):
#         if not arr[i][j] and not arr[j][i]:
#             ans += 1
#     print(ans)

# boj 23825
# n, m = map(int, input().split())
# print(min(n // 2, m // 2))

# boj 1431
# n = int(input())
# arr = []
# for _ in range(n):
#     data = input()
#     num = 0
#     for i in data:
#         if i in '123456789':
#             num += int(i)
#     arr.append((data, num))
# arr.sort(key= lambda x : (len(x[0]), x[1], x[0]))
# for i in arr:
#     print(i[0])

# boj 16435
# n, l = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# for i in arr:
#     if l >= i:
#         l += 1
#     else:
#         break
# print(l)

# boj 11053
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1] * n
# for i in range(n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# boj 2965
# a, b, c = map(int, input().split())
# print(max(b - a, c - b) - 1)

# boj 1037
# n = int(input())
# arr = sorted(list(map(int, input().split())))
# print(arr[0] * arr[- 1])

# boj 13300
# n, k = map(int, input().split())
# arr = [[0] * 6 for _ in range(2)]
# ans = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     arr[x][y - 1] += 1
#
# for i, j in zip(arr[0], arr[1]):
#     ans += i // k
#     if i % k:
#         ans += 1
#     ans += j // k
#     if j % k:
#         ans += 1
# print(ans)

# boj 11023
# print(sum(list(map(int, input().split()))))

# boj 2502
# d, k = map(int, input().split())
# f = [1, 0]
# s = [0, 1]
# p, q, ans = 0, 0, 1
# for i in range(3, d + 1):
#     p = f[0] + s[0]
#     q = f[1] + s[1]
#     f = s
#     s = [p, q]
#
# while True:
#     x = p * ans
#     y = k - x
#     if not y % q:
#         print(ans)
#         print(y // q)
#         break
#     ans += 1

# swea 1
# def solve(r, c):
#     idx, jdx = 0, 0
#     while r + idx < N:
#         if arr[r + idx][c] == '#':
#             idx += 1
#         else:
#             break
#
#     while c + jdx < M:
#         if arr[r][c + jdx] == '#':
#             jdx += 1
#         else:
#             break
#
#     if idx != jdx:
#         return 'no'
#
#     for x in range(r, r + idx):
#         for y in range(c, c + jdx):
#             visited[x][y] = 1
#             if arr[x][y] == '.':
#                 return "no"
#
#     return "yes"
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     M = len(arr[0])
#     visited = [[0] * M for _ in range(N)]
#     chk = True
#     ans = 'yes'
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == '#' and not visited[i][j]:
#                 if chk:
#                     chk = False
#                     ans = solve(i, j)
#                 else:
#                     ans = 'no'
#                     break
#
#     print("#{} {}".format(test_case + 1, ans))

# swea 2
# T = int(input())
# for test_case in range(T):
#     A, B, K = map(int, input().split())
#     P, Q = min(A, B), max(A, B)
#     idx = 1
#     arr = []
#     while K:
#         num = P
#         P, Q = P + num, Q - num
#         val = min(Q, P)
#         if val not in arr:
#             arr.append(val)
#         else:
#             break
#         if P > Q:
#             P, Q = Q, P
#         K -= 1
#         idx += 1
#     print("#{} {}".format(test_case + 1, arr[K % idx - 1]))

# boj 5525
# n = int(input())
# m = int(input())
# s = input()
# idx, ans, pattern = 1, 0, 0
#
# while idx < m - 1:
#     if s[idx - 1] == 'I' and s[idx] == 'O' and s[idx + 1] == 'I':
#         pattern += 1
#         if pattern == n:
#             ans += 1
#             pattern -= 1
#         idx += 1
#     else:
#         pattern = 0
#     idx += 1
# print(ans)

# boj 10823
# s = ''
# while True:
#     try:
#         s += input()
#     except:
#         break
# arr = list(map(int, s.split(',')))
# print(sum(arr))

# boj 1302
# n = int(input())
# arr, books = [], dict()
# for _ in range(n):
#     data = input()
#     if data not in books:
#         books[data] = 1
#     else:
#         books[data] += 1
# for k, v in books.items():
#     arr.append([k, v])
# arr.sort(key = lambda x: (-x[1], x[0]))
# print(arr[0][0])

# boj 14430
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
# print(dp[n - 1][m - 1])

# boj 2028
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     num = (n * n) % pow(10, len(str(n)))
#     print("YES" if n == num else "NO")

# boj 11655
# s = list(input())
# alphal = "abcdefghijklmnopqrstuvwxyz"
# alphau = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ans = ''
#
# for i in s:
#     if i.isupper():
#         ans += alphau[(alphau.index(i) + 13) % 26]
#     elif i.islower():
#         ans += alphal[(alphal.index(i) + 13) % 26]
#     else:
#         ans += i
# print(ans)

# boj 15474
# n, a, b, c, d = map(int, input().split())
# x = n // a if n / a == n // a else n // a + 1
# y = n // c if n / c == n // c else n // c + 1
# print(min(x * b, y * d))

# boj 5054
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     print((arr[- 1] - arr[0]) * 2)

# boj 12756
# ap, al = map(int, input().split())
# bp, bl = map(int, input().split())
# while True:
#     al -= bp
#     bl -= ap
#     if al < 1 or bl < 1:
#         break
# if al < 1 and bl < 1:
#     print("DRAW")
# else:
#     print("PLAYER A" if al > bl else "PLAYER B")

# boj 14914
# b, a = map(int, input().split())
# x = min(b, a)
# for i in range(1, x + 1):
#     if b % i == a % i == 0:
#         print(i, b // i, a // i)

# boj 9063
# n = int(input())
# a, b = [], []
# for _ in range(n):
#     x, y = map(int, input().split())
#     a.append(x)
#     b.append(y)
# a.sort()
# b.sort()
# print((a[- 1] - a[0]) * (b[- 1] - b[0]))

# boj 1092
# import sys
# input = sys.stdin.readline
# n = int(input())
# crane = list(map(int, input().split()))
# m = int(input())
# box = list(map(int, input().split()))
# crane.sort(reverse = True)
# box.sort(reverse = True)
#
# if crane[0] < box[0]:
#     print(- 1)
#     sys.exit()
# else:
#     ans = 0
#     while True:
#         if not box:
#             break
#         for i in range(len(crane)):
#             for j in range(len(box)):
#                 if crane[i] >= box[j]:
#                     del box[j]
#                     break
#         ans += 1
# print(ans)

# boj 5212
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# for x in range(n):
#     for y in range(m):
#         if arr[x][y] == 'X':
#             temp = 0
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == '.':
#                     temp += 1
#             if temp >= 3:
#                 arr[x][y] = '0'
#
# while True:
#     if 'X' not in arr[0]:
#         arr.pop(0)
#     else:
#         break
# while True:
#     if 'X' not in arr[- 1]:
#         arr.pop(- 1)
#     else:
#         break
#
# chk = True
# while True:
#     for i in range(len(arr)):
#         if arr[i][0] == 'X':
#             chk = False
#             break
#     if chk:
#         for i in range(len(arr)):
#             arr[i].pop(0)
#     else:
#         break
#
# chk = True
# while True:
#     for i in range(len(arr)):
#         if arr[i][- 1] == 'X':
#             chk = False
#             break
#     if chk:
#         for i in range(len(arr)):
#             arr[i].pop(- 1)
#     else:
#         break
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == '0':
#             arr[i][j] = '.'
# for a in arr:
#     s = ''
#     for b in a:
#         s += b
#     print(s)

# boj 2303
# n = int(input())
# arr = []
# for i in range(1, n + 1):
#     data = list(map(int, input().split()))
#     temp = 0
#     for x in range(3):
#         for y in range(x + 1, 4):
#             for z in range(y + 1, 5):
#                 if temp < (data[x] + data[y] + data[z]) % 10:
#                     temp = (data[x] + data[y] + data[z]) % 10
#     arr.append([i, temp])
#
# arr.sort(key = lambda x : (- x[1], - x[0]))
# print(arr[0][0])

# boj 3059
# t = int(input())
# for _ in range(t):
#     alpha = [0] * 26
#     ans = sum(list(range(65, 91)))
#     s = input()
#     for i in s:
#         if not alpha[ord(i) - 65]:
#             alpha[ord(i) - 65] += 1
#             ans -= ord(i)
#     print(ans)

# boj 1940
# n = int(input())
# m = int(input())
# arr = sorted(list(map(int, input().split())))
# ans = 0
# l, r = 0, n - 1
# while l < r:
#     if arr[l] + arr[r] > m:
#         r -= 1
#     elif arr[l] + arr[r] < m:
#         l += 1
#     else:
#         l += 1
#         r -= 1
#         ans += 1
# print(ans)

# boj 5355
# t = int(input())
# for _ in range(t):
#     arr = list(input().split())
#     num = float(arr[0])
#     for i in arr[1:]:
#         if i == '@':
#             num *= 3
#         elif i == '%':
#             num += 5
#         else:
#             num -= 7
#     print(format(num, ".2f"))

# boj 2476
# n = int(input())
# ans = 0
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     if a == b == c:
#         money = 10000 + a * 1000
#     elif a == b != c:
#         money = 1000 + a * 100
#     elif b == c != a:
#         money = 1000 + b * 100
#     elif a == c != b:
#         money = 1000 + c * 100
#     else:
#         money = max(a, b, c) * 100
#     ans = max(money, ans)
# print(ans)

# boj 11557
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = [list(input().split()) for _ in range(n)]
#     for i in range(n):
#         arr[i][1] = int(arr[i][1])
#     arr.sort(key = lambda x : (- x[1]))
#     print(arr[0][0])

# boj 2477
# k = int(input())
# arr = [list(map(int, input().split())) for _ in range(6)]
# maxW = maxH = maxWidx = maxHidx = 0
# for i in range(6):
#     if arr[i][0] == 1 or arr[i][0] == 2:
#         if arr[i][1] > maxW:
#             maxW = arr[i][1]
#             maxWidx = i
#     else:
#         if arr[i][1] > maxH:
#             maxH = arr[i][1]
#             maxHidx = i
#
# minW = abs(arr[(maxWidx - 1) % 6][1] - arr[(maxWidx + 1) % 6][1])
# minH = abs(arr[(maxHidx - 1) % 6][1] - arr[(maxHidx + 1) % 6][1])
# ans = (maxW * maxH - minW * minH) * k
# print(ans)

# boj 15973
# px1, py1, px2, py2 = map(int, input().split())
# qx1, qy1, qx2, qy2 = map(int, input().split())
#
# x1 = px1 if px1 > qx1 else qx1
# x2 = px2 if px2 < qx2 else qx2
# y1 = py1 if py1 > qy1 else qy1
# y2 = py2 if py2 < qy2 else qy2
# x = x2 - x1
# y = y2 - y1
# if x > 0 and y > 0:
#     print("FACE")
# elif x > 0 and y == 0 or x == 0 and y > 0:
#     print("LINE")
# elif x < 0 or y < 0:
#     print("NULL")
# elif x == 0 and y == 0:
#     print("POINT")

# boj 1699
# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = list(range(n + 1))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j * j <= i:
#             dp[i] = min(dp[i], dp[i - j * j] + 1)
#         else:
#             break
# print(dp[n])

# boj 9613
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# t = int(input())
# for _ in range(t):
#     arr = list(map(int, input().split()))
#     ans = 0
#     for i in range(arr[0]):
#         for j in range(i + 1, arr[0]):
#             ans += gcd(arr[i + 1], arr[j + 1])
#     print(ans)

# boj 23795
# ans = 0
# while True:
#     n = int(input())
#     if n == - 1:
#         break
#     ans += n
# print(ans)

# boj 1018
# BW = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
# WB = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
#
# def chess(x, y, wcnt, bcnt):
#     for i in range(8):
#         for j in range(8):
#             if arr[x + i][y + j] != WB[i][j]:
#                 wcnt += 1
#             if arr[x + i][y + j] != BW[i][j]:
#                 bcnt += 1
#     return min(wcnt, bcnt)
#
# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]
# ans = float('inf')
# for i in range(n - 7):
#     for j in range(m - 7):
#         temp = chess(i, j, 0, 0)
#         if ans > temp:
#             ans = temp
# print(ans)

# boj 19572
# d1, d2, d3 = map(int, input().split())
# a = (d1 + d2 - d3) / 2
# b = (d1 - d2 + d3) / 2
# c = (- d1 + d2 + d3) / 2
# if min(a, b, c) <= 0:
#     print(- 1)
# else:
#     print(1)
#     print(a, b, c)

# boj 14490
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# a, b = map(int, input().split(':'))
# g = gcd(a, b)
# print("{}:{}".format(a // g, b // g))

# boj 2168
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# a, b = map(int, input().split())
# g = gcd(a, b)
# print(a + b - g)

# boj 23251
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     print(k * 23)

# boj 20205
# n, k = map(int, input().split())
# for i in range(n):
#     arr = list(map(int, input().split()))
#     ans = []
#     for j in arr:
#         ans += [j] * k
#     for _ in range(k):
#         print(*ans)

# boj 10474
# while True:
#     x, y = map(int, input().split())
#     if x == y == 0:
#         break
#     print("{} {} / {}".format(x // y, x % y, y))

# boj 1337
# n = int(input())
# arr = sorted([int(input()) for _ in range(n)])
# ans, cnt, idx = 0, 0, 0
# for i in range(n):
#     cnt += 1
#     while arr[i] - arr[idx] > 4:
#         idx += 1
#         cnt -= 1
#     ans = max(ans, cnt)
#
# if ans > 5:
#     ans = 5
# print(5 - ans)

# boj 10821
# arr = list(map(int, input().split(',')))
# print(len(arr))

# boj 1456
# import sys
# input = sys.stdin.readline
# A, B = map(int, input().split())
# C = int(B ** 0.5) + 1
# arr = [1] * C
# arr[1] = 0
# for i in range(2, C):
#     if i * i > C:
#         break
#     if not arr[i]:
#         continue
#     for j in range(i * i, C, i):
#         arr[j] = 0
#
# ans = 0
# for i in range(1, C):
#     if arr[i]:
#         j = i * i
#         while True:
#             if j < A:
#                 j *= i
#                 continue
#             if j > B:
#                 break
#             j *= i
#             ans += 1
# print(ans)

# boj 4504
# n = int(input())
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if num % n:
#         print("{} is NOT a multiple of {}.".format(num, n))
#     else:
#         print("{} is a multiple of {}.".format(num, n))

# boj 12605
# T = int(input())
# for test_case in range(T):
#     s = input().split()[:: - 1]
#     print("Case #{}:".format(test_case + 1), *s)

# boj 2596
# alpha = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
# n = int(input())
# s = input()
# words = []
# for i in range(0, n * 6, 6):
#     w = s[i : i + 6]
#     words.append(w)
#
# ans = ''
# for i in words:
#     chk = 0
#     for j in alpha:
#         cnt = 0
#         for k in range(6):
#             if i[k] == j[k]:
#                 cnt += 1
#         if cnt >= 5:
#             ans += chr(alpha.index(j) + 65)
#             break
#         else:
#             chk += 1
#     if chk == len(alpha):
#         print(words.index(i) + 1)
#         quit()
# print(ans)

# boj 16483
# T = int(input())
# print(round((0.5 * T) ** 2))

# boj 1284
# while True:
#     s = input()
#     if s == '0':
#         break
#     ans = len(s) + 1
#     for i in s:
#         if i == '0':
#             ans += 4
#         elif i == '1':
#             ans += 2
#         else:
#             ans += 3
#     print(ans)

# boj 1417
# n, p = map(int, input().split())
# num = n
# arr = [n]
# while True:
#     num = (num * n) % p
#     if num not in arr:
#         arr.append(num)
#     else:
#         break
#
# ans = 1
# for i in arr[:: - 1]:
#     if i == num:
#         break
#     else:
#         ans += 1
# print(ans)

# boj 3004
# n = int(input())
# print((n // 2 + 1) * (n // 2 + 2) if n % 2 else (n // 2 + 1) ** 2)

# boj 18187
# n = int(input())
# ans = 0
# idx = 1
# for j in range(n + 1):
#     ans += idx
#     if j % 3:
#         idx += 1
# print(ans)

# boj 18111
# import sys
# input = sys.stdin.readline
# n, m, b = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = float('inf')
# height = 0
# for i in range(257):
#     maxB, minB = 0, 0
#     for j in range(n):
#         for k in range(m):
#             if arr[j][k] < i:
#                 minB += (i - arr[j][k])
#             else:
#                 maxB += (arr[j][k] - i)
#     item = maxB + b
#     if item < minB:
#         continue
#     time = 2 * maxB + minB
#     if time <= ans:
#         ans = time
#         height = i
# print(ans, height)

# boj 1769
# n = input()
# if len(n) > 1:
#     cnt, num = 0, 0
#     while len(n) > 1:
#         cnt += 1
#         for i in n:
#             num += int(i)
#         if num < 10:
#             print(cnt)
#             if num % 3:
#                 print("NO")
#             else:
#                 print("YES")
#             break
#         n = str(num)
#         num = 0
# else:
#     print(0)
#     if int(n) % 3:
#         print("NO")
#     else:
#         print("YES")

# boj 10698
# T = int(input())
# for test_case in range(T):
#     s = input().split()
#     ans = "YES"
#     a, cal, b, c = int(s[0]), s[1], int(s[2]), int(s[4])
#     if cal == '+':
#         if a + b != c:
#             ans = "NO"
#     else:
#         if a - b != c:
#             ans = "NO"
#     print("Case {}: {}".format(test_case + 1, ans))

# boj 5618
# import sys
# input = sys.stdin.readline
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# n = int(input())
# num = list(map(int, input().split()))
# g = gcd(num[0], gcd(num[1], num[- 1]))
# for i in range(1, (g // 2) + 1):
#     if g % i == 0:
#         print(i)
# print(g)

# boj 21212
# n = int(input())
# ans = float('inf')
# for _ in range(n):
#     a, b = map(int, input().split())
#     ans = min(ans, b // a)
# print(ans)

# boj 17219
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# data = dict()
# for _ in range(n):
#     site, password = input().split()
#     data[site] = password
#
# for _ in range(m):
#     find = input().rstrip()
#     print(data[find])

# boj 2468
# from collections import deque
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
# def bfs(x, y, val):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = val
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if arr[nx][ny] <= val:
#                     continue
#                 if visited[nx][ny] == val:
#                     continue
#                 visited[nx][ny] = val
#                 q.append((nx, ny))
#     return 1
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[- 1] * n for _ in range(n)]
# minB, maxB = float('inf'), - float('inf')
# ans = 1
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] < minB:
#             minB = arr[i][j]
#         if arr[i][j] > maxB:
#             maxB = arr[i][j]
#
# for r in range(minB, maxB):
#     temp = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > r and visited[i][j] != r:
#                 temp += bfs(i, j, r)
#     ans = max(ans, temp)
# print(ans)

# boj 15652
# def solve(d, idx, n, m):
#     if d == m:
#         print(*arr)
#         return
#     for i in range(idx, n):
#         arr.append(i + 1)
#         solve(d + 1, i, n, m)
#         arr.pop()
#
# n, m = map(int, input().split())
# arr = []
# solve(0, 0, n, m)

# boj 11279
# import sys, heapq
# input = sys.stdin.readline
# n = int(input())
# q = []
# for _ in range(n):
#     x = int(input())
#     if x:
#         heapq.heappush(q, - x)
#     else:
#         if q:
#             print(abs(heapq.heappop(q)))
#         else:
#             print(0)

# boj 1252
# a, b = input().split()
# print(bin(int(a, 2) + int(b, 2))[2 :])

# boj 2153
# def prime(n):
#     for i in range(2, n):
#         if not n % i:
#             return False
#     return True
#
# s = input()
# ans = 0
# for i in s:
#     if i.isupper():
#         ans += ord(i) - 64
#     else:
#         ans += ord(i) - 96
# print('It is a prime word.' if prime(ans) else 'It is not a prime word.')

# boj 6502
# test_case = 1
# while True:
#     data = list(map(int, input().split()))
#     ans = 'does not fit on the table.'
#     if len(data) == 1:
#         break
#     r, w, l = data[0], data[1], data[2]
#     if (2 * r) ** 2 >= w ** 2 + l ** 2:
#         ans = 'fits on the table.'
#     print("Pizza {} {}".format(test_case, ans))
#     test_case += 1

# boj 10174
# t = int(input())
# for _ in range(t):
#     s = input().lower()
#     print("Yes" if s == s[:: - 1] else "No")

# boj 15128
# p1, q1, p2, q2 = map(int, input().split())
# area = p1 * p2 / (q1 * q2 * 2)
# print(1 if area == int(area) else 0)

# boj 11561
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     print(int((1 + (8 * int(input()) + 1) ** 0.5) / 2) - 1)

# boj 1371
# alpha = [0] * 26
# while True:
#     try:
#         s = input()
#         for i in s:
#             if i != ' ':
#                 alpha[ord(i) - 97] += 1
#     except:
#         break
# ans = ''
# cnt = max(alpha)
# for i in range(26):
#     if alpha[i] == cnt:
#         ans += chr(i + 97)
# print(ans)

# boj 7510
# T = int(input())
# for test_case in range(1, T + 1):
#     a, b, c = sorted(map(int, input().split()))
#     print("Scenario #{}:".format(test_case))
#     if a ** 2 + b ** 2 == c ** 2:
#         print("yes")
#     else:
#         print("no")
#     if test_case != T:
#         print()

# boj 18406
# n = input()
# lenN = len(n) // 2
# a, b = 0, 0
# for i in range(lenN):
#     a += int(n[i])
#     b += int(n[i + lenN])
# print("LUCKY" if a == b else "READY")

# boj 20053
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(min(arr), max(arr))

# boj 1517
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# def merge_sort(s, e):
#     global ans, arr
#
#     if s < e:
#         m = (s + e) // 2
#         merge_sort(s, m)
#         merge_sort(m + 1, e)
#
#         a, b = s, m + 1
#         temp = []
#
#         while a <= m and b <= e:
#             if arr[a] <= arr[b]:
#                 temp.append(arr[a])
#                 a += 1
#             else:
#                 temp.append(arr[b])
#                 b += 1
#                 ans += (m - a + 1)
#
#         if a <= m:
#             temp = temp + arr[a : m + 1]
#         if b <= e:
#             temp = temp + arr[b : e + 1]
#
#         for i in range(len(temp)):
#             arr[s + i] = temp[i]
#
# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# merge_sort(0, n - 1)
# print(ans)

# boj 10972
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int, input().split()))
# idx = - 1
# for i in range(n - 1, 0, - 1):
#     if arr[i - 1] < arr[i]:
#         idx = i - 1
#         break
#
# if idx == - 1:
#     print(- 1)
# else:
#     for i in range(n - 1, 0, - 1):
#         if arr[idx] < arr[i]:
#             arr[idx], arr[i] = arr[i], arr[idx]
#             arr = arr[: idx + 1] + sorted(arr[idx + 1 :])
#             print(*arr)
#             break

# boj 2573
# import sys
# from copy import deepcopy
# from collections import deque
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
#
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def findSea(x, y):
#     res = 0
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m and not temp[nx][ny]:
#             res += 1
#     return res
#
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = 1
#
# while True:
#     visited = [[0] * m for _ in range(n)]
#     temp = deepcopy(arr)
#     cnt, chk = 0, True
#
#     for i in range(1, n - 1):
#         if not chk:
#             break
#         for j in range(1, m - 1):
#             if arr[i][j]:
#                 chk = False
#                 break
#     if chk:
#         print(0)
#         break
#
#     for i in range(1, n - 1):
#         for j in range(1, m - 1):
#             if temp[i][j]:
#                 arr[i][j] = max(0, arr[i][j] - findSea(i, j))
#
#     for i in range(1, n - 1):
#         for j in range(1, m - 1):
#             if not visited[i][j] and arr[i][j]:
#                 bfs(i, j)
#                 visited[i][j] = 1
#                 cnt += 1
#
#     if cnt >= 2:
#         print(ans)
#         break
#
#     ans += 1

# boj 2979
# import sys
# input = sys.stdin.readline
# A, B, C = map(int, input().split())
# arr = [0] * 101
# ans = 0
# for _ in range(3):
#     a, b = map(int, input().split())
#     for i in range(a, b):
#         arr[i] += 1
# for i in range(101):
#     if arr[i] == 1:
#         ans += A
#     elif arr[i] == 2:
#         ans += 2 * B
#     elif arr[i] == 3:
#         ans += 3 * C
# print(ans)

# boj 16400
# import sys
# input = sys.stdin.readline
#
# def isPrime(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# n = int(input())
# dp, prime = [0] * (n + 1), []
# dp[0] = 1
#
# for i in range(2, n + 1):
#     if isPrime(i):
#         prime.append(i)
#
# for i in prime:
#     for j in range(i, n + 1):
#         dp[j] = (dp[j] + dp[j - i]) % 123456789
#
# print(dp[n])


# boj 6484
# def findPrimeFactors(n, k):
#     tPrimeFactorsMap = {}
#     tCompositeChecker = [True] * 2 + [False] * n
#     for p in range(n + 1):
#         if tCompositeChecker[p]:
#             continue
#         q, m = p, 1
#         tPrimeCnt = 0
#         tPrimePowers = [0] * (n + 1)
#
#         while True:
#             tPrimePowers[q] = tPrimePowers[m] + 1
#             if q <= k:
#                 tPrimeCnt -= tPrimePowers[q]
#             if q > n - k:
#                 tPrimeCnt += tPrimePowers[q]
#
#             q += p
#             m += 1
#             if q > n:
#                 break
#             tCompositeChecker[q] = True
#         tPrimeFactorsMap[p] = tPrimeCnt
#     return tPrimeFactorsMap
#
# T = int(input())
# for test_case in range(1):
#     N, K = map(int, input().split())
#     ans = 1
#     a = findPrimeFactors(N, K)
#     print(a)
#     print(len(a))
#     for val in a.values():
#         if val:
#             ans *= (val + 1)
#             ans %= 1000000007
#     print("#{} {}".format(test_case + 1, ans))

# boj 1676
# n=int(input())
# a,b=0,5
# while b<=n:
#     a+=n//b
#     b*=5
# print(a)

# swea 6484
# def x_y(x, y):
#     xy = 1
#     while y > 0:
#         if (y % 2) == 1:
#             xy *= x
#             y -= 1
#             xy %= m
#         x *= x
#         x %= m
#         y /= 2
#     return xy
#
# T = int(input())
# for test_case in range(T):
#     N, R = map(int, input().split())
#     ans1, ans2, m = 1, 1, 1234567891
#     for i in range(N - R + 1, N + 1):
#         ans1 *= i
#         ans1 %= m
#     for i in range(1, R + 1):
#         ans2 *= i
#         ans2 %= m
#
#     ans2 = x_y(ans2, m - 2)
#     ans2 %= m
#     ans1 *= ans2
#     ans1 %= m
#     arr = {}
#
#     num = ans1
#     k = 2
#     while num != 1:
#         if num % k == 0:
#             if k not in arr:
#                 arr[k] = 1
#             else:
#                 arr[k] += 1
#             num //= k
#         else:
#             k += 1
#     ans = 1
#     for i in arr.values():
#         ans *= (i + 1)
#     print("#{} {}".format(test_case + 1, ans))

# boj 15996
# n, a = map(int, input().split())
# ans = 0
# while n:
#     ans += n // a
#     n //= a
# print(ans)

# boj 1440
# s = input()
# i = 0
# while i < len(s):
#     print(s[i], end = '')
#     if s[i] in 'aeiou':
#         i += 2
#     i += 1

# boj 14891
# from collections import deque
#
# def left(idx, l, dir):
#     if l < 0:
#         return
#     if gear[idx][6] != gear[l][2]:
#         left(l, l - 1, - dir)
#         gear[l].rotate(- dir)
#
#
# def right(idx, r, dir):
#     if r > 3:
#         return
#     if gear[idx][2] != gear[r][6]:
#         right(r, r + 1, - dir)
#         gear[r].rotate(- dir)
#
#
# gear = [deque(input()) for _ in range(4)]
# ans = 0
# k = int(input())
#
# for _ in range(k):
#     n, d = map(int, input().split())
#     left(n - 1, n - 2, d)
#     right(n - 1, n, d)
#     gear[n - 1].rotate(d)
#
# for i in range(4):
#     if gear[i][0] == '1':
#         ans += 2 ** i
# print(ans)

# boj 13136
# r, c, n = map(int, input().split())
# s = r // n if r / n == int(r/ n) else (r // n) + 1
# g = c // n if c / n == int(c/ n) else (c // n) + 1
# print(s * g)

# boj 7891
# t = int(input())
# for _ in range(t):
#     print(sum(map(int, input().split())))

# boj 2004
# import sys
# input = sys.stdin.readline
#
# def fivecnt(n):
#     res = 0
#     while n:
#         n //= 5
#         res += n
#     return res
#
# def twocnt(n):
#     res = 0
#     while n:
#         n //= 2
#         res += n
#     return res
#
# n, m = map(int, input().split())
# if m == 0:
#     print(0)
# else:
#     twocnt = twocnt(n) - twocnt(m) - twocnt(n - m)
#     fivecnt = fivecnt(n) - fivecnt(m) - fivecnt(n - m)
#     print(min(twocnt, fivecnt))

# boj 1
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     even, odd = [], []
#     ans = 'yes'
#     for i in arr:
#         if i % 2:
#             odd.append(i)
#         else:
#             even.append(i)
#     if not even:
#         print("#{} {}".format(test_case + 1, 'no'))
#     else:
#         print("#{} {}".format(test_case + 1, 'yes'))

# boj 10816
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = list(map(int, input().split()))
# arr = {}
# for i in data:
#     if i not in arr:
#         arr[i] = 1
#     else:
#         arr[i] += 1
# m = int(input())
# data = list(map(int, input().split()))
# for i in data[:m - 1]:
#     if i not in arr:
#         print(0, end = ' ')
#     else:
#         print(arr[i], end = ' ')
# if data[- 1] not in arr:
#     print(0)
# else:
#     print(arr[data[- 1]])

# boj 9550
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     ans = 0
#     for i in arr:
#         ans += i // k
#     print(ans)

# boj 11098
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     price, ans = 0, ''
#     for _ in range(n):
#         p, name = input().split()
#         if price < int(p):
#             ans = name
#             price = int(p)
#     print(ans)

# boj 1019
# import sys
# input = sys.stdin.readline
#
# def solve(x, p):
#     while x:
#         ans[x % 10] += p
#         x //= 10
#
#
# n = int(input())
# ans = [0] * 10
# s, p = 1, 1
# while s <= n:
#     while n % 10 != 9:
#         solve(n, p)
#         n -= 1
#     if n < s:
#         break
#     while s % 10:
#         solve(s, p)
#         s += 1
#     s //= 10
#     n //= 10
#     for i in range(10):
#         ans[i] += (n - s + 1) * p
#     p *= 10
# print(*ans)

# boj 9950
# while True:
#     l, w, a = map(int, input().split())
#     if l == w == a == 0:
#         break
#     if l == 0:
#         print(a // w, w, a)
#     elif w == 0:
#         print(l, a // l, a)
#     else:
#         print(l, w, l * w)

# boj 7523
# def solve(num):
#     return num * (num + 1) // 2
#
#
# T = int(input())
# for t in range(T):
#     n, m = map(int, input().split())
#     print("Scenario #{}:".format(t + 1))
#     print(solve(m) - solve(n - 1))
#     print()

# boj 2153
# def isPrime(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# s = input()
# ans = 0
# for i in s:
#     if i.isupper():
#         ans += ord(i) - 38
#     else:
#         ans += ord(i) - 96
# print('It is a prime word.' if isPrime(ans) else 'It is not a prime word.')

# boj 2108
# import sys
# from collections import Counter
# input = sys.stdin.readline
# n = int(input())
# arr = sorted([int(input()) for _ in range(n)])
# print(round(sum(arr) / n))
# print(arr[n // 2])
# cnt = Counter(arr).most_common()
# print(cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0])
# print(arr[- 1] - arr[0])

# boj 1246
# n, m = map(int, input().split())
# arr = sorted([int(input()) for _ in range(m)])
# ans1, ans2 = 0, 0
# for i in range(m):
#     p = arr[i] * ((m - i) if m - i <= n else n)
#     if ans2 < p:
#         ans2 = p
#         ans1 = arr[i]
# print(ans1, ans2)

# boj 4740
# while True:
#     s = input()
#     if s == '***':
#         break
#     print(s[:: - 1])

# boj 13866
# a, b, c, d = map(int, input().split())
# print(abs((a + d) - (b + c)))

# boj 22193
# n, m = map(int, input().split())
# a = int(input())
# b = int(input())
# print(a * b)

# boj 11948
# arr1 = sorted([int(input()) for _ in range(4)])
# arr2 = sorted([int(input()) for _ in range(2)])
# print(sum(arr1[1:]) + arr2[1])

# boj 1198
# def area(a, b, c):
#     x = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
#     y = b[0] * a[1] + c[0] * b[1] + a[0] * c[1]
#     return abs(x - y) * 0.5
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             ans = max(ans, area(arr[i], arr[j], arr[k]))
# print(ans)

# boj 13752
# n = int(input())
# for _ in range(n):
#     print('=' * int(input()))

# boj 14175
# m, n, k = map(int, input().split())
# for _ in range(m):
#     s = input()
#     ans = ''
#     for i in s:
#         ans += i * k
#     for _ in range(k):
#         print(ans)

# boj 1356
# def solve(x, y):
#     n, m = 1, 1
#     for i in x:
#         n *= int(i)
#     for j in y:
#         m *= int(j)
#     if n == m:
#         return True
#     return False
#
#
# n = input()
# len = len(n)
# if len == 1:
#     print("NO")
# else:
#     for i in range(1, len):
#         a, b = n[:i], n[i:]
#         if solve(a, b):
#             print("YES")
#             break
#     else:
#         print("NO")

# swea1
# def permutation(arr, r):
#     global xx
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#     def generate(chosen, used):
#         global permuArr
#         if len(chosen) == r:
#             if chosen[0] != '0':
#                 permuArr.append(int(''.join(chosen)))
#             return
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#     generate([], used)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arrN = list(str(N))
#     permuArr = []
#     permutation(arrN, len(arrN))
#     ans = "impossible"
#     for i in permuArr:
#          if i > N:
#             if i % N == 0:
#                 ans = "possible"
#                 break
#     print("#{} {}".format(test_case + 1, ans))

# boj 14625
# sh, sm = map(int, input().split())
# eh, em = map(int, input().split())
# n = int(input())
# ans = 0
# while True:
#     if sh % 10 == n or sh // 10 == n or sm % 10 == n or sm // 10 == n:
#         ans += 1
#     if sh == eh and sm == em:
#         break
#     sm += 1
#     if sm == 60:
#         sm = 0
#         sh += 1
# print(ans)

# boj 1408
# sh, sm, ss = map(int, input().split(':'))
# eh, em, es = map(int, input().split(':'))
#
# es -= ss
# em -= sm
# eh -= sh
# if es < 0:
#     es = 60 + es
#     es = str(es)
#     if len(es) == 1:
#         es = '0' + es
#     em -= 1
# if em < 0:
#     em = 60 + em
#     em = str(em)
#     if len(em) == 1:
#         em = '0' + em
#     eh -= 1
# eh = str(eh)
# if len(eh) == 1:
#     eh = '0' + eh
# print("{}:{}:{}".format(eh, em, es))

# boj 21756
# n = int(input())
# arr = [i for i in range(1, n + 1)]
# temp = []
# while len(arr) != 1:
#     for i in range(len(arr)):
#         if i % 2:
#             temp.append(arr[i])
#     arr = temp
#     temp = []
# print(*arr)

# boj 25393
# N = int(input())
# lrArr = [list(map(int, input().split())) for _ in range(N)]
# Q = int(input())
# qArr = [list(map(int, input().split())) for _ in range(Q)]

# swea1
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = "Bob" if N % 2 else "Alice"
#     print("#{} {}".format(test_case + 1, ans))

# swea2
# 27 // 29
# '''
# 평면의 방정식
# Ax + By + Cz + D = 0
# p1 = (x1, y1, z1)
# p2 = (x2, y2, z2)
# p3 = (x3, y3, z3)
#
# A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
# B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
# C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
# D = x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1)
# '''
#
# def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
#     A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
#     B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
#     C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
#     D = x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1)
#     return A, B, C, D
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = "TAK"
#     if N > 3:
#         a, b, c, d = v(*arr[0], *arr[1], *arr[2])
#         for x, y, z in arr:
#             if a * x + b * y + c * z - d:
#                 ans = "NIE"
#                 break
#     print("#{} {}".format(test_case + 1, ans))

# boj 2583
# from collections import deque
# dx = [- 1, 1, 0, 0]
# dy = [0, 0, - 1, 1]
#
# def bfs(x, y):
#     area = 1
#     q = deque()
#     q.append([x, y])
#     while q:
#         x, y = q.pop()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < M and 0 <= ny < N and not arr[nx][ny]:
#                 area += 1
#                 arr[nx][ny] = 1
#                 q.append([nx, ny])
#     return area
#
# M, N, K = map(int, input().split())
# arr = [[0] * N for _ in range(M)]
# ans1, ans2 = 0, []
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     for y in range(y1, y2):
#         for x in range(x1, x2):
#             arr[y][x] = 1
#
# for i in range(M):
#     for j in range(N):
#         if not arr[i][j]:
#             arr[i][j] = 1
#             ans1 += 1
#             ans2.append(bfs(i, j))
# print(ans1)
# print(*sorted(ans2))

# boj 25304
# X = int(input())
# price = 0
# N = int(input())
# for _ in range(N):
#     a, b = map(int, input().split())
#     price += a * b
# print("Yes" if X == price else "No")

# boj 14606
# N = int(input())
# print(N * (N - 1) // 2)

# boj 16987
# def solve(idx, arr):
#     global ans
#
#     if idx == N:
#         res = 0
#         for i in range(N):
#             if arr[i] <= 0:
#                 res += 1
#         if ans < res:
#             ans = res
#         return
#
#     if arr[idx] > 0:
#         for i in range(N):
#             chk = 0
#             if arr[i] > 0 and i != idx:
#                 chk = 1
#                 temp = arr[:]
#                 temp[i] -= w[idx]
#                 temp[idx] -= w[i]
#                 solve(idx + 1, temp)
#         if not chk:
#             solve(idx + 1, arr)
#     else:
#         solve(idx + 1, arr)
#
#
# N = int(input())
# s, w, ans = [0] * N, [0] * N, 0
# for i in range(N):
#     s[i], w[i] = map(int,input().split())
#
# solve(0, s)
# print(ans)

# boj 16479
# K = int(input())
# D1, D2 = map(int, input().split())
# print(K ** 2 - ((D1 - D2) / 2) ** 2)

# boj 2548

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = sorted(list(map(int, input().split())))
# idx = 0
# number = float('inf')
# diff = float('inf')
# tempNum = - 1
# while idx < N:
#     num = arr[idx]
#     if tempNum == num:
#         idx += 1
#         continue
#     temp = 0
#     for i in arr:
#         temp += abs(num - i)
#         if temp > diff:
#             break
#     if diff >= temp:
#         if diff == temp:
#             if number > num:
#                 number = num
#                 diff = temp
#         else:
#             number = num
#             diff = temp
#     tempNum = num
#     idx += 1
# print(number)

# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = sorted(list(map(int, input().split())))
# l, r = divmod(N, 2)
# print(arr[l + r - 1])

# boj 1269
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(len(a - b) + len(b - a))

# boj 10971

# def dfs(n, cost, cnt):
#     global ans
#     if cnt == N:
#         if arr[n][sn]:
#             if ans > cost + arr[n][sn]:
#                 ans = cost + arr[n][sn]
#     for i in range(N):
#         if not chk[i] and arr[n][i]:
#             chk[i] = 1
#             dfs(i, cost + arr[n][i], cnt + 1)
#             chk[i] = 0
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# chk = [0] * N
# ans = float('inf')
# for i in range(N):
#     sn = i
#     chk[i] = 1
#     dfs(i, 0, 1)
#     chk[i] = 0
# print(ans)

# def dfs(n, cost, cnt):
#     global ans
#     if cnt == N:
#         if arr[n][sn]:
#             if ans > cost + arr[n][sn]:
#                 ans = cost + arr[n][sn]
#     for i in range(N):
#         if not chk[i] and arr[n][i]:
#             chk[i] = 1
#             if ans < cost + arr[n][i]:
#                 chk[i] = 0
#                 continue
#             else:
#                 dfs(i, cost + arr[n][i], cnt + 1)
#                 chk[i] = 0
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# chk = [0] * N
# ans = float('inf')
# for i in range(N):
#     sn = i
#     chk[i] = 1
#     dfs(i, 0, 1)
#     chk[i] = 0
# print(ans)

# boj 2023
# def solve(num, k):
#     if k == N:
#         print(num)
#         return
#
#     for i in la:
#         chk = 1
#         num *= 10
#         num += i
#         for j in range(2, int(num ** 0.5) + 1):
#             if num % j == 0:
#                 chk = 0
#                 break
#         if chk:
#             solve(num, k + 1)
#         num -= i
#         num //= 10
#     return
#
# N = int(input())
# n1 = [2, 3, 5, 7]
# la = [1, 3, 5, 7, 9]
# for i in n1:
#     solve(i, 1)

# boj 10163
# PyPy3
# import sys
# input = sys.stdin.readline
# arr = [[0] * 1001 for _ in range(1001)]
# N = int(input())
# for i in range(1, N + 1):
#     sx, sy, w, h = map(int, input().split())
#     for x in range(sx, sx + w):
#         for y in range(sy, sy + h):
#             arr[x][y] = i
#
# ans = [0] * (N + 1)
# for i in arr:
#     for j in i:
#         if j:
#             ans[j] += 1
#
# for i in ans[1:]:
#     print(i)

# swea 1
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# T = int(input())
# for test_case in range(T):
#     s = input()
#     ans = 0
#     for i in range(len(s)):
#         if alpha[i] == s[i]:
#             ans += 1
#         else:
#             break
#     print("#{} {}".format(test_case + 1, ans))

# boj 2567
# arr = [[0] * 101 for _ in range(101)]
# arr = [[0] * 26 for _ in range(26)]
# N = int(input())
# for _ in range(N):
#     sx, sy = map(int, input().split())
#     for x in range(sx, sx + 10):
#         if arr[25 - sy][x] == 0:
#             arr[25 - sy][x] = 1
#         if arr[15 - sy][x] == 0:
#             arr[15 - sy][x] = 1
#     for y in range(sy, sy + 10):
#         if arr[25 - y][sx] == 0:
#             arr[25 - y][sx] = 1
#         if arr[25 - y][sx + 9] == 0:
#             arr[25 - y][sx + 9] = 1
#     for i in arr:
#         print(*i)
#     print()

# boj 10989
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = [0] * 10001
# for i in range(N):
#     arr[int(input())] += 1
#
# for i in range(10001):
#     print('%s\n' % i * arr[i], end = '')

# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = {}
# for i in range(N):
#     num = int(input())
#     if num not in arr:
#         arr[num] = 1
#     else:
#         arr[num] += 1
#
# for i in sorted(arr.items()):
#     for _ in range(i[1]):
#         print(i[0])

# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = [0] * 10001
# for _ in range(N):
#     arr[int(input())] += 1
#
# for i in range(10001):
#     for _ in range(arr[i]):
#         sys.stdout.write(str(i) + '\n')

# boj 2072
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def bfs(x, y, d, val):
#     dir = [d, [- i for i in d]]
#     q = deque()
#     q.append([x, y])
#     cnt = 1
#     while q:
#         x, y = q.popleft()
#         for dx, dy in dir:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < 20 and 0 <= ny < 20 and not visited[nx][ny] and arr[nx][ny] == val:
#                 visited[nx][ny] = 1
#                 cnt += 1
#                 q.append([nx, ny])
#     return cnt
#
# N = int(input())
# arr = [[0] * 20 for _ in range(20)]
# for i in range(1, N + 1):
#     x, y = map(int, input().split())
#     color = 1 if i % 2 else 2
#     arr[x][y] = color
#     visited = [[0] * 20 for _ in range(20)]
#     visited[x][y] = 1
#
#     for k in [[- 1, - 1], [- 1, 0], [- 1, 1], [0, 1]]:
#         if bfs(x, y, k, color) == 5:
#             print(i)
#             exit()
# else:
#     print(- 1)

# boj 2721
# T, W, A = [0] * 302, [0] * 302, [0] * 302
# for i in range(1, 302):
#     A[i] = i
#     T[i] = T[i - 1] + A[i]
# for i in range(1, 301):
#     for j in range(1, i + 1):
#         W[i] += j * T[j + 1]
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(W[N])

# boj 14467
# N = int(input())
# arr = [[- 1] * 10, [0] * 10]
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     if arr[0][a - 1] == - 1:
#         arr[0][a - 1] = b
#     if arr[0][a - 1] != b:
#         arr[0][a - 1] = b
#         arr[1][a - 1] += 1
# print(sum(arr[1]))

# boj 25965
# N = int(input())
# for _ in range(N):
#     M = int(input())
#     ans, K, D, A = 0, 0, 0, 0
#     arr = [list(map(int, input().split())) for _ in range(M)]
#     k, d, a = map(int, input().split())
#     for i in arr:
#         temp = i[0] * k - i[1] * d + i[2] * a
#         if temp > 0:
#             ans += temp
#     print(ans)

# boj 11034
# while True:
#     try:
#         A, B, C = map(int, input().split())
#         ans = 0
#         while True:
#             AB = B - A
#             BC = C - B
#             if AB == 1 and BC == 1:
#                 break
#             if AB > BC:
#                 C = B
#                 B -= 1
#             else:
#                 A = B
#                 B += 1
#             ans += 1
#         print(ans)
#     except:
#         exit()

# boj 17615
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# S = input()
# arr = []
# temp, cnt = '', 1
# for i in S:
#     if len(temp) == 0:
#         temp = i
#     else:
#         if temp == i:
#             cnt += 1
#         else:
#             arr.append(temp * cnt)
#             temp = i
#             cnt = 1
# arr.append(temp * cnt)
# print(arr)

# boj 1268
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = [0] * N
# for i in range(N):
#     visited = [0] * N
#     for j in range(5):
#         for idx in range(N):
#             if idx != i and arr[idx][j] == arr[i][j]:
#                 visited[idx] = 1
#     ans[i] = len(list(filter(lambda x: x, visited)))
#
# print(ans.index(max(ans)) + 1)

# import time
#
# def binary_search(array, elem):
#     low = 0
#     high = len(array) - 1
#     temp = 0
#
#     while low < high and not temp:
#         mid = (low + high) // 2
#         if array[mid] == elem:
#             temp = 1
#         else:
#             if elem < arr[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#     return temp
#
# arr = [i for i in range(55000000)]
# start = time.time()
# arrr = sorted(arr)
# print(time.time() - start)
#
# start = time.time()
# arrr = binary_search(arr, 0)
# print(time.time() - start)

# arr = [1, 2, 3, 4, 5, 6, 6]
# dic = {}
# for i in range(7):
#     if arr[i] not in dic:
#         dic[arr[i]] = [i]
#     else:
#         dic[arr[i]].append(i)
# print(dic)



# 경우 1) arr[i] > arr[j]:
# - arr[i]가 arr[j + 1]도 볼 수 있다.

# 경우 2) arr[i] < arr[j]:
# - arr[i]가 arr[j + 1]을 볼 수 없다.

# 경우 3) arr[i] == arr[j]:
# - arr[i] > arr[j + 1]인 경우
# - arr[i] < arr[j + 1]인 경우

# boj 16803
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#     visited = [[0] * N for _ in range(N)]
#     idx, jdx = 0, 1
#     chk1 = 0    # 1 > 2
#     chk2 = 0    # 1 = 2
#     chk3 = 0    # 1 < 2
#
#     while idx < N - 1:
#         if arr[idx] > arr[jdx]:
#             chk1 = 1
#             jdx += 1
#
#         elif arr[idx] == arr[jdx]:
#             chk2 = 1
#             jdx += 1
#
#         else:
#             chk3 = 1
#             jdx += 1

# boj 6588
# import sys
# input = sys.stdin.readline
# num = 5000001
# arr = [1] * num
# for i in range(2, int((num - 1) ** 0.5) + 1):
#     if arr[i]:
#         for k in range(i + i, num, i):
#             arr[k] = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     chk = 0
#     for i in range(3, len(arr) + 1):
#         if arr[i] and arr[n - i]:
#             print("{} = {} + {}".format(n, i, n - i))
#             chk = 1
#             break
#     if chk == 0:
#         print("Goldbach's conjecture is wrong.")

# boj 11444
# import sys
# input = sys.stdin.readline
# mod = 1000000007
# def power(adj, n):
#     if n == 1:
#         return adj
#     elif n % 2:
#         return multi(power(adj, n - 1), adj)
#     else:
#         return power(multi(adj, adj), n // 2)
#
#
# def multi(a, b):
#     temp = [[0] * len(b[0]) for _ in range(2)]
#     for i in range(2):
#         for j in range(len(b[0])):
#             total = 0
#             for k in range(2):
#                 total += a[i][k] * b[k][j]
#             temp[i][j] = total % mod
#     return temp
#
# n = int(input())
# adj = [[1, 1], [1, 0]]
# start = [[1], [1]]
# if n < 3:
#     print(1)
# else:
#     print(multi(power(adj, n - 2), start)[0][0])

# import math
#
# k, m = 6, 5
# if k - 619 <= 0:
#     n = 1
# else:
#     n = k - 619
#
# n = 6
# while n <= k + 619:
#         if n == 1:
#             fnm = n + m
#         else: # odd num
#             fnm, cnt = n + 1, 0
#             while cnt != m:
#                 if math.gcd(fnm, n) == 1:
#                     cnt += 1
#                     if cnt == m:
#                         break
#                 fnm += 1
#         if fnm - n == k ^ n:
#             break
#         n += 1
# else:
#     n = - 1
# def factorization(n):
#     res = set()
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             res.add(d)
#             n /= d
#         else:
#             d += 1
#     return sorted(res)
#
# print(factorization(2354346547676))

# swea1
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     ans = 2 * N + 1
#     for i in range(1, N + 1):
#         ans += (2 * int((N ** 2 - i ** 2) ** 0.5) + 1) * 2
#     print("#{} {}".format(test_case + 1, ans))

# swea2
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))

# swea1

# for t in range(int(input())):
#     S,T=input().split()
#     a="yes"if S*len(T)==T*len(S) else "no"
#     print(f'#{t+1} {a}')

# boj 21598
# for _ in range(int(input())):
#     print("SciComLove")

# boj 2738
# N, M = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# B = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         A[i][j] += B[i][j]
# for i in A:
#     print(*i)

# boj 18870
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# X = list(sorted(set(arr)))
# dic = {X[i]: i for i in range(len(X))}
#
# for i in arr:
#     print(dic[i], end = " ")

# swea 1
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     s = input()
#     if N % 2:
#         ans = "No"
#     else:
#         ans = "Yes" if s[:N // 2] == s[N // 2:] else "No"
#     print("#{} {}".format(test_case + 1, ans))

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     s = input()
#     print("#{} {}".format(test_case + 1, "Yes" if N % 2 == 0 and s[:N // 2] == s[N // 2:] else "No"))


# swea 2
# '''
# 파스칼의 삼각형과 이항계수의 성질
# x, y가 가능한 경우
# 1. (x + y) // 3 == 0인 경우
# 만약 x가 y보다 크다면 x == 2y
# '''
# T = int(input())
# mod = 1000000007
# for test_case in range(T):
#     X, Y = map(int, input().split())
#     if X < Y:
#         X, Y = Y, X
#
#     if (X + Y) % 3:
#         ans = 0
#     else:
#         if X > Y and X // Y != 2:
#             ans = 0
#         else:
#             pass

# swea 17900
# T = int(input())
# for test_case in range(T):
#     n = input().split()
#     cnt = [[0] * 5 for _ in range(5)]
#     for i in range(119):
#         cnt[0][ord(n[i][0]) - 49] += 1
#         cnt[1][ord(n[i][1]) - 49] += 1
#         cnt[2][ord(n[i][2]) - 49] += 1
#         cnt[3][ord(n[i][3]) - 49] += 1
#         cnt[4][ord(n[i][4]) - 49] += 1
#     ans = ''
#     for i in range(5):
#         for j in range(5):
#             if cnt[i][j] == 23:
#                 ans += str(j + 1)
#     print(ans)

# swea 11092
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     minIdx, maxIdx = 0, 0
#     for i in range(N):
#         if arr[i] >= arr[maxIdx]:
#             maxIdx = i
#         if arr[i] < arr[minIdx]:
#             minIdx = i
#     print("#{} {}".format(test_case + 1, abs(minIdx - maxIdx)))

# swea 13389
# T = int(input())
# for test_case in range(1):
#     S, N = input().split()
#     N = int(N)
#     alpha, password = '', 0
#
#     for i in range(len(S) - 1):
#         alpha += S[i]
#         if S[i] == S[i + 1]:
#             alpha += 'a'
#     alpha += S[- 1]
#
#     for i in range(len(alpha)):
#         password += (ord(alpha[:: - 1][i]) - 96) * 26 ** i
#     print(password)


# swea 17937
# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     print("#{} {}".format(test_case + 1, A if A == B else 1))

# swea 17938
# T = int(input())
# for test_case in range(T):
#     X, Y, Z = map(int, input().split())
#     if X == Y == Z:
#         ans1 = ans2 = ans3 = '1' * X
#     else:
#         # ans1, ans2, ans3 = [], [], []
#         ans1 = '1' * max(X, Z)
#         ans2 = '1' * max(X, Y)
#         ans3 = '1' * max(Y, Z)
#         print(ans1, ans2, ans3)

# swea 17940
T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    ans = 0
    if N != B:
        if N - B < A:
            ans = - 1
        else:
            
    print(ans)