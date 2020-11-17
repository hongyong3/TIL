import sys
sys.stdin = open("D3_6958_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    cnt, score = 0, 0
    for _ in range(N):
        data = sum(list(map(int, input().split())))
        if data > score:
            score = data
            cnt = 1
        elif score == data:
            cnt += 1
    print("#{} {} {}".format(test_case + 1, cnt, score))