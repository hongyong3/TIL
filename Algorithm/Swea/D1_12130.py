import sys
sys.stdin = open("D1_12130_input.txt", "r")

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    ans = 0
    total = 0
    for i in range(n):
        total = data[i]
        if total == k:
            ans += 1
        for j in range(i + 1, n):
            total += data[j]
            if total == k:
                ans += 1
    print(ans)