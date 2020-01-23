import sys
sys.stdin = open("D4_1219_input.txt", "r")

def dfs(s, order):  # s : 시작 // order : 길 순서
    ans = 0
    if graph[s][order] == 0:
        return 0
    if graph[s][order] == 99:
        return 1
    ans = dfs(graph[s][order], 0)
    if ans:
        return ans
    return dfs(graph[s][order], 1)

for test_case in range(10):
    N, L = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[0, 0] for _ in range(100)]

    for i in range(L):
        if graph[data[2 * i]][0] == 0:
            graph[data[2 * i]][0] = data[2 * i + 1]
        graph[data[2 * i]][1] = data[2 * i + 1]
    print("#{} {}".format(test_case + 1, dfs(0, 0)))