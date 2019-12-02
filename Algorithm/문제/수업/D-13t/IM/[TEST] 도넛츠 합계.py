import sys
sys.stdin = open("도넛츠 합계_input.txt", "r")

N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]


def check(si, sj):
    dsum = 0
    for i in range(si, si + K):
        for j in range(sj, sj + K):
            if j == sj or j == sj + K - 1:
                dsum += data[i][j]
            if (i == si or i == si + K - 1) and sj < j < sj + K -1:
                dsum += data[i][j]
    return dsum

sol = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        dsum = check(i, j)
        if dsum > sol:
            sol = dsum

print(sol)