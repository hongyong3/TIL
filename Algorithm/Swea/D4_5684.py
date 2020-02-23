import sys
sys.stdin = open("D4_5684_input.txt", "r")

# Floyd - Warshall

# T = int(input().replace('혻', ''))
# for test_case in range(T):
#     N, M = map(int, input().replace('혻', '').split())
#     graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
#
#     minCycle = float('inf')
#
#     for _ in range(M):
#         s, e, c = map(int, input().replace('혻', '').split())
#         graph[s][e] = c
#
#     for k in range(1, N + 1):
#         for i in range(1, N + 1):
#             for j in range(1, N + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
#     for i in range(N + 1):
#         minCycle = min(minCycle, graph[i][i])
#
#     if minCycle == float('inf'):
#         print("#{} {}".format(test_case + 1, -1))
#     else:
#         print("#{} {}".format(test_case + 1, minCycle))

# input runtime error 해결..
temporary = input()
T = ''
for t in temporary:
    if t.isdigit():
        T += t
for test_case in range(int(T)):
    temporary = input()
    temporaryNM = ['', '']
    tt = 0
    for t in temporary:
        if t.isdigit():
            temporaryNM[tt] += t
        if t == ' ':
            tt += 1
    N, M = int(temporaryNM[0]), int(temporaryNM[1])

    graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    cycle = float('inf')

    for _ in range(M):
        temporary = input()
        temporarySEC = ['', '', '']
        tt = 0
        for t in temporary:
            if t.isdigit():
                temporarySEC[tt] += t
            if t == ' ':
                tt += 1
        s, e, c = int(temporarySEC[0]), int(temporarySEC[1]), int(temporarySEC[2])
        graph[s][e] = c

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, N + 1):
        cycle = min(cycle, graph[i][i])

    if cycle == float('inf'):
        print("#{} {}".format(test_case + 1, -1))
    else:
        print("#{} {}".format(test_case + 1, cycle))