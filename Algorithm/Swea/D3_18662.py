import sys
sys.stdin = open("D3_18662_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B, C = list(map(int, input().split()))
    xa = abs(A - 2 * B + C) / 1
    xb = abs(B - (C + A) / 2)
    xc = abs(C - 2 * B + A) / 1
    print("#{} {}".format(test_case + 1, min(xa, xb, xc)))