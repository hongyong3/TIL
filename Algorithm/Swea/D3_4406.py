import sys
sys.stdin = open("D3_4406_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(str, input()))
    mat, string = "", "a, e, i, o, u"
    for i in data:
        if not i in string:
            mat += i
    print("#{} {}".format(test_case + 1, mat))