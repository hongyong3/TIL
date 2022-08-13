import sys
sys.stdin = open("D4_14695_input.txt", "r")

'''
평면의 방정식
Ax + By + Cz + D = 0
p1 = (x1, y1, z1)
p2 = (x2, y2, z2)
p3 = (x3, y3, z3)

A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
D = x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1)
'''

# 27 // 29
# def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
#     A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
#     B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
#     C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
#     D = - (x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1))
#     return A, B, C, D
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = "TAK"
#     xp, yp, zp = [0] * N, [0] * N, [0] * N
#     if N > 3:
#         a, b, c, d = v(*arr[0], *arr[1], *arr[2])
#         for x, y, z in arr:
#             n = a * x + b * y + c * z + d
#             if n:
#                 ans = "NIE"
#                 break
#         for i in range(N - 1):
#             x, y, z = arr[i]
#             for j in range(i + 1, N):
#                 if x == arr[i][0]:
#                     xp[i] += 1
#                 if y == arr[i][1]:
#                     yp[i] += 1
#                 if z == arr[i][2]:
#                     zp[i] += 1
#     print(xp)
#     print(yp)
#     print(zp)
#     # print("#{} {}".format(test_case + 1, ans))

def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
    B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
    C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    D = - (x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1))
    return A, B, C, D

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = "TAK"
    xchk, ychk, zchk = [0, 0], [0, 0], [0, 0]
    if N > 3:
        a, b, c, d = v(*arr[0], *arr[1], *arr[2])
        for x, y, z in arr:
            n = a * x + b * y + c * z + d
            if n:
                ans = "NIE"
                break

        chk = 0
        for i in range(N - 1):
            if chk:
                break
            x, y, z = arr[i]
            xchk, ychk, zchk = 0, 0, 0
            xp, yp, zp = 0, 0, 0
            for j in range(i + 1, N):
                if x == arr[j][0]:
                    xp += 1
                    if xp == 2:
                        xchk[0], xchk[1] = 1, x
                        chk = 1
                        break
                if y == arr[j][1]:
                    yp += 1
                    if yp == 2:
                        ychk[0], ychk[1] = 1, y
                if z == arr[j][2]:
                    zp += 1
                    if zp == 2:
                        zchk[0], zchk[1] = 1, z

        if xchk:
            for i in range(N):
                if i != xchk[1] and xp[i] != 0:
                    ans = "NIE"
                    break
        if ychk:
            for i in range(N):
                if i != ychk[1] and yp[i] != 0:
                    ans = "NIE"
                    break
        if zchk:
            for i in range(N):
                if i != zchk[1] and zp[i] != 0:
                    ans = "NIE"
                    break
    print("#{} {}".format(test_case + 1, ans))