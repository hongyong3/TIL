import sys
sys.stdin = open("Ladder2_input.txt", "r")

def ladder(y, x):
    global flag, M, visited, count
    data[y][x] = 9
    dy = [1, 0, 0]  # 아래, 왼쪽, 오른쪽
    dx = [0, -1, 1] # 아래, 왼쪽, 오른쪽
    for i in range(3):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y == M:
            continue
        if new_x < 0 or new_x == M:
            continue
        if data[new_y][new_x] == 9:
            continue
        if data[new_y][new_x] == 1:
            continue
        if new_y == 99:
            flag = 1
            break
        count += 1
        print(count)
        return ladder(new_y, new_x)

def findStart(data):
    for j in range(M):
        for i in range(M):
            if data[j][i] == 1:
                y, x = j, i
            return y, x


for test_case in range(1):
    N = int(input())
    M = 100
    count = 0
    data = [list(map(int, input().split())) for _ in range(M)]
    flag = 0
    visited = [0 for _ in range(M)]
    start_y, start_x = findStart(data)
    ladder(start_y, start_x)