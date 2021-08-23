import sys
sys.stdin = open("D4_10086_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    idx = 0
    while True:
        if arr[idx + K]:
            idx = K
        else:
            if arr[idx + K - 1]:
                pass
            elif arr[idx + K - 1]:
                pass