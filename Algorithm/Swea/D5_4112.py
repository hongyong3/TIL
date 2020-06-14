import sys
sys.stdin = open("D5_4112_input.txt", "r")

def solve(n):
    l, h = 1, 141
    m = (l + h) // 2

    while (m - 1) * m // 2 >= n or n > m * (m + 1) // 2:
        if n > m * (m + 1) // 2:
            l = m + 1
        else:
            h = m
        m = (l + h) // 2
    return m, m * (m + 1) // 2 - n


T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    ra, da = solve(a)
    rb, db = solve(b)

    if da > db:
        ans = (rb - ra) + (da - db)
    else:
        ans = max(rb - ra, db - da)

    print("#{} {}".format(test_case + 1, ans))