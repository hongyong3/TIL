import sys
sys.stdin = open("D4_5643_input.txt", "r")

# Floyd_Warshall Algorithm
# 시간복잡도 O(V^3)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     M = int(input())
#     data = [[0] * N for _ in range(N)]
#     ans = 0
#
#     for _ in range(M):
#         a, b = map(int, input().split())
#         data[a - 1][b - 1] = 1
#
#     for m in range(N):
#         for s in range(N):
#             for e in range(N):
#                 if data[s][e] == 1 or (data[s][m] == 1 and data[m][e] == 1):
#                     data[s][e] = 1
#
#     for s in range(N):
#         known_people = 0
#         for e in range(N):
#             known_people += data[s][e] + data[e][s]
#         if known_people == N - 1:
#             ans += 1
#     print("#{} {}".format(test_case + 1, ans))

# BFS로도 가능할 듯

# import collections
#
# def bfs(v, arr):
#     q = collections.deque()
#     subAns = 0
#     visited[v] = 1
#     q.append(v)
#
#     while q:
#         v = q.popleft()
#         for i in arr[v]:
#             visited[i] = 1
#             q.append(i)
#             subAns += 1
#
#     return subAns
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     M = int(input())
#
#     dataT = [[] for _ in range(N)]
#     dataS = [[] for _ in range(N)]
#
#     for _ in range(M):
#         a, b = map(int, input().split())
#         dataT[a - 1].append(b)
#         dataS[b - 1].append(a)
#
#     ans = 0
#     for i in range(N):
#         visited = [0] * (N)
#         knownPeople = bfs(i, dataT) + bfs(i, dataS) + 1