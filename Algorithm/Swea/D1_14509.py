import sys
sys.stdin = open("D1_14509_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    temp, ans, = 0, min(sum(arr[1:]), sum(arr[:- 1]))
    for i in range(1, N - 1):
        if sum(arr[:i]) > sum(arr[i + 1:]):
            temp = sum(arr[:i])
        elif sum(arr[:i]) < sum(arr[i + 1:]):
            temp = sum(arr[i + 1:])
        if ans > temp:
            ans = temp
    print("#{} {}".format(test_case + 1, ans))