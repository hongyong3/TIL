import sys
sys.stdin = open("D5_6782_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    while N > 2:
        temp = int(N ** 0.5)
        if temp * temp == N:
            N = temp
            ans += 1
        else:
            ans += pow(temp + 1, 2) - N
            N = pow(temp + 1, 2)
    print("#{} {}".format(test_case + 1, ans))