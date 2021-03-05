import sys
sys.stdin = open("D3_5252_ipnut.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    ans = 0
    for i in range(M):
        if input() in data:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))