import time
from time import strftime
start_time = time.time()
import sys
sys.stdin = open("보급로_input.txt", "r")

def BFS(x, y):
    visited[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = [(x, y)]
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if visited[nx][ny] > visited[x][y] + data[x][y]:
                    visited[nx][ny] = visited[x][y] + data[x][y]
                    Q.append((nx, ny))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    BFS(0, 0)
    print("#{} {}".format(test_case+1, visited[N - 1][N - 1]))
print(time.time() - start_time, 'seconds')