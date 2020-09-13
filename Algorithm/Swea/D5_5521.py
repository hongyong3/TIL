import sys
sys.stdin = open("D5_5521_input.txt", "r")

T = int(input().replace('혻', ''))
for test_case in range(T):
    N, M = map(int, input().replace('혻', '').split())
    data = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    visited[1] = 1
    for _ in range(M):
        a, b = map(int, input().replace('혻', '').split())
        data[a].append(b)
        data[b].append(a)
        if a == 1:
            visited[b] = 1

    mat = len(data[1])
    for i in range(len(data[1])):
        for j in range(len(data[data[1][i]])):
            if not visited[data[data[1][i]][j]]:
                mat += 1
                visited[data[data[1][i]][j]] = 1

    print("#{} {}".format(test_case + 1, mat))