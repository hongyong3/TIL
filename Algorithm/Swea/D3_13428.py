import sys
sys.stdin = open("D3_13428_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = []
    N = int(input())
    l = len(str(N))
    minNum = maxNum = N

    for i in str(N):
        arr.append(int(i))

    for i in range(l):
        for j in range(i + 1, l):
            if i == 0 and arr[j] == 0:
                continue
            arr[i], arr[j] = arr[j], arr[i]
            num, cnt = 0, l - 1
            for k in arr:
                num += k * pow(10, cnt)
                cnt -= 1
            arr[i], arr[j] = arr[j], arr[i]
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num
    print("#{} {} {}".format(test_case + 1, minNum, maxNum))