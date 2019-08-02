import sys
sys.stdin = open("D2_1961_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data_90, data_180, data_270 = [], [], []
    for i in range(N):
        for j in range(N):


    # 90도
            data_90[i][j] = data[N - 1 - j][i]
print(data_90)
    # 180도
    # 270도