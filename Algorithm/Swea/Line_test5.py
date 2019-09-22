import sys
sys.stdin = open("Line_test5_input.txt", "r")

def factorial(num):
    fac = 1
    for n in range(1, num+1):
        fac *= n
    return(fac)

N, M = map(int, input().split())
x, y = map(int, input().split())
data = [[0] * N for _ in range(M)]
data[x][y] = 1
ans1,ans2  = 0, 0

if x < 0 or x >= N or y < 0 or y >= M:
    print("fail")
else:
    ans1 = x + y # 최소 시간
    ans2 = factorial(x + y) // (factorial(x) * factorial(y))  # 경우의 수
    print(ans1), print(ans2)