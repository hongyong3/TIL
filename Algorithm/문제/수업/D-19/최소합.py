import sys
sys.stdin = open("최소합_input.txt", "r")

def dfs(x, y, sum):
    global min
    ###########################
    if min <= sum:          # 가지치기
        return
    #########################
    if x == N-1 and y == N-1:
        if min > sum:
            min = sum
    else:
        if x + 1 < N:
            dfs(x+1, y, sum + data[x+1][y])
        if y + 1 < N:
            dfs(x, y + 1, sum + data[x][y + 1])

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min = 987654321
    dfs(0, 0, data[0][0])    # x, y, sum

    print("#{} {}".format(test_case + 1, min))


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