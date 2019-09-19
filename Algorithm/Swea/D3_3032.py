import sys
sys.stdin = open("D3_3032_input.txt", "r")

def gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    print("#{} ".format(test_case + 1), end="")
    print(*gcd(A, B))