import sys
sys.stdin = open("재미있는 오셀로 게임_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, P = list(map(int, input().split()))
    data = [[0 for _ in range(N+1)] for _ in range(N+1)]
    data[N//2][N//2+1], data[N//2+1][N//2], data[N//2+1][N//2+1], data[N//2][N//2] = 1, 1, 2, 2
    for j in range(P):
        x, y, P = list(map(int, input().split()))

        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, -1, 1, 1]    # 상 하 좌 우 좌상 좌하 우상 우하

        for h in range(8):
            for n in range(1, N+1):
                new_x = x + dx[h] + n
                new_y = y + dy[h] + n


        for i in range(P):
            if i % 2 == 0:
                data[x][y] = P
            else:
                data[x][y] = P
for i in data:
    print(*i)