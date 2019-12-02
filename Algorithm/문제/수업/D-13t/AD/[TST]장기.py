import sys
sys.stdin = open("[TST]장기_input.txt", "r")


def BFS(x, y, count):
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]   # 8방향
    dy = [1, 2, 2, 1, -1, -2, -2, -1]   # 8방향
    Q = [(x, y, count)]
    while Q:
        x, y, count = Q.pop(0)
        if x == s - 1 and y == k - 1:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if data[nx][ny] == 0:
                    data[nx][ny] = count
                    Q.append((nx, ny, count + 1))

N, M = map(int, input().split())
data = [[0] * M for _ in range(N)]
r, c, s, k = map(int, input().split())
print(BFS(r-1, c-1, 0))