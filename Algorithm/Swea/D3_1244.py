import sys
sys.stdin = open("D3_1244_input.txt", "r")

def swap(data, i, j):
    numArr = [0] * numCard
    for k in range(numCard - 1, - 1, - 1):
        numArr[k] = data % 10
        data //= 10
    numArr[i], numArr[j] = numArr[j], numArr[i]
    data = 0
    for k in range(numCard):
        data = data * 10 + numArr[k]
    return data

def findMax(data, N, k):
    global ans
    for i in range(720):
        if memo[k][i] == 0:
            memo[k][i] = data
            break
        elif memo[N][i] == data:
            return

    if k == N:
        if data > ans:
            ans = data
    else:
        for i in range(numCard - 1):
            for j in range(i + 1, numCard):
                findMax(swap(data, i, j), N, k + 1)

T = int(input())
for test_case in range(T):
    memo = [[0] * 720 for _ in range(11)]
    data, N = map(int, input().split())
    numCard, ans, t = 0, 0, data
    while(t):
        t //= 10
        numCard += 1
    findMax(data, N, 0)
    print("#{} {}".format(test_case + 1, ans))