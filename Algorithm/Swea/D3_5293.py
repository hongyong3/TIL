import sys
sys.stdin = open("D3_5293_input.txt", "r")

def solve(x, a, b, c, d):
    global ans
    if ans is not None: return
    if b - c > 1 or c - b > 1: return
    if a < 0 or b < 0 or c < 0 or d < 0: return
    if a == 0 and b == 0 and c == 0 and d == 0:
        ans = x
        return
    if x[len(x) - 1] == "0":
        solve(x + "0", a - 1, b, c, d)
        solve(x + "1", a, b - 1, c, d)
        return
    solve(x + "0", a, b, c - 1, d)
    solve(x + "1", a, b, c, d - 1)

T = int(input())
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    total, ans = A + B + C + D, None
    solve("0", A, B, C, D)
    solve("1", A, B, C, D)
    if ans is None:
        ans = "impossible"
    print("#{} {}".format(test_case + 1, ans))