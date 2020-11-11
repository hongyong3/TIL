import sys
sys.stdin = open("D3_6718_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    if N < 100:
        ans = 0
    elif N < 1000:
        ans = 1
    elif N < 10000:
        ans = 2
    elif N < 100000:
        ans = 3
    elif N < 1000000:
        ans = 4
    else:
        ans =5
    print("#{} {}".format(test_case + 1, ans))