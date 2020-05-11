import sys
sys.stdin = open("D5_5521_input.txt", "r")

def bfs():
    global ans
    q = []
    for i in range(1, N + 1):
        if data[1][i]:
            ans += 1
            visited[i] = 1
            q.append(i)
    while q:
        n = q.pop()
        for i in range(1, N + 1):
            if data[n][i] and not visited[i]:
                ans += 1
    return ans

T = int(input().replace('혻', ''))
for test_case in range(T):
    N, M = map(int, input().replace('혻', '').split())
    data = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    visited[1] = 1
    ans = 0

    for _ in range(M):
        a, b = map(int, input().replace('혻', '').split())
        data[a][b], data[b][a] = 1, 1
    print("#{} {}".format(test_case + 1, bfs()))