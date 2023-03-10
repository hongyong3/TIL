import sys
sys.stdin = open("D4_16801_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arrA = sorted(list(map(int, input().split())))
    arrF = sorted(list(map(int, input().split())))[::- 1]
    arr = []
    arrIdx = []
    for i in range(N):
        arr.append(arrA[i] * arrF[i])
        # arr.append([arrA[i], arrF[i], arrA[i] * arrF[i]])