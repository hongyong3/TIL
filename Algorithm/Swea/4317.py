import sys
sys.stdin = open("4317_input.txt", "r")

# Runtime Error
# def chk(x, y):
#     if x + 1 >= H or y + 1 >= W:
#         return False
#     if arr[x][y] or arr[x + 1][y] or arr[x][y + 1] or arr[x + 1][y + 1]:
#         return False
#     return True
#
#
# def dfs(x, y, cnt):
#     global ans
#     if x >= H - 1:
#         x = 0
#         y += 1
#
#     if y == W - 1:
#         if ans < cnt:
#             ans = cnt
#         return
#
#     if x == 0:
#         bit = 0
#         for i in range(H):
#             bit |= arr[i][y] << i
#         if dp[bit][y] >= cnt:
#             return
#         dp[bit][y] = cnt
#
#     if chk(x, y):
#         arr[x][y] = arr[x + 1][y] = arr[x][y + 1] = arr[x + 1][y + 1] = 1
#         dfs(x + 2, y, cnt + 1)
#         arr[x][y] = arr[x + 1][y] = arr[x][y + 1] = arr[x + 1][y + 1] = 0
#     dfs(x + 1, y, cnt)
#
# T = int(input())
# dp = [[- 1] * 24 for _ in range(1024)]
# for test_case in range(T):
#     H, W = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     for i in range(H):
#         for j in range(W):
#             dp[i][j] = - 1
#     ans = 0
#     dfs(0, 0, 0)
#     print("#" + str(test_case + 1) + ' ' + str(ans))