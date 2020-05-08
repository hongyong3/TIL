import sys
sys.stdin = open("D3_9700_input.txt", "r")

T = int(input())
for test_case in range(T):
    p, q = map(float, input().split())
    s1, s2 = (1 - p) * q, p * (1 - q) * q
    ans = "YES" if s1 < s2 else "NO"
    print("#{} {}".format(test_case + 1, ans))