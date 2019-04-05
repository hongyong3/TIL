import sys
sys.stdin = open("[TST]로봇_input.txt", "r")

def BFS():
    dr = [0, 0, 0, 1, -1]   # 동 서 남 북 1234
    dc = [0, 1, -1, 0, 0]
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)] # 동서남북1234별 왼쪽턴 0열, 오른쪽턴 1열
    que = [(sr, sc, sdir, 0)]   # 행 열 방향, 명령횟수
    chk[sdir][sr][sc] = 1
    # 1] 시작점을 큐에 저장 (방문표시)
    while que:
        # 2] 큐에서 데이터 읽기
        r, c, dir, cnt = que.pop(0) # 현재위치
        if r == er and c == ec and dir == edir: return cnt
        for i in range(1, 4):   # go 1, 2, 3
            nr = r + dr[dir] * i
            nc = c + dc[dir] * i
            if nr < 0 or nr >= R or nc < 0 or nc >= C: break    # 맵범위 벗어나면
            if arr[nr][nc] == 1: break  # 벽이면
            if chk[dir][nr][nc]: continue   # 길이지만 방문했다면 스킵
            que.append((nr, nc, dir, cnt + 1))
            chk[dir][nr][nc] = 1
        for i in range(2):  # Turn Left : 0 열, Turn Right : 1열
            ndir = turn[dir][i]
            if chk[ndir][r][c]: continue
            que.append((r, c, ndir, cnt + 1))
            chk[ndir][r][c] = 1



R, C = map(int, input().split())
chk = [[[0] * C for _ in range(R)] for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr, sc = sr - 1, sc - 1
er, ec = er - 1, ec - 1
sol = BFS()
print(sol)