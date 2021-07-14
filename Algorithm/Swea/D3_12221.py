import sys
sys.stdin = open("D3_12221_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    ans = A * B
    if A > 9 or B > 9:
        ans = - 1
    print("#{} {}".format(test_case + 1, ans))