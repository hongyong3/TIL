import sys
sys.stdin = open("2112_input.txt", "r")

def solve(curD, chemicalCnt, prevContinuum, prevMaxContinuum):
    global minChemicalCnt

    if chemicalCnt >= minChemicalCnt:
        return

    if curD == D:
        chk = True
        for i in range(W):
            if prevMaxContinuum[i] < K:
                chk = False
                break

        if chk and chemicalCnt < minChemicalCnt:
            minChemicalCnt = chemicalCnt
        return

    for i in range(2, - 1, - 1):
        chemical[curD] = i
        for j in range(W):
            cur = film[curD][j] if chemical[curD] == 2 else chemical[curD]
            prev = film[curD - 1][j] if chemical[curD - 1] == 2 else chemical[curD - 1]
            continuum[j] = prevContinuum[j] + 1 if cur == prev else 1
            if continuum[j] > prevMaxContinuum[j]:
                maxContinuum[j] = continuum[j]
            else:
                maxContinuum[j] = prevMaxContinuum[j]

        a = 0 if i == 2 else 1
        solve(curD + 1, chemicalCnt + a, continuum, maxContinuum)


T = int(input())
for test_case in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    ans = 0
    minChemicalCnt = K
    continuum = [0] * W
    maxContinuum = [0] * W
    chemical = [0] * D
    for i in range(W):
        continuum[i] = maxContinuum[i] = 1

    chemical[0] = 2
    solve(1, 0, continuum, maxContinuum)
    print(minChemicalCnt)