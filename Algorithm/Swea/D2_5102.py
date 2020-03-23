import sys
sys.stdin = open("D2_5102_input.txt", "r")

# 이전 풀이
# def bfs(data, v):  # 1에서 가장 멀리 있는 정점을 찾으시오.
#     global G
#     queue=[]
#
#     queue.append(v)  #enQueue하면서 방문처리
#     visited[v] = 1
#
#     while len(queue) != 0:
#         t = queue.pop(0)
#         for w in range(1, V+1):
#             if data[t][w] == 1 and visited[w] == 0:
#                 queue.append(w)
#                 visited[w] = visited[t] + 1
#     result = 0
#     if visited[G]:
#         result = visited[G]-1
#     print(f"#{test_case} {result}")
#
# T = int(input())
# for test_case in range(1, T+1):
#     V, E = map(int, input().split())
#     data = [[0 for _ in range(V+1)] for _ in range(V+1)]
#     visited = [0 for _ in range(V + 1)]
#     for C in range(E):
#         i, j = map(int, input().split())
#         data[i][j] = 1
#         data[j][i] = 1
#     S, G = map(int, input().split())
#     bfs(data, S)

def bfs(graph, S):
    q = []
    q.append(S)
    visited[S] = 1

    while q:
        s = q.pop(0)
        for i in range(1, V + 1):
            if graph[s][i] and not visited[i]:
                q.append(i)
                visited[i] = visited[s] + 1
    ans = 0
    if visited[G]:
        ans = visited[G] - 1
    return ans


T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j], graph[j][i] = 1, 1
    S, G = map(int, input().split())
    print("#{} {}".format(test_case + 1, bfs(graph, S)))