import sys
sys.stdin = open("D3_11315_input.txt", "r")

# 한 방향으로만 갈 수 있도록 ex) while이라던가 방향을 고정하기...
# 가로, 세로, 우상, 우하

dx = [1, 0, - 1, 1] # 하, 우, 우상, 우하,
dy = [0, 1, 1, 1]
# def dfs(x, y):
#     for i in range(4):
#         cnt = 1
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < N and 0 <= ny < N):
#             continue
#         while data[nx][ny] == 'o' and not (0 <= nx < N and 0 <= ny < N):
#             cnt += 1
#             nx += dx[i]
#             ny += dy[i]
#         if cnt == 5:
#             return True
#     if cnt < 5:
#         return False

T = int(input())
for test_case in range(1):
    N = int(input())
    data = [input() for _ in range(N)]
    ans = "NO"

    for x in range(N):
        for y in range(N):
            cnt = 1
            if data[x][y] == 'o':
                # ans = dfs(x, y)
                for k in range(4):
                    cnt = 1
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue
                    if data[nx][ny] != 'o':
                        continue
                    while True:
                        nx += dx[k]
                        ny += dy[k]
                        if not (0 <= nx < N and 0 <= ny < N):
                            break
                        if data[nx][ny] != 'o':
                            break
                        cnt += 1
                        if cnt == 5:
                            ans = "YES"
                            break
    print("#{} {}".format(test_case + 1, ans))