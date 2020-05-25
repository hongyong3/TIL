import sys
sys.stdin = open("D5_5685_input.txt", "r")

def dfs(n, num):
    if arr[n][num] >= 0:
        return arr[n][num]
    if n == N - 2:
        if num == ans:
            arr[n][num] = 1
        else:
            arr[n][num] = 0
        return arr[n][num]
    s = 0
    if num + numlist[n + 1] <= 20:
        s = (s + dfs(n + 1, num + numlist[n + 1])) % 1234567891
    if num - numlist[n + 1] >= 0:
        s = (s + dfs(n + 1, num - numlist[n + 1])) % 1234567891
    arr[n][num] = s
    return arr[n][num]


T = int(input().replace('혻', ""))
for test_case in range(T):
    N = int(input().replace('혻', ""))
    arr = [[- 1] * 21 for _ in range(100)]
    data = list(map(int, input().split()))
    numlist, ans = data[: N - 1], data[- 1]
    print("#{} {}".format(test_case + 1, dfs(0, numlist[0])))