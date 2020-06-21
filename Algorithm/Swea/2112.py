import sys
sys.stdin = open("2112_input.txt", "r")

def solve(curD, chemicalCnt, prevContinuum, prevMaxContinuum):
    global minChemicalCnt
    if chemicalCnt >= minChemicalCnt:
        return
    if curD == D:
        chk = True
        for i in range(W):
            if prevContinuum[i] < K:
                chk = False
                break

        if chk and chemicalCnt < minChemicalCnt:
            minChemicalCnt = chemicalCnt


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