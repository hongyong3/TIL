def search(start, y):
    global data, flag

    for i in range(4):
        new_x = start + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            if data[new_y][new_x] == 2:
                flag = 1
            if data[new_y][new_x] == 0:
                data[new_y][new_x] = 9
                search(new_x, new_y)
    return flag

import sys
sys.stdin = open("미로_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    flag = 0

    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [-1, 1, 0, 0] # 상 하 좌 우
    for y in range(N):
        for x in range(N):
            if data[y][x] == 3:
                start_x = x
                start_y = y

    print("#{} {}".format(test_case+1, search(start_x, start_y)))
    # print(f'#{test_case+1} {search(start_x, start_y)}')