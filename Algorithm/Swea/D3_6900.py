import sys
sys.stdin = open("D3_6900_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    Ndata = [list(map(str, input().split())) for _ in range(N)]
    Mdata = [str(input()) for _ in range(M)]
    ans = 0
    chk = [0] * N
    for i in range(N):
        for j in range(M):
            for k in range(8):
                if Ndata[i][0][k] != '*':
                    if Ndata[i][0][k] != Mdata[j][k]:
                        break
            else:
                chk[i] += 1
                if chk[i] == 1:
                    ans += int(Ndata[i][1])
    print(ans)
