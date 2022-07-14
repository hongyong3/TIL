import sys
sys.stdin = open("D3_14555_input.txt", "r")

T = int(input())
for test_case in range(T):
    S = list(input())
    ans = 0
    idx = 0
    while idx < len(S):
        if S[idx] == '(':
            ans += 1
            idx += 1
        elif S[idx] == ')':
            ans += 1
        idx += 1
    print("#{} {}".format(test_case + 1, ans))