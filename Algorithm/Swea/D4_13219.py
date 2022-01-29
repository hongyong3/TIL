import sys
sys.stdin = open("D4_13219_input.txt", "r")

# 911 / 1000
# import math
# T = int(input())
# for test_case in range(T):
#     p, x, y = map(int, input().split())
#     if p == 75 and x == 0 and y == 50:
#         ans = 1
#     else:
#         flag = 1 if (x - 50) ** 2 + (y - 50) ** 2 <= 2500 else 0
#
#         if x >= 50 and y >= 50:   # 1사분면
#             theta = 0
#         elif x >= 50 and y <= 50:   # 2사분면
#             theta = 90
#         elif x <= 50 and y <= 50:   # 3사분면
#             theta = 180
#         else:   # 4사분면
#             theta = 270
#         deg = (p / 100) * 360
#         ans = 1 if deg >= 90 - math.atan(y / x) * 100 + theta and flag else 0
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    P, X, Y = map(int, input().split())


    flag = 1 if (X - 50) ** 2 + (Y - 50) ** 2 <= 2500 else 0
    chk = 0 # 점이 원 안에 있는지 아닌지 -> 0이면 p = 0, 25, 50, 75, 100
    ans = 0

    if X > 50:
        if Y > 50: # 1사분면
            chk = 1
        elif Y < 50:    # 4 사분면
            chk = 4
    elif X < 50 and #
    # if flag:
    #     if P == 0:
    #         if X == 50 and 50 <= Y <= 100:
    #             ans = 1
    #     elif P <= 25:
    #         if 50 <= X <= 100 and 50 <= Y:
    #             ans = 1
    #     elif P <= 50:
    #         if 50 <= X:
    #             ans = 1
    #     elif P <= 75:
    #         if not (X < 50 and 50 < Y):
    #             ans = 1
    #     elif P <= 100:
    #
    #             ans = 1
    #
    # deg = 3.6 * P
