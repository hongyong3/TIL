import sys
sys.stdin = open("D4_10966_input.txt", "r")

# Runtime Error...
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     data = [list(map(str, input())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     w = []
#     ans = 0
#
#     for i in range(N):
#         for j in range(M):
#             if data[i][j] == 'W':
#                 w.append((i, j))
#
#     for i in range(N):
#         for j in range(M):
#             if data[i][j] == 'L':
#                 minVal = float('inf')
#                 for x, y in w:
#                     if abs(x - i) + abs(y - j) < minVal:
#                         minVal = abs(x - i) + abs(y - j)
#                 ans += minVal
#     print("#{} {}".format(test_case + 1, ans))

# dx = [- 1, 1, 0, 0] # 상 하 좌 우
# dy = [0, 0, - 1, 1]
#
# def dfs(x, y):
#     dis = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < N and 0 <= ny < M):
#             if data[nx][ny] == 'L':
#                 pass
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     data = [list(map(str, input())) for _ in range(N)]
#     arr = [[float('inf')] * M for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     w = []
#     ans = 0
#     for i in range(N):
#         for j in range(M):
#             if data[i][j] == 'W':
#                 dfs(i, j)
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans, water, land = 0, set(), []

    for i in range(N):
        data = input()
        for j in range(M):
            if data[j] == 'W':
                water.add(i + j)
            else:
                land.append(i + j)
    water = sorted(list(water))
    land = sorted(land)
    for i in land:
        d = float('inf')
        for j in water:
            temp = abs(i - j)
            if not temp:
                d = 1
                break
            else:
                if d >= temp:
                    d = temp
        ans += d
    print("#{} {}".format(test_case + 1, ans))