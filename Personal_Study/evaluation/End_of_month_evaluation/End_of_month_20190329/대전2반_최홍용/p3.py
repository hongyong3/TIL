import sys
sys.stdin = open("p3_input.txt", "r")

def BFS(x, y, cnt):
    global count
    Q = [(x, y, cnt)]
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]  # 상 하 좌 우
    while Q:
        x, y, cnt = Q.pop(0)
        if data[x][y] == 2:
            data[x][y] = 0
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= M - 1 and 0 <= ny <= M - 1:
                # for i in eatt:
                #     if nx == i[0] or ny == i[1]:
                #         break
                data[nx][ny] = cnt
                Q.append((nx, ny, cnt+1))
                count += cnt
    return count

T = int(input())
for test_case in range(1):
    N = int(input())
    M, count = 100, 0
    eat = list(map(int, input().split()))   # 2
    rob = list(map(int, input().split()))   # 1
    robb = []
    data = [[0] * M for _ in range(M)]
    for i in range(N):
        data[eat[2*i]][eat[2*i+1]] = 2   # eat의 좌표입력
        data[rob[2*i]][rob[2*i+1]] = 1   # rob의 좌표입력
        robb.append((rob[2*i], rob[2*i+1]))
        BFS(robb[i][0], robb[i][1], 0)
    print("#{} {}".format(test_case+1, BFS(robb[i][0], robb[i][1], 0)))
