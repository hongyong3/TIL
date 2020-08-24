import sys
sys.stdin = open("D4_3819_input.txt", "r")

T = int(input())
A = [0] * 200001
for test_case in range(T):
    N = int(input())
    A[0] = int(input())
    ans = A[0]
    for i in range(1, N):
        num = int(input())
        A[i] = num
        if A[i - 1] + A[i] > A[i]:
            A[i] = A[i - 1] + A[i]
        if ans < A[i]:
            ans = A[i]
    print("#{} {}".format(test_case + 1, ans))