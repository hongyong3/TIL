import sys
sys.stdin = open("D5_10202_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A, B, C = input(), input(), input()
    ans = 0
    for i in range(N):
        arr = set()
        arr.add(A[i]), arr.add(B[i]), arr.add(C[i])
        ans += len(arr) - 1
    print("#{} {}".format(test_case + 1, ans))