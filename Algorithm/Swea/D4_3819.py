import sys
sys.stdin = open("D4_3819_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    arr = [0] * N
    ans = max(data[0], 0)
    arr[0] = max(data[0], 0)
    for i in range(1, N):
        arr[i] = max(0, arr[i - 1]) + data[i]
        ans = max(ans, arr[i])
    print("#{} {}".format(test_case + 1, ans))