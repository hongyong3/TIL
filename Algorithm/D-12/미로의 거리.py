def bfs(x,y):
    queue=[]
    queue.append([x,y])
    visited[x][y] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(4):
            new_x = t[0] + dx[i]
            new_y = t[1] + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if data[new_x][new_y] == 3:
                    visited[new_x][new_y] = visited[t[0]][t[1]]
                    return visited[new_x][new_y] -1
                if data[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = visited[t[0]][t[1]] + 1
                    queue.append([new_x, new_y])
    return 0

import sys
sys.stdin = open("미로의 거리_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                start_x, start_y = x, y
                ans = bfs(start_x, start_y)

    print(f"#{test_case} {ans}")