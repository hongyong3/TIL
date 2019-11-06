import sys
sys.stdin = open("D4_3459_input.txt", "r")

def solve(N, x):
    global answer
    if N <= x:
        return answer
    if (N >= 2 * x + 1):
        x = 2 * x + 1
        answer += 1
        solve(N, x)
    elif (N >= 2 * x):
        x = 2 * x
        answer += 1
        solve(N, x)
    elif (N < 2 * x) or (N < 2 * x + 1):
        return answer

T = int(input())
for test_case in range(1):
    N = int(input())
    ans, answer = ["Alice", "Bob"], 1
    solve(N, 1)
    print("#{} {}".format(test_case + 1, ans[answer % 2]))