import sys
sys.stdin = open("D3_17642_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    if A == B:
        ans = 0
    elif B - A < 2:
        ans = - 1
    else:
        ans = (B - A) // 2
    print("#{} {}".format(test_case + 1, ans))