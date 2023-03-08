import sys
sys.stdin = open("D3_16800_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = N - 2
    x = 1
    maxNum = int(N ** 0.5)
    while x <= maxNum:
        if N % x == 0:
            y = N // x
            ans = min(ans, x + y - 2)
            if x == 1:
                ans += 1
        x += 1
    print("#{} {}".format(test_case + 1, ans))