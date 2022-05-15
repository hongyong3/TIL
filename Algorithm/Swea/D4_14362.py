import sys
sys.stdin = open("D4_14362_input.txt", "r")

'''
처음은 동쪽 [1, 0]
dr = [[1, 0], [0, - 1], [- 1, 0], [0, 1]]
dr = [[1, 0], [0, 1], [- 1, 0], [0, - 1]]
L : 반시계방향
    if  [1, 0]      ->  [0, - 1]    동 -> 북
        [0, - 1]    ->  [- 1, 0]    북 -> 서
        [- 1, 0]    ->  [0, 1]      서 -> 남
        [0, 1]      ->  [1, 0]      남 -> 동
R : 시계방향
'''
T = int(input())
for test_case in range(T):
    command = input()
    ans = 'oo'
    dd = 0
    dr = [[1, 0], [0, 1], [- 1, 0], [0, - 1]]
    x, y, r = 0, 0, 0
    d = 0

    for i in command:
        if i == 'S':
            x += dr[r][0]
            y += dr[r][1]
            d = abs(x ** 2 + y ** 2)
            if d < dd:
                d = dd
        elif i == 'R':
            d += 1
            if d == 4:
                d = 0
        elif i == 'C':
            d -= 1
            if d == - 1:
                d = 3