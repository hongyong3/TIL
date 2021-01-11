import sys
sys.stdin = open("D4_11112_input.txt", "r")

T = int(input())
for test_case in range(T):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())
    ans = "YY"
    if a <= (p - r) and b <= (q - r) and c >= (p + r) and d >= (q + r):
        ans = "NY"
    elif a >= (p - r) and b >= (q - r) and c <= (p + r) and d <= (q + r):
        if (p - c) ** 2 + (q - d) ** 2 <= r ** 2:
            if (p - c) ** 2 + (q - b) ** 2 <= r ** 2:
                if (p - a) ** 2 + (q - d) ** 2 <= r ** 2:
                    if (p - a) ** 2 + (q - b) ** 2 <= r ** 2:
                        ans = "YN"
    print("#{} {}".format(test_case + 1, ans))