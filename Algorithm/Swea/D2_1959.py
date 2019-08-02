import sys
sys.stdin = open("D2_1959_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        ans = [0] * (M - N + 1)
        j = -1
        for k in range(len(ans)):
            sum = 0
            j += 1
            for i in range(N):
                sum += A[i] * B[i + j]
            ans[k] = sum
        print("#{} {}".format(test_case + 1, max(ans)))

    else:
        ans = [0] * (N - M + 1)
        j = -1
        for k in range(len(ans)):
            sum = 0
            j += 1
            for i in range(M):
                sum += A[i + j] * B[i]
            ans[k] = sum
        print("#{} {}".format(test_case + 1, max(ans)))