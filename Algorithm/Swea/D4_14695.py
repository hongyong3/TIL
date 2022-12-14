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

# def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
#     A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
#     B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
#     C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
#     D = - (x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1))
#     return A, B, C, D
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = "TAK"
#
#     if N > 3:
#         chk1 = 1
#         a, b, c, d = v(*arr[0], *arr[1], *arr[2])
#         for x, y, z in arr:
#             n = a * x + b * y + c * z + d
#             if n:
#                 ans = "NIE"
#                 chk1 = 0
#                 break

        # if chk1:
        #     chk2, idx = 0, 0
        #     for i in range(N - 1):
        #         if chk2:
        #             break
        #         xchk, ychk, zchk = 0, 0, 0
        #         x1, y1, z1 = arr[i]
        #         xp, yp, zp = 0, 0, 0
        #         for j in range(i + 1, N):
        #             x2, y2, z2 = a52rr[j]
        #             if x1 == x2:
        #                 xp += 1
        #                 if xp == 2:
        #                     xchk, chk2, idx = 1, 1, i
        #                     break
        #             if y1 == y2:
        #                 yp += 1
        #                 if yp == 2:
        #                     ychk, chk2, idx = 1, 1, i
        #                     break
        #             if z1 == z2:
        #                 zp += 1
        #                 if zp == 2:
        #                     zchk, chk2, idx = 1, 1, i
        #                     break
        #
        #     if chk2:
        #         if xchk:
        #             for i in arr:
        #                 if i[0] != x1:
        #                     ans = "NIE"
        #                     break
        #         elif ychk:
        #             for i in arr:
        #                 if i[1] != y1:
        #                     ans = "NIE"
        #                     break
        #         elif zchk:
        #             for i in arr:
        #                 if i[2] != z1:
        #                     ans = "NIE"
        #                     break
    # print("#{} {}".format(test_case + 1, ans))

# 27 / 29
def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
    B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
    C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    D = x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1)
    return A, B, C, D


T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = "TAK"
    if N > 3:
        idx = 2
        while idx < N:
            A, B, C, D = v(*arr[0], *arr[1], *arr[idx])
            if A == B == C == D == 0:
                idx += 1
            else:
                break
        for x, y, z in arr[idx:]:
            if A * x + B * y + C * z - D:
                ans = "NIE"
                break

    print("#{} {}".format(test_case + 1, ans))