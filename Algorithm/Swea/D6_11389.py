import sys
sys.stdin = open("D6_11389_input.txt", "r")

# Runtime Error 1 / 26
T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    idx = 0
    while idx < N:
        if X % arr[idx]:
            idx += 1