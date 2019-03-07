def check(x, y):
    dx = [0, 0, -1, 1]  # 위 아래 왼쪽 오른쪽
    dy = [-1, 1, 0, 0]  # 위 아래 왼쪽 오른쪽


import sys
sys.stdin = open("구슬 굴리기_input.txt", "r")
N, M = list(map(int, input().split()))
data = [list(map(int, input())) for _ in range(M)]
A = int(input())
ans = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            new_i, new_j = i, j
            print(new_i, new_j)
            check(new_i, new_j)