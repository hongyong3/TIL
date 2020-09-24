import sys
sys.stdin = open("D3_10761_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input().split()[1:]
    O, B, k = [], [], 1 # [k, name, distance]; 순서, name, 거리
    ODist, BDist = 1, 1
    ans = 0
    while data:
        if data[0] == 'B':
            B.append([k, data.pop(0), int(data.pop(0))])
        else:
            O.append([k, data.pop(0), int(data.pop(0))])
        k += 1
    while O or B:
        if O and B:
            if O[0][0] > B[0][0]:
                if B[0][2] > BDist:
                    BDist += 1
                elif B[0][2] == BDist:
                    B.pop(0)
                else:
                    BDist -= 1

                if O[0][2] > ODist:
                    ODist += 1
                elif O[0][2] == ODist:
                    pass
                else:
                    ODist -= 1

            else:
                if O[0][2] > ODist:
                    ODist += 1
                elif O[0][2] == ODist:
                    O.pop(0)
                else:
                    ODist -= 1

                if B[0][2] > BDist:
                    BDist += 1
                elif B[0][2] == BDist:
                    pass
                else:
                    BDist -= 1

        elif O and not B:
            if O[0][2] > ODist:
                ODist += 1
            elif O[0][2] == ODist:
                O.pop(0)
            else:
                ODist -= 1
        else:
            if B[0][2] > BDist:
                BDist += 1
            elif B[0][2] == BDist:
                B.pop(0)
            else:
                BDist -= 1
        ans += 1
    print("#{} {}".format(test_case + 1, ans))