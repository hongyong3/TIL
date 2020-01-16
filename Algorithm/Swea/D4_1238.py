import sys
sys.stdin = open("D4_1238_input.txt", "r")

# dfs
#
# def dfs(s):
#     visited[s] = 1
#     for ns in range(1, N):
#         if arr[s][ns] and not visited[ns]:
#             visited[ns] = 1
#             if not distance[ns] or (distance[ns] and distance[ns] > distance[s] + 1):
#                 distance[ns] = distance[s] + 1
#             dfs(ns)
#             visited[ns] = 0
#     ans = 0
#     for i in range(1, N):
#         if ans <= distance[i]:
#             ans, index = distance[i], i
#     return index
#
# for test_case in range(10):
#     length, start = map(int, input().split())
#     data = list(map(int, input().split()))
#     N = max(data) + 1
#     arr = [[0] * N for _ in range(N)]
#     distance, visited = [0] * N, [0] * N
#     for i in range(length // 2):
#         arr[data[2 * i]][data[2 * i + 1]] = 1
#     print("#{} {}".format(test_case + 1, dfs(start)))

# bfs

def bfs(s):
    visited[s] = 1
    q = [(s)]

    while q:
        s = q.pop(0)
        for ns in range(1, N):
            if arr[s][ns] and not visited[ns]:
                visited[ns] = 1
                q.append(ns)
                distance[ns] = distance[s] + 1
    ans = 0
    for i in range(1, N):
        if ans <= distance[i]:
            ans, index = distance[i], i
    return index

for test_case in range(10):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))

    N = max(data) + 1
    distance, visited = [0] * N, [0] * N
    arr = [[0] * N for _ in range(N)]

    for i in range(length // 2):
        arr[data[2 * i]][data[2 * i + 1]] = 1

    print("#{} {}".format(test_case + 1, bfs(start)))