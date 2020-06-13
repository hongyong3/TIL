import sys
sys.stdin = open("D5_9222_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    num = input()
    ans = 0
    for i in range(M):
        s, e = map(int, input().split())
        if not int(num[s - 1: e] + num[:s - 1] + num[e:]) % K:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))