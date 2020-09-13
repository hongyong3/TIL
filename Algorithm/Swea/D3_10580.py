import sys
sys.stdin = open("D3_10580_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat = 0

    for i in range(N):
        a, b = data[i][0], data[i][1]
        for j in range(i + 1, N):
            c, d = data[j][0], data[j][1]
            if a > c and b < d or a < c and b > d:
                mat += 1
    print("#{} {}".format(test_case + 1, mat))