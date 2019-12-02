import sys
sys.stdin = open('표준 입출력 방법_input.txt', 'r')
N = int(input())
print(N)
T, M = map(int, input().split())
print(T, M)
data = [list(map(int, input())) for _ in range(T)]
for i in range(T):
    for j in range(M):
        print(data[i][j], end="")
    print()