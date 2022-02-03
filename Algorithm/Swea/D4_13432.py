import sys
sys.stdin = open("D4_13432_input.txt", "r")

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

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
    elif (s % 2 == t % 2 == 0) or gcd(s, t) != 1:
        ans = 1
    else:
        ans = 5
    print("#{} {}".format(test_case + 1, ans))

print(gcd(2546575, 54388892))