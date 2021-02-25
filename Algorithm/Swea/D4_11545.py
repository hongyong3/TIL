import sys
sys.stdin = open("D4_11545_input.txt", "r")

dx = [0, 1, 1, - 1, 0, - 1, 1, - 1] # 우 하 우하 상 좌 우상 좌하 좌상
dy = [1, 0, 1, 0, - 1, 1, - 1, - 1]

T = int(input())
for test_case in range(T):
    data = [input() for _ in range(4)]
    ans = "aa"
    if test_case != T - 1:
        temp = input()

    for x in range(4):
        for y in range(4):
            if data[x][y] == 'X':
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
                    while 0 <= nx < 4 and 0 <= ny < 4:
                        if data[nx][ny] == 'X' or data[nx][ny] == 'T':
                            cnt += 1
                        else:
                            break
                        nx += dx[i]
                        ny += dy[i]
                        if cnt == 4:
                            ans = "X won"
                            break
            elif data[x][y] == 'Y':
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
                    while 0 <= nx < 4 and 0 <= ny < 4:
                        if data[nx][ny] == 'Y' or data[nx][ny] == 'T':
                            cnt += 1
                        else:
                            break
                        nx += dx[i]
                        ny += dy[i]
                        if cnt == 4:
                            ans = "Y won"
                            break
    print(ans)