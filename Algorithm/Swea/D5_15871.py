import sys
sys.stdin = open("D5_15871_input.txt", "r")

# 101 // 151 Fail
numArr = [0, 1]
num = 1
for i in range(50):
    num *= 2
    numArr.append(num)

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = "yes"
    if N != 1:
        if arr[1] - arr[0] == 1:
            x0 = arr[0]
            chk1, ckh2 = 1, 1
            for i in arr:
                if i not in numArr:
                    chk1 = 0
                    break
            if not chk1:
                for i in range(1, N):
                    arr[i] -= x0
                    if arr[i] not in numArr:
                        ans = "no"
                        break

        else:
            
    print("#{} {}".format(test_case + 1, ans))