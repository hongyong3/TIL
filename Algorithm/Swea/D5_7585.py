import sys
sys.stdin = open("D5_7585_input.txt", "r")

def solve(n, p):
    temp = 1
    while p:
        if p & 1:
            temp = (temp * n) % K
        n = (n * n) % K
        p >>= 1
    return temp % K

MOD = 1000000007
T = int(input())
for test_case in range(T):
    A, B, N, K = map(int, input().split())
    iarr = [0] * K
    jarr = [0] * K
    m = 0
    for i in range(1, min(N, K) + 1):
        c = N // K
        if i <= (N % K):
            c += 1
        a, b = solve(i, A), solve(i, B)

        iarr[a] = (iarr[a] + c) % MOD
        jarr[b] = (jarr[b] + c) % MOD

        if not (a + b) % K:
            m = (m + c) % MOD

    ans = iarr[0] * jarr[0] % MOD

    for i in range(1, K):
        ans += iarr[i] * jarr[K - i] % MOD
    print("#{} {}".format(test_case + 1, (ans - m) % MOD))