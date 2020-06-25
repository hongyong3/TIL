import sys
sys.stdin = open("5650_input.txt", "r")

'''
- 1     : 블랙홀
0       : 빈공간
1 ~ 5   : 블록(방향전환)
        1 : (1, 3, 0, 2)
        2 : (3, 0, 1, 2)
        3 : (2, 0, 3, 1)
        4 : (1, 2, 3, 0)
        5 : (1, 0, 3, 2)
6 ~ 10  : 웜홀
'''

########################################################
wormHole = (
    'block',
    (1, 3, 0, 2),   # 1
    (3, 0, 1, 2),   # 2
    (2, 0, 3, 1),   # 3
    (1, 2, 3, 0),   # 4
    (1, 0, 3, 2),   # 5
)

dx = [- 1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, - 1, 1]

T = int(input())
for test_case in range(1):
    N = int(input())
    data = [[5] * (N + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N + 2)]
    ans = 0

    # 웜홀
    wormDict = {}
    wormStack = ['block'] * 6 + [0] * 5

    for x in range(1, N - 1):
        for y in range(1, N - 1):
            if data[x][y] in range(6, 11):
                wormStart = wormStack[data[x][y]]
                if not wormStart:
                    wormStack[data[x][y]] = (x, y)
                else:
                    wormDict[wormStart] = (x, y)
                    wormDict[(x, y)] = wormStart
    #
    # for x in range(1, N - 1):
    #     for y in range(1, N - 1):
    #         if data[x][y] == 0:
    #             for i in range(4):
    #                 cnt = 0
    #                 nx = x + dx[i]
    #                 ny = y + dy[i]
    #
    #                 while True:
    #                     if (nx, ny) == (x, y) or data[x][y] == - 1:
    #                         break
    #
    #                     elif data[x][y] in range(1, 6):
    #                         i = wormHole[data[x][y]][i]
    #                         cnt += 1
    #
    #                     elif data[x][y] in range(6, 11):
    #                         x, y = wormDict[(x, y)]
    #
    #                     nx = nx + dx[i]
    #                     ny = ny + dy[i]
    #
    #                 if ans < cnt:
    #                     ans = cnt