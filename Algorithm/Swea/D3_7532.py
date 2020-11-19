import sys
sys.stdin = open("D3_7532_input.txt", "r")

T = int(input())
for test_case in range(T):
    S, E, M = map(int,input().split())

    while True:
        e = 24 if not S % 24 else S % 24
        m = 29 if not S % 29 else S % 29
        if e == E and m == M:
            break
        S += 365
    print("#{} {}".format(test_case + 1, S))