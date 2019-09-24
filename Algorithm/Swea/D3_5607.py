import sys
sys.stdin = open("D3_5607_input.txt", "r")

def x_y(x, y):
    xy = 1
    while y > 0:
        if (y % 2) == 1:
            xy *= x
            y -= 1
            xy %= m
        x *= x
        x %= m
        y /= 2
    return xy

T = int(input())
for test_case in range(T):
    N, R = map(int, input().split())
    ans1, ans2, m = 1, 1, 1234567891
    for i in range(N - R + 1, N + 1):
        ans1 *= i
        ans1 %= m
    for i in range(1, R + 1):
        ans2 *= i
        ans2 %= m

    ans2 = x_y(ans2, m - 2)
    ans2 %= m
    ans1 *= ans2
    ans1 %= m
    print("#{} {}".format(test_case + 1, ans1))