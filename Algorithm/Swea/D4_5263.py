import sys
sys.stdin = open("D4_5263_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat = 0

    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                data[i][j] = float('inf')

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    data[i][j] = min(data[i][j], data[i][k] + data[k][j])

    for i in range(N):
        for j in range(N):
            if i != j and data[i][j] > mat:
                mat = data[i][j]
    print("#{} {}".format(test_case + 1, mat))