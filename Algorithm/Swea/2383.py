import sys
sys.stdin = open("2383_input.txt", "r")

def selectStair():
    stair1_r, stair1_c, stair1_m = S[0][0], S[0][1], S[0][2]
    stair2_r, stair2_c, stair2_m = S[1][0], S[1][1], S[1][2]
    stair1, stair2 = [], []
    for i in range(len(P)):
        pr, pc = P[i][0], P[i][1]
        if select[i] == 1:
            stair1.append([abs(stair1_r - pr) + abs(stair1_c - pc), stair1_m])
        elif select[i] == 2:
            stair2.append([abs(stair2_r - pr) + abs(stair2_c - pc), stair2_m])


def select(x):
    if x >= len(P):
        selectStair()
        return
    else:
        sel_Stair[x] = 1
        select(x + 1)
        sel_Stair[x] = 2
        select(x + 1)


T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    S, P = [], []

    for i in range(N):
        for j in range(N):
            if data[i][j] >= 2:
                S.append([i, j, data[i][j]])
            if data[i][j] == 1:
                P.append([i, j])
    sel_Stair = [0] * len(P)
    select=(0)