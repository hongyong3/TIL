import sys
sys.stdin = open('배열정리.txt', 'r')
Y, X = map(int, input().split())
data = [list(map(int, input().split())) for i in range(Y)]
print(data)

for x in range(Y):
    for y in range(1, X):
        if data[x][y] == 1:
            data[x][y] = data[x][y-1]+1
for i in range(len(data)):
    print(*data[i])