import sys
sys.stdin = open("[TST]단지 번호붙이기_input.txt", "r")

def DFS(x, y):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if data[nx][ny] == 1:
            count += 1
            data[nx][ny] = 9
            DFS(nx, ny)
    if count == 0:
        count = 1
    return count

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
apartment = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            count = 0
            apartment.append(DFS(i, j))
print(len(apartment))
for i in sorted(apartment):
    print(i)