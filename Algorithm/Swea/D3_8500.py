import sys
sys.stdin = open("D3_8500_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans, cnt = N + sum(data), 0
    for i in data:
        cnt = max(cnt, i)
    print(ans + cnt)