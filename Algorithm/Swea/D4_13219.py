import sys
sys.stdin = open("D4_13219_input.txt", "r")

# 911 / 1000
import math
T = int(input())
for test_case in range(T):
    p, x, y = map(int, input().split())
    if (p == 0 and x == 50 and 50 <= y <= 100) or (p == 100 and x == 50 and 50 <= y <= 100) or (p == 25 and 50 <= x <= 100 and y == 50) or (p == 50 and x == 50 and 0 <= y <= 50) or (p == 75 and 0 <= x <= 50 and y == 50):
        ans = 1
        # continue
    else:
        flag = 1 if (x - 50) ** 2 + (y - 50) ** 2 <= 2500 else 0
        if 50 <= x <= 100 and 50 <= y <= 100:   # 1사분면
            theta = 0
        elif 50 <= x <= 100 and y <= 50:   # 2사분면
            theta = 90
        elif x <= 50 and y <= 50:   # 3사분면
            theta = 180
        else:   # 4사분면
            theta = 270
        deg = p / 100 * 360
        ans = 1 if deg >= 90 - math.atan(y / x) * 100 + theta and flag else 0
    print("#{} {}".format(test_case + 1, ans))