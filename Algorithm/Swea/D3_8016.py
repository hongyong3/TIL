import sys
sys.stdin = open("D3_8016_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans1, ans2 = 0, 0
    for i in range(N):
        ans1 += (4 * (i - 1) + 2)
        ans2 += (4 * i + 2)
    print("#{} {} {}".format(test_case + 1, ans1 + 3, ans2 - 1))