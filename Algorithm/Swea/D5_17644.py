import sys
sys.stdin = open("D5_17644_input.txt", "r")

def solve(total):
    idx, sqr = 0, 1
    while sqr <= total:
        sqr *= 2
        idx += 1
    return idx, sqr // 2

T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    if X >= 2 ** (N - 1):
        ans = [- 1]
    else:
        ans = [i for i in range(1, N + 1)]

        while X:
            idx, tot = solve(X)
            ans[0], ans[idx] = ans[idx], ans[0]
            X -= tot
    print("#{}".format(test_case + 1), *ans)