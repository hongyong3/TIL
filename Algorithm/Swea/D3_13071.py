import sys
sys.stdin = open("D3_13071_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [0] * 25
    arr.sort(key = lambda x : x[1] - x[0])

    for s, e in arr:
        if 1 not in visited[s:e]:
            for i in range(s, e):
                visited[i] = 1
            ans += 1
    print("#{} {}".format(test_case + 1, ans))