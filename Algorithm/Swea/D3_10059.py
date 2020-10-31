import sys
sys.stdin = open("D3_10059_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = input()
    x, y = int(N[:2]), int(N[2:])

    if 0 < x < 13 and 0 < y < 13:
        ans = "AMBIGUOUS"
    elif 0 < x < 13 and not (0 < y < 13):
        ans = "MMYY"
    elif not (0 < x < 13) and 0 < y < 13:
        ans = "YYMM"
    else:
        ans = "NA"
    print("#{} {}".format(test_case + 1, ans))