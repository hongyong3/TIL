import sys
sys.stdin = open("달팽이사각형_input.txt", "r")
N = int(input())
data = [[0 for _ in range(N)] for _ in range(N)]
# 방법 1
# r, c= 0, -1 # 한칸 이전에서 시작
# num = 0
# count = N   # 회전수
# while num < N**2:
#     # 오른쪽
#     for i in range(count):
#         c += 1
#         num += 1
#         data[r][c] = num
#     count -= 1
#     # 아래
#     for i in range(count):
#         r += 1
#         num += 1
#         data[r][c] = num
#     # 왼쪽
#     for i in range(count):
#         c -= 1
#         num += 1
#         data[r][c] = num
#     count -= 1
#     # 위
#     for i in range(count):
#         r -= 1
#         num += 1
#         data[r][c] = num
#
# for i in range(N):
#     for j in range(N):
#         print(data[i][j], end = " ")
#     print()

# 방법 2
r, c, i, j = 0, -1, 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(1,N**2+1):
    r += dr[j]
    c += dc[j]
    data[r][c] = i
    if i == N or i == 2*N-1 or i == 3*N-2 or data[r+dr[j]][c+dc[j]] != 0:
        if j == 3: j = 0
        else: j += 1
for i in range(N):
    for j in range(N):
        print(data[i][j], end = " ")
    print()
# for line in data:
#     print(*line)