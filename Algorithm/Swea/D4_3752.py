import sys
sys.stdin = open("D4_3752_input.txt", "r")

def recursion(l1, l2, arr):
    arr.append(l1)
    for i, x in enumerate(l2):
        recursion(l1 + [x], l2[i+1:], arr)

def combination(l):
    result = []

    recursion([], l, result)
    return result[1:]

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print(combination(data))