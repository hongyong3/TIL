import sys
sys.stdin = open("D5_7585_input.txt", "r")


def solve(n, p):
    temp = 1
    while p:
        if p & 1:
            temp = (temp * n) % K
        n = (n * n) % K
        p >>= 1
    return temp

MOD = 1000000007
T = int(input())
for test_case in range(T):
    A, B, N, K = map(int, input().split())
    iarr = [0] * 100001
    jarr = [0] * 100001
    m = 0
    for i in range(1, min(N, K) + 1):
        c = N // K
        if i <= (N % K):
            c += 1
        iA, jB = solve(i, A) % K, solve(i, B) % K

        iarr[iA] += c
        jarr[jB] += c
        iarr[iA] %= MOD
        jarr[jB] %= MOD

        if ((iA + jB) % K) == 0:
            m = (m + c) % MOD

    ans = (iarr[0] * jarr[0]) % MOD

    for i in range(1, K):
        ans = (ans + (iarr[i] * jarr[K - i]) % MOD) % MOD
    print("#{} {}".format(test_case + 1, (ans - m + MOD) % MOD))