import sys
sys.stdin = open("D4_17643_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y = map(int, input().split())
    X, Y = abs(X), abs(Y)
    ans = "yes"
    if X % 3 and Y % 3:
        ans = "no"
    else:
        if X > Y:
            X, Y = Y, X
        if X % 3:
            chk = 1 # chk이면 X에 1, 아니면 Y에 1

        arr = []
        num = 0

        for i in range(20):
            p = 3 ** i
            arr.append(p)
            if Y < p - num:
                arr.pop()
                break
            num += p

        idx, jdx = 0, len(arr)
        for i in range(len(arr)):
            if X < arr[i]:
                break
            idx += 1