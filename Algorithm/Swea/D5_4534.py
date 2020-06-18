import sys
sys.stdin = open("D5_4534_input.txt", "r")

def solve(n):
    end, ws, wb = 1, 1, 1
    for i in tree[n]:
        if not visited[i]:
            end = 0
            visited[i] = 1
            w, b = solve(i)
            ws *= w
            wb *= (w + b)
    if end:
        return 1, 1
    return wb, ws

T = int(input())
for test_case in range(T):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    visited[1] = 1
    for _ in range(N - 1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
    print("#{} {}".format(test_case + 1, sum(solve(1)) % 1000000007 ))