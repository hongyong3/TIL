import sys
sys.stdin = open("D6_1795_input.txt", "r")

# djikstra? O
# or cycle -> X

# def djikstra():
#     time1[X] = time2[X] = 0
#     q1, q2 = [], []
#     q1.append([X, 0])
#     q2.append([X, 0])
#
#     while q1:
#         x, c = q1.pop()
#         if time1[x] < c:
#             continue
#         for i in graph1[x]:
#             nx = i[0]
#             nt = i[1] + c
#             if time1[nx] > nt:
#                 time1[nx] = nt
#                 q1.append([nx, nt])
#
#     while q2:
#         y, c = q2.pop()
#         if time2[y] < c:
#             continue
#         for i in graph2[y]:
#             ny = i[0]
#             nt = i[1] + c
#             if time2[ny] > nt:
#                 time2[ny] = nt
#                 q2.append([ny, nt])
#
#
# T = int(input())
# for test_case in range(T):
#     N, M, X = map(int, input().split())
#     graph1 = [[] for _ in range(N + 1)]
#     graph2 = [[] for _ in range(N + 1)]
#     time1 = [float('inf')] * (N + 1)
#     time2 = [float('inf')] * (N + 1)
#     ans = 0
#     for _ in range(M):
#         x, y, c = map(int, input().split())  # x -> y, time
#         graph1[x].append([y, c])  # add y and time in graph's x index
#         graph2[y].append([x, c])  # add x and time in graph's y index
#     djikstra()
#
#     for i in range(1, N + 1):
#         ans = max(ans, time1[i] + time2[i])
#     print("#{} {}".format(test_case + 1, ans))

def djikstra(n):
    if n > 1:
        return
    q = []
    q.append([X, 0])

    while q:
        x, c = q.pop()
        if time[n][x] < c:
            continue
        for i in graph[n][x]:
            nx = i[0]
            nt = i[1] + c
            if time[n][nx] > nt:
                time[n][nx] = nt
                q.append([nx, nt])
    djikstra(n + 1)


T = int(input())
for test_case in range(T):
    N, M, X = map(int, input().split())
    graph = [[[] for _ in range(N + 1)] for _ in range(2)]
    time = [[float('inf')] * (N + 1) for _ in range(2)]
    time[0][X] = time[1][X] = 0
    for _ in range(M):
        x, y, c = map(int, input().split()) # x -> y, time
        graph[0][x].append([y, c])    # add y and time in graph's x index
        graph[1][y].append([x, c])    # add x and time in graph's y index
    djikstra(0)
    mat = 0
    for i in range(1, N + 1):
        mat = max(mat, time[0][i] + time[1][i])
    print("#{} {}".format(test_case + 1, mat))