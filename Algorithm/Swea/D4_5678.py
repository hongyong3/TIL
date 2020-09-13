import sys
sys.stdin = open("D4_5678_input.txt", "r")

T = int(input().replace('혻', ''))
for test_case in range(T):
    seq = str(input().replace('혻', ''))
    N = len(seq)
    mat = 0
    pal = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N - i):
            if i < 2 and seq[j] == seq[i + j] or seq[j] == seq[i + j] and pal[j + 1][i + j - 1]:
                pal[j][i + j] = 1
                mat = i + 1
    print("#{} {}".format(test_case + 1, mat))