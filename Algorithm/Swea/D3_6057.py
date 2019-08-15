import sys
sys.stdin = open("D3_6057_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    temp = [[0] * (N) for _ in range(N)]
    count = 0

    for i in range(N):
        temp[data[i][0] - 1][data[i][1] - 1] = 1
        temp[data[i][1] - 1][data[i][0] - 1] = 1

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if data[j][i] == 0: continue
                if data[k][i] == 0: continue
                if data[k][j] == 0: continue
                count += 1
    print("#{} {}".format(test_case + 1, count))