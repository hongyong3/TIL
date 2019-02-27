import sys
sys.stdin = open('같은 모양 찾기_input.txt', 'r')
T = int(input())
data = [list(map(int, input())) for i in range(T)]
print(data)
X = int(input())
ans = [list(map(int, input())) for i in range(X)]
print(ans)
count = 0
# for i in range(len(data)):
#     for j in range(len(data)):