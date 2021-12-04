import sys
sys.stdin = open("D3_13253_input.txt", "r")

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def bfs(x, y, d):
    global visited
    minAns = float('inf')
    q = [(x, y, d)]

    for i in q:
        x, y, d = i[0], i[1], i[2]
        visited[x][y] = d
        if arr[x][y] >= 1:
            if arr[x][y] >= n and d < minAns:
                minAns = d
            continue

        if d >= minAns:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r and d + 10 < visited[nx][ny]:
                q.append((nx, ny, d + 10))

    return - 1 if minAns == float('inf') else minAns

T = int(input())
for test_case in range(T):
    n, r, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]
    ans, temp = 0, 0
    for i in range(r):
        for j in range(c):
            if temp < arr[i][j]:
                temp = arr[i][j]
            if arr[i][j] == - 1:
                sr, sc = i, j

    if temp < n:
        print("#{} {}".format(test_case + 1, - 1))
    else:
        visited = [[float('inf')] * c for _ in range(r)]
        ans = bfs(sr, sc, 0)
        if ans < 60:
            print("#{} {}".format(test_case + 1, ans % 60))
        else:
            print("#{} {} {}".format(test_case + 1, ans // 60, ans % 60))