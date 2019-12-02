import sys
sys.stdin = open("더블더블_input.txt", "r")
N = int(input())
ans = []
num = 1
for i in range(N+1):
    ans.append(2**i)
print(*ans)