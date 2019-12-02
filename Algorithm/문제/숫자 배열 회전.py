import sys
sys.stdin = open("숫자 배열 회전_input.txt", "r")
T = int(input())
for test_case in range(T):
    N = int(input())
    data = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(4)]
    for i in range(N):
        data[0][i] = list(map(int, input().split()))
    for k in range(1, 4):
        for i in range(N):
            for j in range(N):
                data[k][j][N-1-i] = data[k-1][i][j]

    print("#{}".format(test_case+1))
    for i in range(N):
        for k in range(1, 4):
            if k != 1:
                print(end=" ")
            for j in range(N):
                print(data[k][i][j], end="")
        print()