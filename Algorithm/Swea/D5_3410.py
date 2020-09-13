import sys
sys.stdin = open("D5_3410_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    minn = float('inf')
    wList = [0] * (N + 2)
    eList = [0] * (N + 2)
    mat = 0

    for _ in range(M):
        data = input()
        for i in range(N):
            if data[i] == 'E':
                eList[i + 1] += 1
            else:
                wList[i + 1] += 1

    for i in range(2, N + 1):
        eList[i] += eList[i - 1]
        wList[N + 1 - i] += wList[N + 2 - i]

    for i in range(N + 1):
        if minn > eList[i] + wList[i + 1]:
            minn = eList[i] + wList[i + 1]
            mat = i

    print("#{} {} {}".format(test_case + 1, mat, mat + 1))