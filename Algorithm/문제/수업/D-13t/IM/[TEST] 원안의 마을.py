import sys
sys.stdin = open("원안의 마을_input.txt", "r")
N = int(input())
data = [list(map(int, input())) for _ in range(N)]

ans = []
answer = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            x, y = i, j
        elif data[i][j] == 1:
            ans.append([i, j])

for k in ans:
    [i, j] = k
    d = ((i-x)**2 + (j-y)**2)**0.5
    if answer < d:
        answer = d

print(int(answer) + (answer%int(answer) > 0))