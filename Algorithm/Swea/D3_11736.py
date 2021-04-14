import sys
sys.stdin = open("D3_11736_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N - 2):
        if arr[i] < arr[i + 1] < arr[i + 2] or arr[i] > arr[i + 1] > arr[i + 2]:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))