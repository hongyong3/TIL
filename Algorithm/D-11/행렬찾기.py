def search(start, y):
    global data
    stack = []
    for i in range(2):
        new_x = start + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            if data[new_y][new_x] != 0:
                print(new_y, new_x)
                stack.append(new_y)
                stack.append(new_x)
                flag = 1
            if data[new_y][new_x] == 0:
                data[new_y][new_x] = 9
                search(new_x, new_y)
    return flag


import sys
sys.stdin = open("행렬찾기_input.txt", "r")

T = int(input())
# for test_case in range(1, T+1):
for test_case in range(1):
    N = int(input())
    # print(N)
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    dx = [0, 1]  # 하 우
    dy = [1, 0]  # 하 우
    count_dx = 0
    count_dy = 0
    for y in range(N):
        for x in range(N):
            if data[y][x] != 0:
                start_x = x
                start_y = y
                # print(start_x, start_y)

    # for y in range(N):
    #     for x in range(N):
    #         if data[start_y]
