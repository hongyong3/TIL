def dfs(S):
    global L, visited, V
    visited[S] = 1
    print(visited)
    # print(S, end=" ")

    for w in range(V):
        if L[S][w] == 1 and visited[w] == 0:
            dfs(w)

    if visited[G] == 1:
        return 1
    else:
        return 0


import sys
sys.stdin =open("그래프 경로_input.txt", "r")
T = int(input())
for N in range(T):
    V, E = map(int, input().split())
    V += 1
    # print(V, E)
    L = [[0 for _ in range(V)] for _ in range(V)]
    # print(L)
    visited = [0 for i in range(V)]
    # print(visited)
    for C in range(E):
        i, j = map(int, input().split())
        L[i][j] = 1
    print(L)
    S, G = map(int, input().split())
    # print(S, G)

    print(f'#{N+1} {dfs(S)}')
