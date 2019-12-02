import sys
sys.stdin =open("거꾸로 출력해 보아요_input.txt", "r")

N = int(input())
ans = [] * N
for i in range(N+1):
    ans.append(i)
ans.reverse()
print(*ans)