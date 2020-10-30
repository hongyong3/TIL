import sys
sys.stdin = open("D3_6913_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    cnt, score = 1, 0
    for _ in range(N):
        data = list(map(int, input().split()))
        if sum(data) > score:
            score = sum(data)
            cnt += 1
    print(cnt, score)