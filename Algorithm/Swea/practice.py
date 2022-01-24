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
s = input()
h, s = s.count(":-)"), s.count(":-(")
if h > s:
    print("happy")
elif h < s:
    print("sad")
elif h == s == 0:
    print("none")
else:
    print("none")