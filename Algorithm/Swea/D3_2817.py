import sys
sys.stdin = open("D3_2817_input.txt", "r")

def solve(total,i):
    global count
    if total > K: return
    if total == K:
        count += 1
        return
    if i > N - 1: return
    solve(total, i + 1)
    solve(total + data[i], i + 1)
    return count

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    count = 0
    print("#{} {}".format(test_case + 1, solve(0, 0)))