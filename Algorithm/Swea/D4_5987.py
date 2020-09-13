import sys
sys.stdin = open("D4_5987_input.txt", "r")

def dp(n):
    if n == (1 << N) - 1:
        return 1
    if mat[n] != - 1:
        return mat[n]
    mat[n] = 0
    for i in range(N):
        if n & (1 << i) == 0 and solve(n, i):
            mat[n] += dp(n | (1 << i))
    return mat[n]

def solve(n, idx):
    for i in data[idx]:
        if (n & 1 << i) > 0:
            return False
    return True

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [[] for _ in range(N)]

    for _ in range(M):
        x, y = map(int, input().split())
        data[y - 1].append(x - 1)

    mat = [- 1] * (1 << N)
    print("#{} {}".format(test_case + 1, dp(0)))