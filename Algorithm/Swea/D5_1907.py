import sys
sys.stdin = open("D5_1907_input.txt", "r")

# 2 / 7
dx = [- 1, 1, 0, 0, - 1, - 1, 1, 1] # 상하좌우대각
dy = [0, 0, - 1, 1, - 1, 1, - 1, 1]

def bfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if arr[nx][ny] > 0:
                arr[nx][ny] -= 1
                if arr[nx][ny] == 0:
                    arr[nx][ny] = - 1
                    q.append((nx, ny))


T = int(input())
for test_case in range(T):
    H, W = map(int, input().split())
    arr = [[0] * W for _ in range(H)]
    ans = 0
    q = []

    for i in range(H):
        data = input()
        for j in range(W):
            if data[j].isdigit():
                arr[i][j] = int(data[j])

    for x in range(H):
        for y in range(W):
            if arr[x][y] == 0:
                bfs(x, y)

    while q:
        qSize = len(q)
        while qSize:
            qSize -= 1
            x, y = q.pop(0)
            bfs(x, y)
        ans += 1
    print("#{} {}".format(test_case + 1, ans))