import sys
sys.stdin = open("D4_10908_input.txt", "r")

def pow(a, n):
    if n == 0:
        return 1
    return a * pow(a, n - 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    ans, cnt = N + 1, 0

    while N >= 1:
        if N % 2:
            cnt += 1
        N //= 2
    print("#{} {}".format(test_case + 1, ans - pow(2, cnt)))