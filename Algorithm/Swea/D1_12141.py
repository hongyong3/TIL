import sys
sys.stdin = open("D1_12141_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    l, r = 0, 100000000
    while l + 1 < r:
        m = (l + r) // 2
        if m * m <= N:
            l = m
        else:
            r = m
    if l * l + l < N:
        l += 1
    print(l)