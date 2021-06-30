import sys
sys.stdin = open("D1_12148_input.txt", "r")

T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    l, r = - 1, 500000000
    while l + 1 < r:
        m = (l + r) // 2
        i, c = 0, 0
        while i < n:
            u = arr[i] + 2 * m
            while i < n and arr[i] <= u:
                i += 1
            c += 1
        if c <= k:
            r = m
        else:
            l = m
    print(r)