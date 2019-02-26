import sys
sys.stdin = open("행렬찾기_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    visited = [0] * N
    data = [list(map(int, input().split())) for _ in range(N)]
    save = []
    print(data)

    for y in range(N):
        for x in range(N):
            if data[y][x]:
                new_x = x
                new_y = y

                # 부분 행렬을 찾기
                # 행에 대해서
                while data[y][new_x]:
                    new_x += 1
                    if new_x == N:
                        break

                # 열에 대해서
                while data[new_y][x]:
                    new_y += 1
                    if new_y == N:
                        break

                # 찾은 부분 행렬을 save에 append 해준다.
                if data[new_y - 1][new_x - 1]:
                    save.append([new_y - y, new_x - x])

                # 찾은 부분 행렬의 요소를 0으로 바꾼다.
                for i in range(y, new_y):
                    for j in range(x, new_x):
                        data[i][j] = 0
    # save.sort()
    # print(save)

    # print(f"#{test_case} {len(save)} ")
    # 1 2 2 1 1 4
    # 2 4 1 2 5 1 2 4 4 3
    # 3 6 1 2 2 3 8 1 3 7 5 8 9 5
    # 4 10 1 8 2 5 11 1 12 2 5 6 8 4 6 9 4 15 9 10 10 11
    # 5 8 1 6 10 2 2 15 6 11 7 14 11 10 17 7 15 17
    # 6 10 1 10 16 1 7 4 4 18 11 7 6 16 18 6 12 11 15 12 13 15
    # 7 13 1 13 6 3 19 1 3 12 8 6 12 4 4 14 7 11 15 8 14 10 11 15 10 19 13 20
    # 8 15 2 1 3 4 1 22 4 13 8 9 25 3 12 8 9 11 10 17 15 12 13 15 11 18 22 10 18 23 17 25
    # 9 18 8 2 3 7 4 10 15 3 9 6 14 4 11 8 7 16 6 21 16 9 10 17 21 14 27 11 17 18 18 20 26 15 20 23 23 27
    # 10 20 2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 12 14 21 8 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30