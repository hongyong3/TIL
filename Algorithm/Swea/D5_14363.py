import sys
sys.stdin = open("D5_14363_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    p = q = [i for i in range(N)]
    a = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if p[i] and q[j]:
                a[i][j] = '#'
            else:
                a[i][j] = '.'

                