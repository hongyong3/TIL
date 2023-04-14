import sys
sys.stdin = open("D1_17206_input.txt", "r")

T = int(input())
for test_case in range(T):
    s = input()
    ans = "YES"
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            ans = "NO"
            break
    if cnt != 0:
        ans = "NO"
    print("#{} {}".format(test_case + 1, ans))