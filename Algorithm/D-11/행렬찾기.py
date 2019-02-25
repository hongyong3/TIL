# def search(start, y):
#     global data
#     stack = []
#     for i in range(2):
#         new_x = start + dx[i]
#         new_y = y + dy[i]
#         if 0 <= new_x < N and 0 <= new_y < N:
#             if data[new_y][new_x] != 0:
#                 print(new_y, new_x)
#                 stack.append(new_y)
#                 stack.append(new_x)
#                 flag = 1
#             if data[new_y][new_x] == 0:
#                 data[new_y][new_x] = 9
#                 search(new_x, new_y)
#     return flag

# dx = [0, 0, -1, 1]  # 상 하 좌 우
# dy = [-1, 1, 0, 0]  # 상 하 좌 우
# count_dx = 0
# count_dy = 0
# for y in range(N):
#     for x in range(N):
#         if data[y][x] != 0:
#             start_x = x
#             start_y = y
# print(start_x, start_y)

import sys
sys.stdin = open("행렬찾기_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    visited = [0] * N
    data = [list(map(int, input().split())) for _ in range(N)]
    save = []

    for y in range(N):
        for x in range(N):
            if data[y][x]:
                new_x = x
                new_y = y
                while data[y][new_x]:
                    new_x += 1
                    if new_x == N:
                        break
                while data[new_y][x]:
                    new_y += 1
                    if new_y == N:
                        break

                if data[new_y - 1][new_x - 1]:
                    save.append([new_y - y, new_x - x])

                for i in range(y, new_y):
                    for j in range(x, new_x):
                        data[i][j] = 0

    print(f"#{test_case} {len(save)}", end=" ")

    for i in range(len(save) - 1, 0, -1):
        for j in range(0, i):
            if save[j][0] * save[j][1] > save[j + 1][0] * save[j + 1][1]:
                save[j][0], save[j][1], save[j + 1][0], save[j + 1][1] = save[j + 1][0], save[j + 1][1], save[j][0], save[j][1]
            elif (save[j][0] * save[j][1] == save[j + 1][0] * save[j + 1][1]) and save[j][0] > save[j + 1][0]:
                save[j][0], save[j][1], save[j + 1][0], save[j + 1][1] = save[j + 1][0], save[j + 1][1], save[j][0], save[j][1]
    for i in range(len(save)):
        for j in range(2):
            print(save[i][j], end=" ")
    print()