import sys
sys.stdin = open("D4_13432_input.txt", "r")

# RuntimeError 66 // 106
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def factorization(n):
    res = set()
    d = 2
    while d <= n:
        if n % d == 0:
            res.add(d)
            n //= d
        else:
            d += 1
    return sorted(res)


T = int(input())
for test_case in range(T):
    n, s, t = map(int, input().split())
    if s < t:
        s, t = t, s
    ans = - 1
    if s == t:
        ans = 0
    elif s == 1 or t == 1:
        ans = - 1
    elif s % 2 == 0 and t % 2 == 0:
        if t % 2:
            ans = 2
        else:
            ans = 1
    else:
        sarr, tarr = factorization(s), factorization(t)
        for i in sarr:
            if i in tarr:
                ans = 1
                break
        else:
            if sarr[0] * tarr[0] <= n:
                ans = 2
    # elif s % 2 and t % 2 == 0:
    #     if s * 2 <= n:
    #         ans = 2
    # #     else:

#     elif (s % 2 == t % 2 == 0) or gcd(s, t) != 1:
#         ans = 1
#     else:
#         ans = 5
    print("#{} {}".format(test_case + 1, ans))

    