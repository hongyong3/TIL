def myprint(q):
    while q != 0:
        q = q - 1
        print("%d" % (T[q]), end = " ")
    print()

def perm(n, r, q):
    if r == 0:
        myprint(q)
    # elif n == 0:
    #     return
    else:
        for i in range(n-1, -1, -1):
            A[i], A[n - 1] = A[n - 1], A[i]
            T[r-1] = A[n-1]
            perm(n-1, r-1, q)
            A[i], A[n - 1] = A[n - 1], A[i]


A = [1, 2, 3, 4]
T = [0] * 3
perm(4, 3, 3)