import sys
sys.stdin = open("D5_4701_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    rate = []
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[0][0] = 1
    size = [0, 0]

    for i in range(N):
        rate.append((A[i], 0))
        rate.append((B[i], 1))
    rate = sorted(rate, key = lambda x : x[0])

    for i in range(2 * N):
        nt = rate[i][1]
        size[nt] += 1

        for j in range(N - 1, - 1, - 1):
            for k in range(N):
                if arr[j][k]:
                    remains = size[nt ^ 1] - j

                    if remains:
                        arr[j + 1][k + (nt ^ 1)] = (arr[j + 1][k + (nt ^ 1)] + arr[j][k] * remains) % 1000000007

    print("#{}".format(test_case + 1), *arr[N])