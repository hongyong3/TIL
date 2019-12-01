import sys
sys.stdin = open("D4_1865_input.txt", "r")

def solve(n):
    global percentage, ans
    if percentage <= ans:
        return

    if n == N:
        ans = percentage
        return

    for i in range(N):
        if not visited[i]:
            if data[n][i] == 0:
                continue
            else:
                percentage *= (data[n][i] / 100)
                visited[i] = 1
                solve(n + 1)
                percentage /= (data[n][i] / 100)
                visited[i] = 0


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    percentage, ans = 1, 0
    solve(0)
    print("#{} {}".format(test_case + 1, '%.6f' % (ans * 100)))