import sys
sys.stdin = open("D2_1979_input.txt", "r")

T = int(input())
for test_case in range(1):
    count, ans = 0, 0
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                x, y = i, j
                if data[x][y+]
    # print("#{} {}".format(test_case + 1, ans))