import sys
sys.stdin = open("D1_14553_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))[:: - 1]
    ans = 0
    if N != 1:
        while True:
            arr[0] -= 1
            arr[1] -= 1
            arr = sorted(arr)[:: - 1]
            ans += 1
            if arr[1] == 0:
                break
    print("#{} {}".format(test_case + 1, ans))