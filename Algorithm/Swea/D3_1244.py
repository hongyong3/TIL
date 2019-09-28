import sys
sys.stdin = open("D3_1244_input.txt", "r")

def solve(data, n, a):
    if n == N:
        return
    # for i in range(a, len(data)):
    if data[a] < max(data[a + 1:]):
        data[a].replace(data[0], max(data[a + 1:]))
        solve(data, n + 1, a + 1)
    else:
        pass

T = int(input())
for test_case in range(T):
    data, N = map(str, input().split())
    solve(data, 0, 0)

##################################################################################


def solve(ans, n, a):
    global N
    if n == int(N):
        return ans
    k = 0
    for i in range(a, len(ans)):
        if ans[i] == max(ans[a + 1:]):
            k = i
            continue
    if ans[a] < max(ans[a + 1:]):
        ans[a], ans[k] = ans[k], ans[a]
    else:
        pass
    solve(ans, n + 1, a + 1)


T = int(input())
for test_case in range(T):
    data, N = map(str, input().split())
    ans = []
    for i in data:
        ans.append(int(i))
    print(ans, N)