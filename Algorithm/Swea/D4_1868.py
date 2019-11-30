import sys
sys.stdin = open("D4_1868_input.txt", "r")

dx = [- 1, 1, 0, 0, - 1, - 1, 1, 1] # 상 하 좌 우 좌상 우상 좌하 우하
dy = [0, 0, - 1, 1, - 1, 1, - 1, 1] # 상 하 좌 우 좌상 우상 좌하 우하

def solve():
    global count
    count += 1
    while q:
        x, y = q.pop(0)
        mine = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < N) and data[nx][ny] == '*':
                mine += 1

        if mine == 0:
            data[x][y] = 'x'
            for i in range(8):
                nx = x + dx[i]
                ny = x + dy[i]

                if not (0 <= nx < N and 0 <= ny < N) or data[nx][ny] != '.' or visited[nx][ny]:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny))

        else:
            data[x][y] = 'x'

def isRange(x, y):
    if (x < 0 or x >= N or y < 0 or y >= N):
        return False
    return True


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    count = 0
    visited = [[0] * N for _ in range(N)]
    q = []
    for i in data:
        print(i)
    print('--------------')
    for x in range(N):
        for y in range(N):
            if data[x][y] == '.':
                mine = 0
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if (0 <= nx < N and 0 <= ny < N) and data[nx][ny] == '*':
                        mine += 1

                if mine == 0:
                    q.append((x, y))
                    solve()
    for i in data:
        print(i)

    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                count += 1

    print("#{} {}".format(test_case + 1, count))

##################################################################################

# def boom(i, j, N):
#     for dy, dx in dir:
#         ty = i + dy;
#         tx = j + dx
#         if 0 <= ty < N and 0 <= tx < N and arr[ty][tx] != -1:
#             arr[ty][tx] += 1
#
#
# def DFS(i, j):
#     arr[i][j] = -2
#     for dy, dx in dir:
#         ty = i + dy;
#         tx = j + dx
#         if 0 <= ty < N and 0 <= tx < N:
#             if not arr[ty][tx]:
#                 DFS(ty, tx)
#             arr[ty][tx] = -2
#
#
# for tc in range(int(input())):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '*':
#                 arr[i][j] = -1
#             else:
#                 arr[i][j] = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == -1: boom(i, j, N)
#
#     for i in range(N):
#         for j in range(N):
#             if not arr[i][j]:
#                 cnt += 1
#                 DFS(i, j)
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > 0:
#                 cnt += 1
#
#     print('#{} {}'.format(tc + 1, cnt))