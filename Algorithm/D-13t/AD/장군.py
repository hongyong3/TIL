import sys
sys.stdin = open("장군_input.txt", "r")
def BFS(x, y, count):
    dx = [-3, -2, 2, 3, 3, 2, -2, -3]
    dy = [2, 3, 3, 2, -2, -3, -3, -2]
    Q = [(x, y, count)]
    while Q:
        x, y, count = Q.pop(0)
        if x == s-1 and y == k-1:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 9 and 0 <= ny <= 8:
                if data[nx][ny] == 0:
                    data[nx][ny] = count
                    Q.append((nx, ny, count + 1))

r, c = map(int, input().split())    # 상
s, k = map(int, input().split())    # 왕왕
data = [[0] *9 for _ in range(10)]
print(BFS(r-1, c-1, 0))
