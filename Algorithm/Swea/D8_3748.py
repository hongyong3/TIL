import sys
sys.stdin = open("D8_3748_input.txt", "r")

def takeover(n, m, a, b, k):
    if not n:
        return 0
    if not m:
        return 1
    if n <= 1 and a <= b:
        return 0

    if n > 1:
        x = a
        y = A[n - 1] if not k else B[n - 1]
        if x + y > b:
            k = 1 if not k else 0
            result = takeover(m, n - 1, b, x + y, k)
            if not result:
                return 1

    if a > b:
        if not k:
            result = takeover(m - 1, n, B[m - 1], a, 1)
        else:
            result = takeover(m - 1, n, A[m - 1], a, 0)
        if not result:
            return 1
    return 0


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ans = "Takeover Incorporated" if takeover(N, M, A[- 1], B[- 1], 0) else "Buyout Limited"
    print("#{} {}".format(test_case + 1, ans))