import sys
sys.stdin = open("[TST]자외선을 피해 가기_input.txt", "r")

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0x7fffffff]*n for _ in range(n)]
    visited[0][0] = arr[0][0]
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:continue
            if visited[nx][ny] < visited[x][y]:continue
            if visited[nx][ny] <= visited[x][y]+arr[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y]+arr[nx][ny]
            stack.append((nx, ny))
    return visited[n-1][n-1]

# main-------------------------------------------
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
print(bfs())