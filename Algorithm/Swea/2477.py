import sys
sys.stdin = open("2477_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))

    A, B = A - 1, B - 1
    w1, w2 = [], []
    AA, BB = [None] * N, [None] * N
    AA_num = 0
    subAns = [0] * (K + 1)
    mat = 0
    time = 0

    idx = 1
    while t or AA_num or w2:
        while t and t[0] == time:
            t.pop(0)
            w1.append(idx)
            idx += 1

        for i in range(N):
            if AA[i]:
                AA[i][1] -= 1
                if not AA[i][1]:
                    w2.append(AA[i][0])
                    AA[i] = None
                    AA_num -= 1

            if AA[i] is None:
                if w1:
                    num = w1.pop(0)
                    AA[i] = [num, a[i]]
                    AA_num += 1
                    if i == A:
                        subAns[num] = 1

        for i in range(M):
            if BB[i]:
                BB[i][1] -= 1
                if not BB[i][1]:
                    BB[i] = None

            if BB[i] is None:
                if w2:
                    num = w2.pop(0)
                    BB[i] = [num, b[i]]
                    if i == B and subAns[num]:
                        mat += num

        time += 1

    if not mat:
        mat = - 1

    print("#{} {}".format(test_case + 1, mat))