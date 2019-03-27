import sys
sys.stdin = open("[TST]미로 탈출 로봇_input.txt", "r")

def BFS():
    que = []
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    # 1) 시작점을 큐에 저장(방문표시)
    que.append((sr, sc, 0)) # 행, 열, 시간 큐에 저장
    data[sr][sc] = 1 # 맵에 방문 표시
    while que:  # 큐가 있을 동안 반복
        # 2) 큐에서 data 읽기(현재좌표)
        r, c, time = que.pop(0)
        if r == er and c == ec:
            return time # 도착하면 리턴
        for i in range(4):  # 3) 사방탐색하면서 연결점(길)을 찾아 큐에 저장
            nr = r + dr[i]
            nc = c + dc[i]
            # 3-1) 맵의 범위 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue    # 맵의 범위를 벗어나면 스킵
            # 3-2) 연결점을 찾아 큐에 저장(방문표시)
            if data[nr][nc] != 0:
                continue    # 길이 아니면 스킵
            que.append((nr, nc, time+1))
            data[nr][nc] = 1
    return -1   # 4) 큐가 빈상태(예외상황)

C, R = map(int, input().split())
sc, sr, ec, er = map(int, input().split())
sc -= 1; sr -= 1; ec -= 1; er -= 1
data = [list(map(int, input()))  for _ in range(R)]
print(BFS())
