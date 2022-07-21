import sys
sys.stdin = open("D1_14538_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    ans = 0
    arr = [0] * 1000001
    for i in range(1, N + 1):
        arr[num[i - 1]] += i

    for i in range(1, M + 1):
        x = int(input())
        ans += arr[x]
    print("#{} {}".format(test_case + 1, ans))