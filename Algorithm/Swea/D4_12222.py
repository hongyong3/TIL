import sys
sys.stdin = open("D4_12222_input.txt", "r")

T = int(input())
for test_case in range(1):
    S = input()
    lS = len(S)
    ans = 0
    a, idx = S[0], 1

    while idx < lS:
        b = S[idx]
        if a == b:
            if idx + 1 == lS:
                break
            if a == S[idx + 1]:
                a 