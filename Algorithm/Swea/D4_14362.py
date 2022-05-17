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
dx = [1, 0, - 1, 0]
dy = [0, - 1, 0, 1]
T = int(input())
for test_case in range(T):
    command = input()
    ans = 'oo'
    distance = 0

    x, y, r = 0, 0, 0
    d = 0

    for i in command:
        if i == 'S':
            x += dx[r]
            y += dy[r]
            distance = abs(x ** 2 + y ** 2)
            if d < distance:
                d = distance
        elif i == 'R':
            r = (r + 1) % 4
        elif i == 'L':
            r = (r - 1) % 4
    # print(x, y)
    print(d)