import sys
sys.stdin = open("D5_10666_input.txt", "r")

T = int(input())
for test_case in range(T):
    a, b, c = map(int, input().split())
    bc = pow(b, c, 1000000006)
    ans = pow(a, bc, 1000000007)
    print("#{} {}".format(test_case + 1, ans))