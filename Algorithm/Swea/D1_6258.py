import sys
sys.stdin = open("D1_6258_input.txt", "r")

N = int(input())
ans = {}
for i in range(1, N + 1):
    ans[i] = pow(i, 2)
print(ans)