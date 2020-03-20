import sys
sys.stdin = open("D3_5105_input.txt", "r")

# 이전 풀이
# def bfs(x,y):
#     queue=[]
#     queue.append([x,y])
#     visited[x][y] = 1
#     while len(queue) != 0:
#         t = queue.pop(0)
#         for i in range(4):
#             new_x = t[0] + dx[i]
#             new_y = t[1] + dy[i]
#             if 0 <= new_x < N and 0 <= new_y < N:
#                 if data[new_x][new_y] == 3:
#                     visited[new_x][new_y] = visited[t[0]][t[1]]
#                     return visited[new_x][new_y] -1
#                 if data[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
#                     visited[new_x][new_y] = visited[t[0]][t[1]] + 1
#                     queue.append([new_x, new_y])
#     return 0
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input())) for _ in range(N)]
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for x in range(N):
#         for y in range(N):
#             if data[x][y] == 2:
#                 start_x, start_y = x, y
#                 ans = bfs(start_x, start_y)
#     print(f"#{test_case} {ans}")

def bfs(x, y):
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if data[nx][ny] == 3:
                visited[nx][ny] = visited[x][y]
                return visited[x][y] - 1
            if not data[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return 0

dx = [0, 0, - 1, 1] # 상 하 좌 우
dy = [- 1, 1, 0, 0]
T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                print("#{} {} ".format(test_case + 1, bfs(i, j)))
                break