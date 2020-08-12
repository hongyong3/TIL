import sys
sys.stdin = open("D4_3501_input.txt", "r")

# 소수점이 전체 표시가 안됨.

# T = int(input())
# for test_case in range(T):
#    p, q = map(int, input().split())
#    ans = '0.'
#    if p / q == p // q:
#        print("#{} {}".format(test_case + 1, p // q))
#    else:
#        if len(str(float(p) / float(q))) <= 4:
#            print("#{} {}".format(test_case + 1, p / q))
#        else:
#            circulating = str("%.50f" % (p / q))[2:]
#            for i in range(len(circulating)):
#                j = i + 1
#                while j < len(circulating):
#                    if circulating[i : j] == circulating[j : 2 * j]:
#                        ans += '(' + circulating[i : j] + ')'
#                        break
#                    else:
#                        j += 1
#                break
#            print("#{} {}".format(test_case + 1, ans))

# runtime error

# from decimal import *
# getcontext().prec = 100
#
# def checkCir(x, y):
#     global a, b, y2, idx
#     if x % y == 0:
#         return True
#     y2 = y
#
#     while y2 % 2 == 0:
#         y2 /= 2
#         a += 1
#
#     while y2 % 5 == 0:
#         y2 /= 5
#         b += 1
#     idx = max(a, b)
#
#     if y2 == 1:
#         return True
#     else:
#         return False
#
# def getCir():
#     n = 1
#     target = 9
#     while (target % y2) != 0:
#         n += 1
#         target = target * 10 + 9
#     return n
#
# T = int(input())
# for test_case in range(T):
#     x, y = map(int, input().split())
#     a, b, y2, idx = 0, 0, 0, 0
#     if checkCir(x, y):
#         pass
#         if x // y == x / y:
#             print("#{} {}".format(test_case + 1, x // y))
#             continue
#         else:
#             print("#{} {}".format(test_case + 1, x / y))
#             continue
#     else:
#         l = getCir() + idx
#         a = str(Decimal(x) / Decimal(y))
#         ans = a[:2 + idx] + "(" + a[2 + idx: 2 + l] + ")"
#         print("#{} {}".format(test_case + 1, ans))

# runtime error

# def checkCir(p, q):
#     global a, b, q2, idx
#     if p % q == 0:
#         return True
#     q2 = q
#
#     while q2 % 2 == 0:
#         q2 /= 2
#         a += 1
#
#     while q2 % 5 == 0:
#         q2 /= 5
#         b += 1
#     idx = max(a, b)
#
#     if q2 == 1:
#         return True
#     else:
#         return False
#
# def getCir():
#     n = 1
#     target = 9
#     while (target % q2) != 0:
#         n += 1
#         target = target * 10 + 9
#     return n
#
# T = int(input())
# for test_case in range(T):
#     p, q = map(int, input().split())
#     a, b, q2, idx = 0, 0, 0, 0
#     if checkCir(p, q):
#         if p // q == p / q:
#             print("#{} {}".format(test_case + 1, p // q))
#         else:
#             print("#{} {}".format(test_case + 1, p / q))
#     else:
#         l = getCir()
#         print("#{} {}.".format(test_case + 1, p // q), end = '')
#         for i in range(idx):
#             p = (p % q) * 10
#             print(p // q, end = '')
#         print("(", end = '')
#         for i in range(l):
#             p = (p % q) * 10
#             print(p // q, end = '')
#         print(")")

# runtime error 38 / 50
# T = int(input())
# for test_case in range(T):
#     p, q = map(int, input().split())
#     ans = ''
#     isCirculation, cirList = False, [0] * q # 순환소수 유무, 순환 길이 list
#     idx = 0 # 순환 부분 길이
#
#     while p:
#         if not idx:
#             ans += str(p // q)
#             if p % q:
#                 ans += '.'
#         else:
#             ans += str(p // q)
#
#         idx += 1
#         p %= q
#
#         if cirList[p]:
#             isCirculation = True
#             start = cirList[p] + 1
#             break
#
#         cirList[p] = idx
#         p *= 10
#
#     if isCirculation:
#         ans = ans[:start] + '(' + ans[start: ] + ')'
#     print("#{} {}".format(test_case + 1, ans))

# runtime error 43 / 50
# T = int(input())
# for test_case in range(T):
#     p, q = map(int, input().split())
#     w, isCycle, start = 0, False, 0
#     rest = [0] * q
#     ans = ''
#     while p:
#         if not w:
#             firstNum = p // q
#             if p % q:
#                 w += 1
#                 ans += '.'
#         else:
#             w += 1
#             ans += str(p // q)
#         p %= q
#         if rest[p]:
#             isCycle = True
#             start = rest[p]
#         if isCycle:
#             break
#         else:
#             rest[p] = w
#         p *= 10
#
#     print("#{} {}".format(test_case + 1, firstNum), end = '')
#     if isCycle:
#         for i in range(w):
#             if i == start:
#                 print('(', end = '')
#                 print(ans[start : w], end = '')
#                 print(')')
#                 break
#             else:
#                 print(ans[i], end = '')
#     else:
#         print(ans)

# runtime error 38 / 50
# T = int(input())
# for test_case in range(T):
#     p, q = map(int, input().split())
#     w, isCycle, start = 0, False, 0 # isCycle : 순환소수 유무, start : 순환소수 시작점
#
#     rest = [0] * q
#     ans = str(p // q)
#
#     while p:
#         if not w:
#             if p % q:
#                 ans += '.'
#         else:
#             ans += str(p // q)
#
#         w += 1
#         p %= q
#
#         if rest[p]:
#             isCycle = True
#             start = rest[p]
#             break
#         else:
#             rest[p] = w
#         p *= 10
#
#     if isCycle:
#         ans = ans[:start + 1] + '(' + ans[start + 1:] + ')'
#     print("#{} {}".format(test_case + 1, ans))

def cycleLength():
    global a, b, idx, q2
    n1, n2 = 1, 9
    idx = a if a > b else b
    while n2 % q2:
        n1 += 1
        n2 = n2 * 10 + 9
    return n1


def cycle():
    global a, b, q2
    if not p % q:
        return True

    while (q2 % 2 == 0) or (q2 % 5 == 0):
        if q2 % 2 == 0:
            q2, a = q2 / 2, a + 1
        if q2 % 5 == 0:
            q2, b = q2 / 5, b + 1

    if q2 == 1:
        return True
    else:
        return False


def gcd(x, y):
    while y:
        c = x % y
        x, y = y, c
    return x


T = int(input())
for test_case in range(T):
    p, q = map(int, input().split())
    divider = gcd(p, q)
    p, q = p // divider, q // divider
    ans = ''
    a, b, idx, q2 = 0, 0, 0, q
    if cycle():
        ans += str(p // q)
        p = (p % q) * 10
        if p:
            ans += '.'
        while p:
            ans += str(p // q)
            p = (p % q) * 10
    else:
        l = cycleLength()
        ans += str(p // q) + '.'

        for i in range(idx):
            ans += str(p // q)
            p = (p % q) * 10
        ans += '('

        for i in range(l):
            p = (p % q) * 10
            ans += str(p // q)
        ans += ')'
    print("#{} {}".format(test_case + 1, ans))