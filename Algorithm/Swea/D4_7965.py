import sys
sys.stdin = open("D4_7965_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                ans += 1
    # print("#{} {}".format(test_case + 1, ans))