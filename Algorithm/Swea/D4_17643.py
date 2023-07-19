import sys
sys.stdin = open("D4_17643_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y = map(int, input().split())
    X, Y = abs(X), abs(Y)
    ans = "yes"
    if X % 3 and Y % 3:
        print("#{} {}".format(test_case + 1, "no"))
        continue

    if X > Y:
        X, Y = Y, X

    if X % 3:
        chk = 1 # chk이면 X에 1이 , 아니면 Y에 1이

    arr = []
    for i in range(20):
        arr.append(3 ** i)
        if max(X, Y) <= 3 ** i:
            if 3 ** i not in arr:
                arr.append(3 ** i)
            break

    idx, jdx = 0, len(arr)
    for i in range(len(arr)):
        if X < arr[i]:
            break
        idx += 1


    print(arr)
    print(idx, jdx)
    print(arr[:idx], arr[idx:jdx])
    print()