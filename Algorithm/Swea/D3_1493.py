import sys
sys.stdin = open("D3_1493_input.txt", "r")

def solve(n):
    for i in range(1, 144):
        if n < 1 + (i * (i - 1)// 2):
            diff = n - (1 + (i - 1) * (i - 2) // 2)
            return diff + 1, i - 1 - diff

def value(x, y):
    n, diff = y + x - 1, x - 1
    return diff + 1 + (n * (n - 1)) // 2

T = int(input())
for test_case in range(T):
    p, q = map(int, input().split())
    x, y = map(sum, zip(solve(p), solve(q)))
    print("#{} {}".format(test_case + 1, value(x, y)))