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