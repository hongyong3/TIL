import sys
sys.stdin = open("D4_7465_input.txt", "r")

def solve(x, y):
    global count
    if data[x][y]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    count = 0
    for i in range(len(data)):
        solve(0, 1)

    visited = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(len(data)):
        visited[data[i][0]][data[i][1]], visited[data[i][1]][data[i][0]] = 1, 1
    for i in visited:
        print(i)
    print()