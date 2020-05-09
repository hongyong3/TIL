import sys
sys.stdin = open("4013_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(N)]
    for i in rotation:
        idx, rot = i[0], i[1]
        idx -= 1
        move = [(idx, rot)]

        temp = rot
        for i in range(idx - 1, - 1, - 1):
            if data[i][2] != data[i + 1][6]:
                temp *= - 1
                move.append((i, temp))

            else:
                break

        temp = rot
        for i in range(idx + 1, 4):
            if data[i][6] != data[i - 1][2]:
                temp *= - 1
                move.append((i, temp))

            else:
                break

        for idx, rot in move:
            if rot == 1:
                data[idx] = [data[idx].pop()] + data[idx]
            elif rot == -1:
                data[idx].append(data[idx].pop(0))

    score = data[0][0] + data[1][0] * 2 + data[2][0] * 4 + data[3][0] * 8

    print('#{} {}'.format(test_case + 1, score))