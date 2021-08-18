import sys
sys.stdin = open("D1_12136_input.txt", "r")

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = temp = - float('inf')
    for i in arr:
        temp = max(i, temp + i)
        ans = max(ans, temp)
    print(ans)