import sys
sys.stdin = open("D5_17301_input.txt", "r")

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
    idx, jdx, cnt = 0, N, 0

    while True:
        avg = total // N
        arr[jdx] = avg
        total += arr[jdx] - arr[idx]
        nAvg = total // N
        if avg == nAvg:
            cnt += 1
        else:
            cnt = 0
        if cnt == N:
            kdx = jdx - N + 2
            break
        idx += 1
        jdx += 1

    print("#{}".format(test_case + 1), end = " ")
    for i in arrX:
        if i >= kdx:
            print(avg, end=" ")
        else:
            print(arr[i - 1], end = " ")
    print()