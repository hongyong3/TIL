import sys
sys.stdin = open("D4_11112_input.txt", "r")

T = int(input())
answer = []
for test_case in range(T):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())
    ans = "YY"
    if a <= (p - r) and b <= (q - r) and c >= (p + r) and d >= (q + r):
        ans = "NY"
    elif a >= (p - r) and b >= (q - r) and c <= (p + r) and d <= (q + r):
        x, y, z, k = (p - c) ** 2, (p - a) ** 2, (q - d) ** 2, (q - b) ** 2
        if r ** 2 >= max(x + z, x + k, y + z, y + k):
            ans = "YN"
    answer.append("#{} {}".format(test_case + 1, ans))
for i in answer:
    print(i)