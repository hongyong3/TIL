import sys
sys.stdin = open("D6_3813_input.txt", "r")

# Binary Search
def binary(p):
    cnt, now = 0, 1
    for i in range(1, N + 1):
        cnt = cnt + 1 if W[i] <= p else 0
        if cnt == S[now]:
            cnt = 0
            now += 1
            if now > K:
                break
    if now > K:
        return now

T = int(input())
W = [0] * 200009
S = [0] * 200009
for test_case in range(T):
    N, K = map(int, input().split())
    wdata = list(map(int, input().split()))
    sdata = list(map(int, input().split()))
    for i in range(N):
        W[i + 1] = wdata[i]
    for i in range(K):
        S[i + 1] = sdata[i]

    s, e = 1, 200009

    while s < e:
        m = (s + e) // 2
        if binary(m):
            e = m
        else:
            s = m + 1
    print("#{} {}".format(test_case + 1, s))