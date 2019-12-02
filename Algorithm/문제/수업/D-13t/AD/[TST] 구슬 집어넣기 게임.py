import sys
sys.stdin = open("[TST] 구슬 집어넣기 게임_input.txt", "r")

def BFS():
    global Rr, Rc, Br, Bc, Hr, Hc
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = []
    Q = [(Rr, Rc, Br, Bc, 0)]
    visited[Rr][Rc][Br][Bc] = 1
    while Q:
        Rr, Rc, Br, Bc, count = Q.pop(0)
        for i in range(4):
            Rnr, Rnc = Rr + dr[i], Rc + dc[i]
            Bnr, Bnc = Br + dr[i], Bc + dc[i]
            if 0 <= Rnr <= R - 1 and 0 <= Bnr <= R - 1 and 0 <= Rnc <= C - 1 and 0 <= Bnc <= C - 1:


T = int(input())
for test_case in range(1):
    R, C = map(int, input().split())
    data = [list(input()) for _ in range(R)]
    visited = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    Rr, Rc, Br, Bc, Hr, Hc = 0, 0, 0, 0, 0, 0
    for i in range(R):
        for j in range(C):
            if data[i][j] == 'R':
                Rr, Rc = i, j
                data[i][j] = '.'
            elif data[i][j] == 'B':
                Br, Bc = i, j
                data[i][j]= '.'
            elif data[i][j] == 'H':
                Hr, Hc = i, j
                data[i][j] = '.'

print(BFS())