import sys
sys.stdin = open("D3_16603_input.txt", "r")

T = int(input())
for _ in range(T):
    test_case = int(input())
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K %= (N - 2) * 2 + 2 * M
    rotate = []
    for i in range(M):
        rotate.append(arr[0][i])

    for i in range(1, N - 1):
        rotate.append(arr[i][- 1])
    rotate += arr[- 1][:: - 1]
    if N > 2:
        for i in range(N - 2, 0, - 1):
            rotate.append(arr[i][0])
    rotate = rotate[- K:] + rotate[: - K]


    k, x, y, idx = 0, 0, 0, 0
    while k < 4:
        if k == 0:
            if y < M:
                arr[x][y] = rotate[idx]
                idx += 1
                y += 1
            else:
                x += 1
                y -= 1
                k += 1
        elif k == 1:
            if x < N:
                arr[x][y] = rotate[idx]
                idx += 1
                x += 1
            else:
                x -= 1
                y -= 1
                k += 1
        elif k == 2:
            if y >= 0:
                arr[x][y] = rotate[idx]
                idx += 1
                y -= 1
            else:
                x -= 1
                y += 1
                k += 1
        else:
            if x >= 1:
                arr[x][y] = rotate[idx]
                idx += 1
                x -= 1
            else:
                k += 1
    print("#{}".format(test_case))
    for i in arr:
        print(*i)