import sys
sys.stdin = open("D1_17045_input.txt", "r")

T = int(input())
for test_case in range(T):
    a, b, c, d = map(int, input().split())
    print("#{} {}".format(test_case + 1, a * b * c * d))
    