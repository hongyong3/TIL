import sys
sys.stdin = open("D3_1289_input.txt", "r")

def solve(ans, n):
    global count
    if ans == data:
        return count
    for i in range(n, len(data)):
        if ans[i] != data[i]:
            if ans[i] == 1:
                ans[i:] = 0
            else:
                ans[i:] = 1
            count += 1
            solve(data, i)

T = int(input())
for test_case in range(T):
    data = list(map(str, input()))
    ans, count = [0] * len(data), 0
    solve(ans, 0)