import sys
sys.stdin = open("D8_18578_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    d = arr[0]
    ans = 0
    for i in arr[1:]:
        if d > i:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))