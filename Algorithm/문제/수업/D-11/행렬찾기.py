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

                while data[y][new_x]:   # 부분 행렬을 찾기
                    new_x += 1           # 행에 대해서
                    if new_x == N:
                        break

                while data[new_y][x]:   # 열에 대해서
                    new_y += 1
                    if new_y == N:
                        break

                if data[new_y - 1][new_x - 1]:  # 찾은 부분 행렬을 save에 append 해준다.
                    save.append([new_y - y, new_x - x])

                for i in range(y, new_y):        # 찾은 부분 행렬의 요소를 0으로 바꾼다.
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