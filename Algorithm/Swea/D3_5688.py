import sys
sys.stdin = open("D3_5688_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A = N**(1/3)
    B = int(N**(1/3))
    if N**(1/3) == int(N**(1/3)):
        ans = int(N**(1/3))
    elif N**(1/3) >= int(N**(1/3)):
        ans = int(N**(1/3)) + 1
    for i in range(ans, ans + 1):
        if i**3 == N:
            print("#{} {}".format(test_case + 1, i))
        else:
            print("#{} {}".format(test_case + 1, -1))