import sys
sys.stdin = open("D3_9280_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    park = [[0, int(input())] for _ in range(N)]
    W = [int(input()) for _ in range(M)]
    data = [int(input()) for _ in range(2 * M)]

    ans, wait = 0, []

    while data:
        val = data.pop(0)
        if val > 0:
            for i in range(N):
                if not park[i][0]:
                    park[i][0] = W[val - 1]
                    ans += park[i][0] * park[i][1]
                    break
            else:
                wait.append(val)
        else:
            for i in range(N):
                if park[i][0] == W[- (val + 1)]:
                    park[i][0] = 0
                    if wait:
                        park[i][0] = W[wait.pop(0) - 1]
                        ans += park[i][0] * park[i][1]
    print("#{} {}".format(test_case + 1, ans))