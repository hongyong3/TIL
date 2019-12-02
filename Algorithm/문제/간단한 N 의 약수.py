import sys
sys.stdin = open("간단한 N 의 약수_input.txt", "r")

N = int(input())
ans = []
for i in range(1, N+1):
    if N % i == 0:
        ans.append(i)
print(*ans)