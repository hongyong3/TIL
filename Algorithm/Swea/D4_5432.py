import sys
sys.stdin = open("D4_5432_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = str(input())
    ans, s = 0, []
    for i in range(len(data)):
        if data[i] == "(":
            s.append(data[i])
            continue
        if data[i] == ")":
            if data[i - 1] == "(":
                s.pop()
                ans += len(s)
            else:
                s.pop()
                ans += 1
    print("#{} {}".format(test_case + 1, ans))