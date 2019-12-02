import sys
sys.stdin = open("단순 2진 암호코드_input.txt", "r")

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

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                sx = i
                sy = j
                break
    ans = []
    k = len(data[sx]) - 1

    while k >= 6:
        if data[sx][k] == 1:
            if data[sx][k - 6: k + 1] in code:
                ans.append(code.index(data[sx][k - 6:k + 1]))
                k -= 5
        k -= 1
    ans.reverse()

    if ((ans[0] + ans[2] + ans[4] + ans[6]) * 3 + ans[1] + ans[3] + ans[5] + ans[7]) % 10 == 0:
        print('#{} {}'.format(test_case+1, sum(ans)))
    else:
        print('#{} {}'.format(test_case+1, 0))