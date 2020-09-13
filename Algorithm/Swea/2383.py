import sys
sys.stdin = open("2383_input.txt", "r")

def dfs():
    global mat
    stair1_r, stair1_c, stair1_m = S[0][0], S[0][1], S[0][2]
    stair2_r, stair2_c, stair2_m = S[1][0], S[1][1], S[1][2]
    stair1, stair2, q1, q2, minute = [], [], [], [], 1
    for i in range(len(P)):
        pr, pc = P[i][0], P[i][1]
        if sel_stair[i] == 1:
            stair1.append([abs(stair1_r - pr) + abs(stair1_c - pc), stair1_m])
        elif sel_stair[i] == 2:
            stair2.append([abs(stair2_r - pr) + abs(stair2_c - pc), stair2_m])

    sorted(stair1[::-1]), sorted(stair2[::-1])

    while 1:
        if minute >= ans:
            return
        if len(q1) == 0 and len(q2) == 0 and len(stair1) == 0 and len(stair2) == 0:
            break

        for i in range(len(stair1) - 1, -1, -1):
            if len(q1) < 3 and stair1[i][0] <= minute:
                q1.append(stair1.pop(i))

        for i in range(len(stair2) - 1, -1, -1):
            if len(q2) < 3 and stair2[i][0] <= minute:
                q2.append(stair2.pop(i))

        for i in range(len(q1) - 1, -1, -1):
            q1[i][1] -= 1
            if q1[i][1] == 0:
                q1.pop(i)

        for i in range(len(q2) - 1, -1, -1):
            q2[i][1] -= 1
            if q2[i][1] == 0:
                q2.pop(i)
        minute += 1

    if minute < ans:
        ans = minute + 1


def select(x):
    if x >= len(P):
        dfs()
        return
    else:
        sel_stair[x] = 1
        select(x + 1)
        sel_stair[x] = 2
        select(x + 1)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    S, P, mat = [], [], float('inf')

    for i in range(N):
        for j in range(N):
            if data[i][j] >= 2:
                S.append([i, j, data[i][j]])
            if data[i][j] == 1:
                P.append([i, j])
    sel_stair = [0] * len(P)
    select(0)

    print("#{} {}".format(test_case + 1, mat))