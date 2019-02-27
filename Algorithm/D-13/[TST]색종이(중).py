import sys
sys.stdin = open('색종이(중)_input.txt', 'r')
T = int(input())
count = 0
data = [[0 for _ in range(101)] for _ in range(101)]
for test_case in range(T):
    N, M = map(int, input().split())
    for i in range(N, (N + 10)):
        for j in range(M, (M + 10)):
            data[i][j] = 1
dx = [-1, 0, 1, 0] # 상 하 좌 우
dy = [0, -1, 0, 1] # 상 하 좌 우
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 1:
            for k in range(4):
                if data[i+dx[k]][j+dy[k]] == 0:
                    count += 1
print(count)
