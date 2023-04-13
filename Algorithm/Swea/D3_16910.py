import sys
sys.stdin = open("D3_16910_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 2 * N + 1
    for i in range(1, N + 1):
        ans += (2 * int((N ** 2 - i ** 2) ** 0.5) + 1) * 2
    print("#{} {}".format(test_case + 1, ans))