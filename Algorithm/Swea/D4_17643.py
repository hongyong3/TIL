import sys
sys.stdin = open("D4_17643_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y = map(int, input().split())
    X, Y = abs(X), abs(Y)
    ans = "yse"
    if X % 3 and Y % 3:
        print("#{} {}".format(test_case + 1, "no"))
        continue
    if Y % 3:
        X, Y = Y, X
    if X % 3 == 2:
        ans = "no"
    arr = []
    for i in range(20):
        if max(X, Y) < 3 ** i:
            break
        arr.append(3 ** i)
    print(arr)