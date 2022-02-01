import sys
sys.stdin = open("D4_13219_input.txt", "r")

# 911 / 1000
import math
T = int(input())
for test_case in range(T):
    p, x, y = map(int, input().split())
    flag = 1 if (x - 50) ** 2 + (y - 50) ** 2 <= 2500 else 0    # circle in out
    if not flag:
        ans = 0
    else:
        degP = 3.6 * p
        radian = 180 / math.pi
        deg = math.atan(y / x) * radian

        if p == 0:
            if x == 50 and y >= 50:
                ans = 1
            else:
                ans = 0
        if x > 50 and y >= 50:  # 1사분면
            theta = 0
        elif x > 50:
            theta = 90
        # elif x >= 50 and y <= 50:   # 2사분면
        #     theta = 90
        # elif x <= 50 and y <= 50:   # 3사분면
        #     theta = 180
        # else:   # 4사분면
        #     theta = 270
        # deg = (p / 100) * 360
        # ans = 1 if deg >= 90 - math.atan(y / x) * 100 + theta and flag else 0
    # print("#{} {}".format(test_case + 1, ans))