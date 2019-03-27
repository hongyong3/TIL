import sys
sys.stdin = open("[TST]예산_input.txt", "r")

N = int(input())
data = list(map(int, input().split()))
budget = int(input())
answer, start, end = 0, 0, max(data)

while start <= end or answer > budget:
    answer = 0
    mid = (start + end) // 2
    for i in data:
        if i < mid:
            answer += i
        else:
            answer += mid
    if answer <= budget:
        start = mid + 1
    else: end = mid - 1
print(mid)