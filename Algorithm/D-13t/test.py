import sys
sys.stdin = open("[TST]예산_input.txt", "r")
N = int(input())
data = list(map(int, input().split()))
ans = int(input())
sum, count = 0, 0

for i in range(N):
    sum += data[i]
if ans >= sum:
    print(max(data))
else:

    for i in range(N):
        if data[i] <= sum // N:
            ans -= data[i]
            count += 1
    print(ans//count)