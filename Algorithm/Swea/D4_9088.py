import sys
sys.stdin = open("D4_9088_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = sorted([int(input()) for _ in range(N)])
    ans, cnt = 1, 1

    for i in range(N - 1):
        before = data[i]
        cnt = 1
        for j in range(i + 1, N):
            after = data[j]
            if after - before <= K:
                cnt += 1
            else:
                break
        if ans < cnt:
            ans = cnt
    print("#{} {}".format(test_case + 1, ans))