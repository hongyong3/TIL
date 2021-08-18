import sys
sys.stdin = open("D3_12201_input.txt", "r")

def solve(n, i):
    if n <= 1:
        return n
    x = 1
    while 2 * x <= n:
        x *= 2
    if i < x:
        return solve(n // 2, i)
    elif i > x:
        return solve(n // 2, i - x)
    else:
        return n % 2

T = int(input())
for test_case in range(T):
    N, idx = map(int, input().split())
    ans = solve(N, idx)
    print("#{} {}".format(test_case + 1, ans))