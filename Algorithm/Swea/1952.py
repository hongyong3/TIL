import sys
sys.stdin = open("1952_input.txt", "r")

def dfs(i, total):
    global cost
    if i >= 12:
        cost = min(cost, total)
        return
    if use[i] == 0:
        dfs(i + 1, total)
    else:
        dfs(i + 1, total + (use[i] * D1))
        dfs(i + 1, total + M1)
        dfs(i + 3, total + M3)

T = int(input())
for test_case in range(T):
    D1, M1, M3, Y = map(int, input().split())
    use = list(map(int, input().split()))
    cost = Y
    dfs(0, 0)
    print("#{} {}".format(test_case + 1, cost))