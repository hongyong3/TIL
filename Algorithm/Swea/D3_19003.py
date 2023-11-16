import sys
sys.stdin = open("D3_19003_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans, chk, arr = 0, 0, []
    for _ in range(N):
        S = input()
        if S == S[:: - 1]:
            chk = 1
        else:
            arr.append(S)

    for _ in range(len(arr)):
        s = arr.pop()
        if s[:: - 1] in arr:
            ans += M * 2

    if chk:
        ans += M
    print("#{} {}".format(test_case + 1, ans))