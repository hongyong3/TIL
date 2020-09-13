import sys
sys.stdin = open("D3_1240_input.txt", "r")

T = int(input())
code = [[0, 0, 0, 1, 1, 0, 1],  # 0
        [0, 0, 1, 1, 0, 0, 1],  # 1
        [0, 0, 1, 0, 0, 1, 1],  # 2
        [0, 1, 1, 1, 1, 0, 1],  # 3
        [0, 1, 0, 0, 0, 1, 1],  # 4
        [0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 1, 0, 1, 1, 1, 1],  # 6
        [0, 1, 1, 1, 0, 1, 1],  # 7
        [0, 1, 1, 0, 1, 1, 1],  # 8
        [0, 0, 0, 1, 0, 1, 1]]  # 9

for test_case in range(T):
    N, M = list(map(int, input().split()))
    data = [list(map(int, input())) for _ in range(N)]
    mat, k = [], M - 1
    for i in range(N):
        if 1 in data[i]:
            x = i
            break

    while k >= 6:
        if data[x][k] == 1:
            if data[x][k - 6: k + 1] in code:
                mat.append(code.index(data[x][k - 6: k + 1]))
                k -= 5
        k -= 1
    mat.reverse()

    if ((mat[0] + mat[2] + mat[4] + mat[6]) * 3 + mat[1] + mat[3] + mat[5] + mat[7]) % 10 == 0:
        print('#{} {}'.format(test_case + 1, sum(mat)))
    else:
        print('#{} {}'.format(test_case + 1, 0))