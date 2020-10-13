import sys
sys.stdin = open("D2_2369_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    for _ in range(N):
        l, r = map(int, input().split())
        ans += r - l + 1
    print("#{} {}".format(test_case + 1, ans))