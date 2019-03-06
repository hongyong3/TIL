import sys
sys.stdin = open("줄세우기_input.txt", "r")
N = int(input())
data = list(map(int, input().split()))      # 제비번호
ans = []

for i in range(1, N+1):     # i : 학생번호
    pick = data.pop(0)      # pick : 제비번호
    if pick:
        ans = ans[:-pick] + [i] + ans[-pick:]
    else:
        ans += [i]
print(*ans)