import sys
sys.stdin = open("D6_1260_input.txt", "r")

def solve(x, y):
    global ans
    dx, dy = 0, 0
    while x + dx < N and data[x + dx][y]:
        dx += 1
    while y + dy < N and data[x][y + dy]:
        dy += 1

    ans.append((x + dx, y + dy))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                solve(i, j)
    print(ans)