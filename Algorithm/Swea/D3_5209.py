import sys
sys.stdin = open("D3_5209_input.txt", "r")

# 이전 풀이
# def dfs(x, total):
#     global ans
#     if x == N:
#         if total < ans:
#             ans = total
#         return
#     if total > ans:
#         return
#     for y in range(N):
#         if not visited[y]:
#             visited[y] = 1
#             dfs(x + 1, total + data[x][y])
#             visited[y] = 0
#
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     ans = float('inf')
#     dfs(0, 0)
#     print("#{} {}".format(test_case + 1, ans))

def dfs(n, total):
    global ans
    if n == N:
        if ans > total:
            ans = total
        return

    if ans < total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, total + data[n][i])
            visited[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    visited = [0] * N
    dfs(0, 0)
    print("#{} {}".format(test_case + 1, ans))