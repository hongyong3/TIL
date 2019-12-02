def findStart(data):
    for j in range(N):
        for i in range(N):
            if data[j][i] != 0:
                y, x = j, i
    return y, x

T =int(input())
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N+1)]
G = [0 for _ in range(N)]