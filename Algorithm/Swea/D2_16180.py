import sys
sys.stdin = open("D2_16180_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    num = input()
    mat = [0] * 10
    maxNum = 0
    maxIndex = 0
    for i in num:
        mat[int(i)] += 1
    for k, v in enumerate(mat):
        if maxIndex <= v:
            maxIndex = v
            if maxNum < k:
                maxNum = k
    print("#{} {} {}".format(test_case + 1, maxNum, maxIndex))