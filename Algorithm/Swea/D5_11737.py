import sys
sys.stdin = open("D5_11737_input.txt", "r")

def solve(N, i):
    if N == 1:
        x = (i - 1) // 2
        y = (i - 1) % 2
        return x + 1, int(x != y) + 1

    x = (i - 1) // (4 ** (N - 1))
    y = (i - 1) % (4 ** (N - 1)) + 1

    ar_1, ar_2 = solve(N - 1, y)

    if x == 0:
        return ar_2, ar_1
    if x == 1:
        return ar_1, 2 ** (N - 1) + ar_2
    if x == 2:
        return 2 ** (N - 1) + ar_2, 2 ** (N - 1) + ar_2
    if x == 3:
        return 2 ** N + 1 - ar_2, 2 ** (N - 1) + 1 - ar_1


T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    a1, a2 = solve(N, A)
    b1, b2 = solve(N, B)
    ans = round(10 * ((a1 - b1) ** 2 + (a2 - b2) ** 2) ** 0.5)
    print("#{} {}".format(test_case + 1, ans))