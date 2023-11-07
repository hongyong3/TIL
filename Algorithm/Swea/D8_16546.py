import sys
sys.stdin = open("D8_16546_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = input().strip()
    arr = [0] * 10
    for i in N:
        arr[int(i)] += 1
    for i in range(10):
        while arr[i] > 2:
            arr[i] -= 3

    for i in range(8):
        while arr[i] and arr[i + 1] and arr[i + 2]:
            arr[i] -= 1
            arr[i + 1] -= 1
            arr[i + 2] -= 1
    print("#{} {}".format(test_case + 1, 'false' if sum(arr) else 'true'))