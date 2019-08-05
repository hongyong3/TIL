import sys
sys.stdin = open("D2_1954_input.txt", "r")

def solve(N):
    # 상 하 좌 우
    direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    num = 0
    direction_index = 0
    x, y = 0, -1
    array = [[0] * N for _ in range(N)]

    while num < N * N:
        dir = direction_list[direction_index]
        new_x = x + dir[0]
        new_y = y + dir[1]

        # change direction
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or array[new_x][new_y] != 0:
            direction_index += 1
            if direction_index == 4:
                direction_index = 0
        else:
            num += 1
            x, y = new_x, new_y
            array[x][y] = num
    return array

T = int(input())
for test_case in range(T):
    N = int(input())
    print("#{}".format(test_case + 1))
    result = solve(N)
    for i in result:
        print(' '.join(map(str, i)))