import sys
sys.stdin = open("D4_17643_input.txt", "r")

T = int(input())
for test_case in range(T):
    X, Y = map(int, input().split())

n = 3
kp, km = 0, 0
arr = []
numArr = []
numArr2 = []
x = 0
for i in range(22):
    arr.append(n ** i)
    kp += n ** i
    km = kp - n ** i
    numArr.append(kp)
    numArr2.append(km)
print(arr)
print(numArr)
print(numArr2)