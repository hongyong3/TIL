import sys
sys.stdin = open("D5_17301_input.txt", "r")

# Fail 4 // 20
T = int(input())
arr = [0] * 100001
for test_case in range(T):
    N = int(input())
    arrA = list(map(int, input().split()))
    Q = int(input())
    arrX = list(map(int, input().split()))

    for i in range(N):
        arr[i] = arrA[i]

    total = sum(arrA)
    idx = 0

    for x in range(N, Q):
        arr[x] = total // N
        total += arr[x] - arr[idx]
        idx += 1
    print("#{}".format(test_case + 1), *arr[:Q])