import sys
sys.stdin = open("D3_4466_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    score = sorted(list(map(int, input().split())))
    sum = 0
    for i in range(K):
        sum += score[- 1 - i]
    print("#{} {}".format(test_case + 1, sum))