import sys
sys.stdin = open("D4_5608_input.txt", "r")

T = int(input())
for test_case in range(1):
    # N = int(input())
    N = 154

    maxNum, maxCount, idx, arr = 0, 0, 1, [[0] * N, [0] * (N + 1)]

    for i in range(1, N + 1):
        if pow(i, 3) < N:
            arr[0][i] = pow(i, 3)
        else:
            break

    for i in range(1, N + 1):
        if i == arr[0][idx]:
            arr[1][i] = 1
            idx += 1
        else:
            arr[1][i] = arr[1][i - arr[0][idx - 1]] + 1

    for i in range(1, N + 1):
        if maxCount <= arr[1][i]:
            maxCount = arr[1][i]
            maxNum = i
    print("#{} {} {}".format(test_case + 1, maxNum, maxCount))
    print(arr[1])