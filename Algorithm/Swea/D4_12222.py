import sys
sys.stdin = open("D4_12222_input.txt", "r")

T = int(input())
# dp = [0] * 200001
for test_case in range(T):
    S = input()
    s, n = 0, len(S)    # 시작, 문자열길이
    ans, i = 1, 1
    a = S[s]

    while s < n:
        b = S[s + i]
        if a == b:
            i += 1
        else:
            s += i
            i = 1
            a = b
            ans += 1