import sys
sys.stdin = open("D1_14505_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += arr[i] % arr[j]
            ans += arr[j] % arr[i]
    print("#{} {}".format(test_case + 1, ans))