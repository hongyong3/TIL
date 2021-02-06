import sys
sys.stdin = open("D4_10947_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    print("#{} {}".format(test_case + 1, ans))