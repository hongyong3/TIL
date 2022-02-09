import sys
sys.stdin = open("D3_13547_input.txt", "r")

T = int(input())
for test_case in range(T):
    so = se = 0
    s = input()
    ans = "YES"
    for i in s:
        if i == 'o':
            so += 1
            if so == 8:
                ans = "YES"
                break
        else:
            se += 1
            if se == 8:
                ans = "NO"
                break
    print("#{} {}".format(test_case + 1, ans))