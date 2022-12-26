import sys
sys.stdin = open("D1_15916_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = list(map(int, input().split()))
    maxNum, minNum, maxIdx, minIdx = -float('inf'), float('inf'), 0, 0

    for i in range(10):
        num = arr[i]
        if num > maxNum:
            maxNum = num
            maxIdx = i
        if num < minNum:
            minNum = num
            minIdx = i
    arr[maxIdx], arr[minIdx] = arr[minIdx], arr[maxIdx]
    print(f'#{test_case + 1}', *arr)
