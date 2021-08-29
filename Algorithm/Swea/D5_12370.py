import sys
sys.stdin = open("D5_12370_input.txt", "r")

# ..?
T = int(input())
for test_case in range(T):
    N = int(input())
    A0, B0, C0 = map(int, input().split())
    A1, B1, C1 = map(int, input().split())
    ans = 0
    print("#{} {}".format(test_case + 1, ans))