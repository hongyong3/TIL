import sys
sys.stdin = open("D1_12890_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y, C = input().split()
    if C == '+':
        ans = int(X) + int(Y)
    elif C == '-':
        ans = int(X) - int(Y)
    elif C == '*':
        ans = int(X) * int(Y)
    else:
        ans = int(X) // int(Y)
    print("#{} {}".format(test_case + 1, ans))