import sys
sys.stdin = open("최소합_input.txt", "r")

# def iswall(x, y, N):
#     if x < 0 or x >= N: return True
#     if y < 0 or y >= N: return True
#     return False
#
# def find(x, y, distance, N):
#     global ans
#     if distance > ans:
#         return
#
#     if x == N-1 and y == N-1:
#         distance += data[y][x]
#         if ans > distance:
#             ans = distance
#     dx = [1, 0]
#     dy = [0, 1]
#     nx, ny = x, y
#
#     for i in range(2):
#         new_x = nx + dx[i]
#         new_y = ny + dy[i]
#
#         if not iswall(ny, nx, N):
#             find(new_x, new_y, distance + data[nx][ny], N)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     ans = 1234567890
#     find(0, 0, 0, N)
#
#     print("#{} {}".format(test_case+1, ans))

def dfs(x, y, sum):
    global min
    if x == N-1 and y == N-1:
        if min > sum:
            min = sum
        # return

    else:
        dx = [1, 0]
        dy = [0, 1]

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny >= N:  # 오른쪽 벽
                continue
            elif nx >= N: # 아래 벽
                continue
            else:
                sum += data[nx][ny]
                x = nx
                y = ny
                dfs(x, y, sum)


T = int(input())
for tese_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    min = 987654321
    dfs(0, 0, data[0][0])    # x, y, sum

    print(min)