import sys
sys.stdin = open("D3_4406_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(str, input()))
    ans, string = "", "a, e, i, o, u"
    for i in data:
        if not i in string:
            ans += i
    print("#{} {}".format(test_case + 1, ans))