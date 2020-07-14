import sys
sys.stdin = open("D3_10200_input.txt", "r")

# 545 / 1010
T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    if A + B <= N:
        ans1, ans2 = min(A, B), 0
    elif N < A + B < 2 * N:
        ans1, ans2 = min(A, B), A + B - N
    else:
        ans1 = ans2 = N
    print("#{} {} {}".format(test_case + 1, ans1, ans2))