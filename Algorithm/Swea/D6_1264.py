import sys
sys.stdin = open("D6_1264_input.txt", "r")

lcs = [[0] * 501 for _ in range(501)]
T = int(input())
for test_case in range(T):
    N = int(input())
    x = input()
    y = input()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if x[i - 1] == y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    print("#{} {}".format(test_case + 1, format(lcs[N][N] / N * 100, ".2f")))