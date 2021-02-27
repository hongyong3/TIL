import sys
sys.stdin = open("D4_11545_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = [input() for _ in range(4)]
    total = 0
    if test_case != T - 1:
        temp = input()

    for x in range(4):
        for y in range(4):
            if data[x][y] != '.':
                total += 1

    k = 0
    while k < 4:
        OGcnt, OScnt, XGcnt, XScnt, OCcnt1, OCcnt2, XCcnt1, XCcnt2 = 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(4):
            if data[k][i] in 'OT':
                OGcnt += 1
            if data[k][i] in 'XT':
                XGcnt += 1
            if data[i][k] in 'OT':
                OScnt += 1
            if data[i][k] in 'XT':
                XScnt += 1
            if data[i][i] in 'OT':
                OCcnt1 += 1
            if data[i][i] in 'XT':
                XCcnt1 += 1
            if data[3 - i][i] in 'OT':
                OCcnt2 += 1
            if data[3 - i][i] in 'XT':
                XCcnt2 += 1

        if OGcnt == 4 or OScnt == 4 or OCcnt1 == 4 or OCcnt2 == 4:
            print("#{} O won".format(test_case + 1))
            break
        if XGcnt == 4 or XScnt == 4 or XCcnt1 == 4 or XCcnt2 == 4:
            print("#{} X won".format(test_case + 1))
            break
        k += 1

    if k == 4:
        if total == 16:
            print("#{} Draw".format(test_case + 1))
        else:
            print("#{} Game has not completed".format(test_case + 1))