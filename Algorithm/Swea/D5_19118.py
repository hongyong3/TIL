import sys
sys.stdin = open("D5_19118_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxH = max(arr)
    ans = 0
    h = arr[0]
    for i in arr[1:]:
        if h < i:
            h = i
        else:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))