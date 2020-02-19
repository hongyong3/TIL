import sys
sys.stdin = open("D4_5676_input.txt", "r")

# def intersection(x3, y3, x4, y4):
#     global meet, ans
#     p = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
#     tm = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
#     sm = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
#
#     if tm == sm == p == 0:
#         meet = 4
#         return
#
#     if p:
#         if 0 < tm / p < 1 and 0 < sm / p < 1:
#                 t, s = tm / p, sm / p
#                 x = x1 + t * (x2 - x1)
#                 y = y1 + t * (y2 - y1)
#                 if [x, y] not in ans:
#                     ans.append([x, y])
#
# T = int(input().replace('혻', ''))
# for test_case in range(T):
#     xmin, ymin, xmax, ymax = map(int, input().replace('혻', '').split())
#     x1, y1, x2, y2 = map(int, input().replace('혻', '').split())
#
#     meet = 0
#     ans = []
#     rectangleLine = [[xmin, ymin, xmax, ymin], [xmin, ymin, xmin, ymax], [xmin, ymax, xmax, ymax], [xmax, ymin, xmax, ymax]]
#
#     for i in rectangleLine:
#         intersection(i[0], i[1], i[2], i[3])
#     print("#{} {}".format(test_case + 1, meet))

# def intersection(x3, y3, x4, y4):
#     global meet, ans
#     E = ((y2 - y1) * x1) + ((x1 - x2) * y1)
#     F = ((y4 - y3) * x3) + ((x3 - x4) * y3)
#     # T = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
#     # S = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
#     P = ((y2 - y1) * (x3 - x4)) - ((x1 - x2) * (y4 - y3))
#
#     if not P:
#         # if T == S == P == 0:
#         #     meet = 4
#         return
#     else:
#         X = ((E * (x3 - x4)) - (F * (x1 - x2))) / P
#         Y = ((F * (y2 - y1)) - (E * (y4 - y3))) / P
#         if x1 <= X <= x2 and x3 <= X <= x4 and y1 <= Y <= y2 and y3 <= Y <= y4 and [X, Y] not in ans:
#             ans.append([X, Y])
#
# T = int(input().replace('혻', ''))
# for test_case in range(T):
#     xmin, ymin, xmax, ymax = map(int, input().replace('혻', '').split())
#     x1, y1, x2, y2 = map(int, input().replace('혻', '').split())
#
#     meet = 0
#     ans = []
#     if xmin > xmax:
#         xmin, ymin, xmax, ymax = xmax, ymax, xmin, ymin
#
#     if x1 > x2:
#         x1, y1, x2, y2 = x2, y2, x1, y1
#
#     rectangleLine = [[xmin, ymin, xmax, ymin], [xmin, ymin, xmin, ymax], [xmin, ymax, xmax, ymax], [xmax, ymin, xmax, ymax]]
#
#     if y1 == y2:
#         if ymin < y1 < ymax:
#             if x1 <= xmin < x2 < xmax or xmin < x1 < xmax <= x2:
#                 meet = 1
#             elif xmin <= x1 < x2 <= xmax or x1 <= xmin < xmax <= x2:
#                 meet = 2
#         elif ymin == y1 or ymax == y1:
#             if xmin == x2 or xmax == x1:
#                 meet = 1
#             elif xmin <= x1 <= xmax or xmin <= x2 <= xmax:
#                 meet = 4
#
#     elif x1 == x2:
#         if xmin < x1 < xmax:
#             if ymin <= y1 or ymax <= y1 or y2 <= ymax or y2 <= ymin:
#                 meet = 1
#             elif ymin <= y1 < y2 <= ymax or y1 <= ymin < ymax <= y2:
#                 meet = 2
#         elif xmin == x1 or xmax == x2:
#             if ymin == y2 or ymax == y1:
#                 meet = 1
#             elif ymin <= y1 <= ymax or ymin <= y2 <= ymax:
#                 meet = 4
#     else:
#         for i in rectangleLine:
#             intersection(i[0], i[1], i[2], i[3])
#     if meet != 4:
#         meet = len(ans)
#     print("#{} {}".format(test_case + 1, meet))

T = int(input().replace('혻', ''))
for test_case in range(T):
    xmin, ymin, xmax, ymax = map(int, input().replace('혻', '').split())
    x1, y1, x2, y2 = map(int, input().replace('혻', '').split())

    meet = 0
    sx, sy, bx, by = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

    if xmin > bx or xmax < sx or ymin > by or ymax < sy:
        pass

    elif y1 == y2:
        if sx == xmax or bx == xmin:
            meet = 1
        elif y1 in (ymin, ymax):
            meet = 4
        else:
            if sx <= xmin:
                meet += 1
            if bx >= xmax:
                meet += 1

    elif x1 == x2:
        if sy == ymax or by == ymin:
            meet = 1
        elif x1 in (xmin, xmax):
            meet = 4
        else:
            if sy <= ymin:
                meet += 1
            if by >= ymax:
                meet += 1

    elif sx == xmax or bx == xmin or sy == ymax or by == ymin:
        meet = 1

    else:
        m = (y2 - y1) / (x2 - x1)
        ky1 = m * (xmin - x1) + y1
        ky2 = m * (xmax - x1) + y1
        kx1 = (ymin - y1) / m + x1
        kx2 = (ymax - y1) / m + x1

        if sy <= ky1 <= by and ymin < ky1 < ymax:
            meet += 1
        if sy <= ky2 <= by and ymin < ky2 < ymax:
            meet += 1
        if sx <= kx1 <= bx and xmin <= kx1 <= xmax:
            meet += 1
        if sx <= kx2 <= bx and xmin <= kx2 <= xmax:
            meet += 1

    print("#{} {}".format(test_case + 1, meet))