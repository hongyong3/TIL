import sys
sys.stdin = open('같은 모양 찾기_input.txt', 'r')

T = int(input())
data = [list(map(int, input())) for _ in range(T)]
X = int(input())
ans = [list(map(int, input())) for _ in range(X)]
answer = 0

# 기본 모양
for i in range(T-X+1):
    for j in range(T-X+1):
        count = 0
        for x in range(X):
            for y in range(X):
                if data[i+x][j+y] == ans[x][y]:
                    count += 1
        if count == X * X:
            answer += 1

# 90도 회전 모양
ans_90 = [[0]*X for _ in range(X)]
for i in range(X):
    for j in range(X):
        ans_90[j][X-i-1] = ans[i][j]

for i in range(T-X+1):
    for j in range(T-X+1):
        count = 0
        for x in range(X):
            for y in range(X):
                if data[i+x][j+y] == ans_90[x][y]:
                    count += 1
        if count == X*X:
            answer += 1

# 180도 회전 모양
ans_180 = [[0]*X for _ in range(X)]
for i in range(X):
    for j in range(X):
        ans_180[X-1-i][X-1-j] = ans[i][j]

for i in range(T-X+1):
    for j in range(T-X+1):
        count = 0
        for x in range(X):
            for y in range(X):
                if data[i+x][j+y] == ans_180[x][y]:
                    count += 1
        if count == X*X:
            answer += 1

# 270도 회전 모양
ans_270 = [[0]*X for _ in range(X)]
for i in range(X):
    for j in range(X):
        ans_270[X-1-j][i] = ans[i][j]

for i in range(T-X+1):
    for j in range(T-X+1):
        count = 0
        for x in range(X):
            for y in range(X):
                if data[i+x][j+y] == ans_270[x][y]:
                    count += 1
        if count == X*X:
            answer += 1

print(answer)