import sys
sys.stdin = open("D3_4299_input.txt", "r")

T = int(input())
for test_case in range(T):
    D, H, M = map(int, input().split())
    if D == 11:
        if H < 11: print("#{} {}".format(test_case + 1, -1))
        elif H == 11 and M < 11: print("#{} {}".format(test_case + 1, -1))
        elif H == 11 and M >= 11: print("#{} {}".format(test_case + 1, M - 11))
    else:
        print("#{} {}".format(test_case + 1, ((D - 11) * 24 * 60 ) + ((H - 11) * 60 ) + M -  11))