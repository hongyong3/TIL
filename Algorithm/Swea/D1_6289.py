import sys
sys.stdin = open("D1_6289_input.txt", "r")

N = str(input())
ans = 0
for i in N:
    ans += int(i)
print(ans)
print(sum(int(i) for i in N))