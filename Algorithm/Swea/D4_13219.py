import sys
sys.stdin = open("D4_13219_input.txt", "r")

import math
T = int(input())
for test_case in range(T):
    p, x, y = map(int, input().split())
    flag = 1 if (x - 50) ** 2 + (y - 50) ** 2 <= 2500 else 0
    if not flag:
        ans = 0
    else:
        thetaP = 3.6 * p
        a = ((50 - x) ** 2 + (100 - y) ** 2) ** 0.5
        c = ((50 - x) ** 2 + (50 - y) ** 2) ** 0.5
        theta = math.acos((2500 + c ** 2 - a ** 2) / (100 * c)) * 180 / math.pi
        if x < 50:
            theta = 360 - theta
        ans = 0 if thetaP < theta else 1
    print("#{} {}".format(test_case + 1, ans))