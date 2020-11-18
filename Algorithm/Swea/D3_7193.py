import sys
sys.stdin = open("D3_7193_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, X = map(str, input().split())
    ans = 0
    for i in X:
        ans += int(i)
    print("#{} {}".format(test_case + 1, ans % (int(N) - 1)))