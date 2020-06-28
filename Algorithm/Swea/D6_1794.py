import sys
sys.stdin = open("D6_1794_input.txt", "r")

# 점화식 f(n) = (n - 1) * (f(n - 1) + f(n - 2)) (단, n >= 3; f(0) = f(1) = 0, f(2) = 1)
# ans = f(n)^2
# N %= M
# 계산을 할 때마다 % M

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    N %= M
    memo = [0, 0, 1] + [0] * N
    for i in range(3, N + 1):
        memo[i] = ((i - 1) * (memo[i - 1] + memo[i - 2])) % M
    print("#{} {}".format(test_case + 1, (memo[N] ** 2) % M))