import sys
sys.stdin = open('p1.txt')


def iswall(y, x):
    if y < 0 or y >= N: return True
    if x < 0 or x >= N: return True
    return False


def bfs(sy, sx, ty, tx):

    dy = [-2, -3, -3, -2, 2, 3, 3, 2]
    dx = [-3, -2, 2, 3, 3, 2, -2, -3]

    queue = [(sy, sx, 0)]
    pan[sy][sx] = 2

    while queue:
        y, x, turn = queue.pop(0)
        for idx in range(8):
            ny = y + dy[idx]
            nx = x + dx[idx]
            if ny == ty and nx == tx:
                return turn + 1
            if not iswall(ny, nx) and pan[ny][nx] == 0:
                queue.append((ny, nx, turn + 1))
                pan[ny][nx] = 2
    else:
        return 0


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    sx, sy, tx, ty = map(int, input().split())
    pan[ty][tx] = 3
    print('#{} {}'.format(tc, bfs(sy, sx, ty, tx)))

