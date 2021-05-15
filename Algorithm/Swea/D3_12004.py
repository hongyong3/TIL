import sys
sys.stdin = open("D3_12004_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = "Yes"
    for i in range(1, 10):
        b = N / i
        if N // i == N / i and N / i < 10:
            break
    else:
        ans = "No"
    print("#{} {}".format(test_case + 1, ans))