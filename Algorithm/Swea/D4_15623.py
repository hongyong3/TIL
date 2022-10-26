import sys
sys.stdin = open("D4_15623_input.txt", "r")

def solve(idx, nx, ny):
    global chk
    for i in range(1, N + 1):
        if not chk[i] and graph[idx][i] != 0:
            
    if idx == 2:
        return nx * ny


T = int(input())
for test_case in range(T):
    if test_case + 1 in [66, 73, 181, 260]:
        temp = input()
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    ans = - 1
    for i in range(M):
        A, B, X, Y = map(int, input().split())
        graph[A][B] = [X, Y]
        graph[B][A] = [X, Y]

    chk1, chk2 = 0, 0
    for i in range(1, N + 1):
        if graph[1][i] != 0:
            chk1 = 1
        if graph[2][i] != 0:
            chk2 = 1

    if chk1 and chk2:
        visited = [0] * (N + 1)
        for i in range(1, N + 1):
            if graph[1][i] != 0:
                numX, numY = graph[1][i][0], i[1][i][1]
                visited[i] = 1
                ans = solve(i, numX, numY)  # idx, 가중치X 가중치Y
        print()
    # print("#{} {}".format(test_case + 1, ans))