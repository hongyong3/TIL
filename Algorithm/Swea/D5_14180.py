import sys
sys.stdin = open("D5_14180_input.txt", "r")

# 118 / 139
T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(set(list(map(int, input().split()))))
    evenCnt = 0
    for i in arr:
        if not i % 2:
            evenCnt += 1
    if not evenCnt and len(arr) < 3:
        print("#{} {}".format(test_case + 1, 'no'))
    else:
        chk = False
        for i in range(len(arr)):
            if chk:
                break
            n1 = arr[i]
            for j in range(i + 1, len(arr)):
                if chk:
                    break
                n2 = arr[j]
                for k in range(j + 1, len(arr)):
                    n3 = arr[k]
                    if n1 & n2 and n1 & n3 and n2 & n3 and not n1 & n2 & n3:
                        chk = True
                        break
        if chk:
            print("#{} {}".format(test_case + 1, 'yes'))
        else:
            print("#{} {}".format(test_case + 1, 'no'))