import sys
sys.stdin = open("D2_4834_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    num = input()
    arr = [0] * 10
    maxNum = 0
    maxIndex = 0
    for i in num:
        arr[int(i)] += 1
    for k, v in enumerate(arr):
        if maxIndex <= v:
            maxIndex = v
            if maxNum < k:
                maxNum = k
    print("#{} {} {}".format(test_case + 1, maxNum, maxIndex))