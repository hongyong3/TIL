import sys
sys.stdin = open("D3_10059_input.txt", "r")

T = int(input())
for test_case in range(T):
    # N = list(map(str, input()))
    N = input()
    x, y = int(N[:2]), int(N[2:])
    ans = 'AMBIGUOUS'
    if x > 12:
        if y > 12:
            ans = 'NA'
        else:
            ans = 'YYMM'
    else:
        if y > 12:
            ans = 'MMYY'
    print("#{} {}".format(test_case + 1, ans))