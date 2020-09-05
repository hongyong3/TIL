import sys
sys.stdin = open("D5_6111_input.txt", "r")

def solve(arr, n):
    chk = 1
    while len(arr) > 2:
        if not chk:
            break
        for i in range(len(arr) - 2):
            if n:
                if arr[i + 1] - arr[i] == arr[i + 2] - arr[i + 1] == K:
                    arr = arr[:i] + arr[i + 3:]
                    break
            else:
                if arr[i] - arr[i + 1] == arr[i + 1] - arr[i + 2] == K:
                    arr = arr[:i] + arr[i + 3:]
                    break
        else:
            chk = 0
    return len(arr)

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    print("#{} {}".format(test_case + 1, min(solve(data, 1), solve(data[::- 1], 0))))