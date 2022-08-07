import sys
sys.stdin = open("D2_14510_input.txt", "r")

# 49 // 50
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    high = max(data)
    ans, n1, n2, n4, n5 = 0, 0, 0, 0, 0
    for i in data:
        k = high - i
        if k % 3:
            if k > 6:
                ans += (k // 6) * 4
                k %= 6
            if k == 1:
                n1 += 1
            elif k == 2:
                n2 += 1
            elif k == 4:
                n4 += 1
            else:
                n5 += 1
        else:
            ans += (k // 3) * 2

    m = min(n1, n2)
    ans += 2 * m
    n1 -= m
    n2 -= m

    if n1:
        if n5:
            m = min(n1, n5)
            ans += 4 * m
            n1 -= m
            n5 -= m
        if n4:
            m = min(n1 // 2, n4)
            ans += 4 * m
            n1 -= 2 * m
            n4 -= m
        if n1:
            ans += (2 * n1) - 1
            n1 -= n1

    if n2:
        if n4:
            m = min(n2, n4)
            ans += 4 * m
            n2 -= m
            n4 -= m
        if n5:
            m = min(n2 // 2, n5)
            ans += 6 * m
            n2 -= 2 * m
            n5 -= m
        if n2:
            ans += (n2 // 3) * 4
            if n2 % 3 == 1:
                ans += 2
            elif n2 % 3 == 2:
                ans += 3

    if n4 and n5:
        m = min(n4, n5)
        ans += 6 * m
        n4 -= m
        n5 -= m

    if n4:
        ans += (n4 // 3) * 8
        if n4 % 3 == 1:
            ans += 3
        elif n4 % 3 == 2:
            ans += 6

    if n5:
        ans += (n5 // 3) * 10
        if n5 % 3 == 1:
            ans += 4
        elif n5 % 3 == 2:
            ans += 7

    print("#{} {}".format(test_case + 1, ans))