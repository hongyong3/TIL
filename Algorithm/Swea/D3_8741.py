import sys
sys.stdin = open("D3_8741_input.txt", "r")

T = int(input())
for test_case in range(T):
    a, b, c = input().upper().split()
    print("#{} {}".format(test_case + 1, a[0] + b[0] + c[0]))