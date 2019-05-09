import sys
sys.stdin = open("p1_input.txt", "r")
T = int(input())

def BFS(x, y, count):
    Q = [(x, y, count)]
    dx = [-3, -2, 2, 3, 3, 2, -2, -3]
    dy = [2, 3, 3, 2, -2, -3, -3, -2]
    while Q:
        x, y, count = Q.pop(0)
        if x == s and y == k:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                data[nx][ny] = count
                Q.append((nx, ny, count + 1))
    return count

for test_case in range(T):
    N = int(input())
    r, c, s, k = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    print("#{} {}".format(test_case+1, BFS(r, c, 0)))