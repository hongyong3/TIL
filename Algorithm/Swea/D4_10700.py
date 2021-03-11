import sys
sys.stdin = open("D4_10700_input.txt", "r")


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = [[0, 0, 0, 0] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    print(arr)