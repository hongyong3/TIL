import sys
sys.stdin = open("D3_16002_input.txt", "r")
def prime(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res


T = int(input())
arr = prime(10000000)
for test_case in range(T):
    N = int(input())
    if N % 2:
        y = 4
        while True:
            if y + N not in arr:
                break
            y += 2
        x = y + N
    else:
        x, y = N + 4, 4
    print("#{} {} {}".format(test_case + 1, x, y))