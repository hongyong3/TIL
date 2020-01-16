import sys
sys.stdin = open("D4_1249_input.txt", "r")

# BFS
#
# dx = [1, 0, - 1, 0] # 하 우 상 좌
# dy = [0, 1, 0, - 1]
#
# def bfs(x, y):
#     visited[x][y] = 0
#     q = [(x, y)]
#     while q:
#         x, y = q.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= nx < N) and (0 <= ny < N):
#                 if visited[nx][ny] > visited[x][y] + data[x][y]:
#                     visited[nx][ny] = visited[x][y] + data[x][y]
#                     q.append((nx, ny))
#     return visited[- 1][- 1]
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input())) for _ in range(N)]
#     visited = [[float('inf')] * N for _ in range(N)]
#     print("#{} {}".format(test_case + 1, bfs(0, 0)))
#     # bfs(0, 0)
#     # print("#{} {}".format(test_case + 1, visited[- 1][- 1]))


# heapq

import heapq

dx = [1, 0, - 1, 0] # 하 우 상 좌
dy = [0, 1, 0, - 1]

def dijkstra(x, y):
    distance[x][y] = 0
    heapq.heappush(heap, (distance[x][y], x, y))

    while True:
        d, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            return distance[x][y]
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and distance[nx][ny] > distance[x][y] + data[nx][ny]:
                distance[nx][ny] = distance[x][y] + data[nx][ny]
                heapq.heappush(heap, (distance[nx][y], nx, ny))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    heap = []
    print("#{} {}".format(test_case + 1, dijkstra(0, 0)))