import sys
sys.stdin = open("D3_5549_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    if N % 2:
        print("#{} {}".format(test_case + 1, "Odd"))
    else:
        print("#{} {}".format(test_case + 1, "Even"))
