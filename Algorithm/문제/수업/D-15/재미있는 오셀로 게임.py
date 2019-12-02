import sys
sys.stdin = open("재미있는 오셀로 게임_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, P = map(int, input().split())
    data = [[0 for _ in range(N+1)] for _ in range(N+1)]
    data[N // 2 + 1][N // 2], data[N // 2][N // 2 + 1] = 1, 1
    data[N // 2][N // 2], data[N // 2 + 1][N // 2 + 1] = 2, 2 # 오델로 중앙에 W, B 놓기

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]  # 상 하 좌 우 좌상 좌하 우상 우하
    for _ in range(P):
        x, y, P = map(int, input().split())
        data[x][y] = P  # 오델로 데이터 받아오기

        for i in range(8):
            new_x = x + dx[i]   # 돌 바꿔주기 위한작업
            new_y = y + dy[i]
            stack = []
            while 0 < new_x <= N and 0 < new_y <= N:
                if data[new_x][new_y] == 0:
                    break
                elif data[new_x][new_y] != P:
                    stack.append(new_x)
                    stack.append(new_y)
                elif data[new_x][new_y] == P:
                    while stack:
                        turn_y = stack.pop()
                        turn_x = stack.pop()
                        data[turn_x][turn_y] = P
                    break
                new_x += dx[i]
                new_y += dy[i]
    B = 0
    W = 0
    for x in range(N+1):
        for y in range(N+1):
            if data[x][y] == 1:
                B += 1
            elif data[x][y] == 2:
                W += 1
    print("#{} {} {}".format(test_case+1, B, W))