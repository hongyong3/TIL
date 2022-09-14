import sys
sys.stdin = open("D3_15230_input.txt", "r")

alpha = 'abcdefghijklmnopqrstuvwxyz'
T = int(input())
for test_case in range(T):
    s = input()
    ans = 0
    for i in range(len(s)):
        if alpha[i] == s[i]:
            ans += 1
        else:
            break
    print("#{} {}".format(test_case + 1, ans))