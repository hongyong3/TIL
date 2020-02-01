import sys
sys.stdin = open("D4_5640_input.txt", "r")

def diophantine(a, b, c):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 % r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2

    return c // r1 * s1, c // r1 * t1

T = int(input())
for test_case in range(T):
    A, B, C = map(int, input().split())
    print("#{}".format(test_case + 1), *diophantine(A, B, C))