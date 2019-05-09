import sys
sys.stdin = open('p2.txt')


def mycal(Ls):
    n1 = Ls[0]
    n2 = Ls[1]
    n3 = Ls[2]
    return abs(n1-n2)+abs(n2-n3)+abs(n3-n1)


def comb(idx, cnt, L):
    if cnt == 3:
        k = []
        for idx in range(len(chk)):
            if chk[idx] == 1:
                k.append(L[idx])
        rchk.append(k[:])
        return
    if idx >= 6:
        return
    chk[idx] = 1
    comb(idx+1, cnt+1, L)
    chk[idx] = 0
    comb(idx+1, cnt, L)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    s_data = []
    chk = [0 for _ in range(6)]

    for Y in range(1, N):
        for X1 in range(1, M-1):
            for X2 in range(X1+1, M):
                t1 = 0
                t2 = 0
                t3 = 0
                t4 = 0
                t5 = 0
                t6 = 0
                for y in range(Y):
                    for x in range(X1):
                        t1 += data[y][x]
                for y in range(Y):
                    for x in range(X1, X2):
                        t2 += data[y][x]
                for y in range(Y):
                    for x in range(X2, M):
                        t3 += data[y][x]
                for y in range(Y, N):
                    for x in range(X1):
                        t4 += data[y][x]
                for y in range(Y, N):
                    for x in range(X1, X2):
                        t5 += data[y][x]
                for y in range(Y, N):
                    for x in range(X2, M):
                        t6 += data[y][x]
                s_data.append([t1, t2, t3, t4, t5, t6])
    rchk = []
    for i in range(len(s_data)):
        comb(0, 0, s_data[i])

    result = []
    for i in rchk:
        result.append(mycal(i))
    print('#{} {}'.format(tc, max(result)))





