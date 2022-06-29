import sys
sys.stdin = open("D1_14509_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = - 1

    for i in range(N):
        ans = max(ans, sum(arr[:i]), sum(arr[i + 1:]))
    print("#{} {}".format(test_case + 1, ans))