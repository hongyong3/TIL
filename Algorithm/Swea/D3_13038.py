import sys
sys.stdin = open("D3_13038_input.txt", "r")

T = int(input())
for test_case in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    while True:
        if not arr[0]:
            arr.append(arr.pop(0))
        else:
            break
    ans = (n - 1) // sum(arr) * 7 + 1
    if n <= sum(arr):
        while n:
            for i in arr:
                if i:
                    n -= 1
    print("#{} {}".format(test_case + 1, ans))