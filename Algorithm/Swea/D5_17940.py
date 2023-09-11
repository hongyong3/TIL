import sys
sys.stdin = open("D5_17940_input.txt", "r")

# Fail 59 // 191
T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    ans = 0

    if N != B:
        if N < A + B:
            ans = - 1
        else:
            while N >= A + B:
                N -= B
                ans += N * B
            if N != B:
                ans += A * (N - A)
    print("#{} {}".format(test_case + 1, ans))