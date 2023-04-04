import sys
sys.stdin = open("D6_11389_input.txt", "r")

# Runtime Error 1 / 26
T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    idx = 0
    if X == 0:
        if X in arr:
            pass
    else:
        cut = []
        idx = 0
        for i in range(N):
            if arr[i] == 0:
                continue
            if X % arr[i]:
                cut.append([idx, i])
                idx = i + 1
        else:
            cut.append([idx, N])