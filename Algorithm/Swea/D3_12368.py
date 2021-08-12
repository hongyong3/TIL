import sys
sys.stdin = open("D3_12368_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    ans = (A + B) % 24
    print("#{} {}".format(test_case + 1, ans))