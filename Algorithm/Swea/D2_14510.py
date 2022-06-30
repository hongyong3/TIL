import sys
sys.stdin = open("D2_14510_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    high = max(arr)
    ans = 0
    for i in arr:
        ans += high - i
    print("#{} {}".format(test_case + 1, ans))