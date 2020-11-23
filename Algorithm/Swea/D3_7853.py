import sys
sys.stdin = open("D3_7853_input.txt", "r")

mod = 1000000007
T = int(input())
for test_case in range(T):
    s = input()
    ans = 1 if s[0] == s[1] else 2

    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i] == s[i + 1]:
            ans %= mod
        elif (s[i - 1] == s[i] and s[i] != s[i + 1]) or (s[i - 1] != s[i] and s[i - 1] == s[i + 1]) or (s[i - 1] != s[i] and s[i] == s[i + 1]):
            ans = (ans * 2) % mod
        else:
            ans = (ans * 3) % mod

    if s[- 2] != s[- 1]:
        ans = (ans * 2) % mod

    print("#{} {}".format(test_case + 1, ans))