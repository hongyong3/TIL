import sys
sys.stdin = open("D3_5215_input.txt", "r")

def combination(score, cal, k):
    global maxScore, N
    if k + 1 > N:
        if cal <= L and score > maxScore:
            maxScore = score
        return
    combination(score, cal, k + 1)
    combination(score + data[k][0], cal + data[k][1], k + 1)


T = int(input())
for test_case in range(T):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    maxScore = 0
    combination(0, 0, 0)
    print("#{} {}".format(test_case + 1, maxScore))