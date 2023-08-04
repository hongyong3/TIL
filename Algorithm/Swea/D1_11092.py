import sys
sys.stdin = open("D1_11092_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    minIdx, maxIdx = 0, 0
    for i in range(N):
        if arr[i] >= arr[maxIdx]:
            maxIdx = i
        if arr[i] < arr[minIdx]:
            minIdx = i
    print("#{} {}".format(test_case + 1, abs(minIdx - maxIdx)))