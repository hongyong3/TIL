import sys
sys.stdin = open("D5_7230_input.txt", "r")

def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            temp = [i for i in arr]
            temp.remove(arr[i])
            for p in perm(temp, n - 1):
                result.append([arr[i]] + p)
    return result

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    K = int(input())
    arr = []
    print(len(perm(data, N)))