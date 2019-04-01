import sys
sys.stdin = open("사람 네트워크2_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    N = data.pop(0) # 노드
    graph = []  # 그래프
    for i in range(N):
        graph.append(data[i * N : i * N + N ])  # 그래프 분리

###################################################################################

# 가지치기 필요
    for i in range(N):
        for j in range(N):
            if i == j: continue # D[i][i] = 0
            if graph[i][j] == 1: continue   # 경로가 있으면 pass
            graph[i][j] = float('inf')  # 경로가 없으면 inf

###################################################################################

    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    CC = [0] * N
    for i in range(N):
        CC[i] = sum(graph[i])
    print('#{} {}'.format(test_case+1, min(CC)))