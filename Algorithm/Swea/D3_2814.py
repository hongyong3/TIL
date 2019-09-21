import sys
sys.stdin = open("D3_2814_input.txt", "r")


def solve(v, len, visit):
    global count
    visit[v] = 1
    for i in range(N):
        if i ==  v: continue
        if visit[i]: continue
        if not visited[v][i]: continue
        solve(i, len + 1, visit)
        visit[i] = 0
    if len > count:
        count = len

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    count = 0

    visited = [[0] * (N) for _ in range(N)]
    for i in range(M):
        visited[data[i][0] - 1][data[i][1] - 1] = 1
        visited[data[i][1] - 1][data[i][0] - 1] = 1
    for i in range(N):
        solve(i, 1, [0] * (N + 1))
    print("#{} {}".format(test_case + 1, count))