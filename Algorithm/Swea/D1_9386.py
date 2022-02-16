import sys
sys.stdin = open("D1_9386_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    s = input()
    ans = 0
    temp = 0
    for i in s:
        if i == '1':
            temp += 1
        else:
            if ans < temp:
                ans = temp
                temp = 0
    if ans < temp:
        ans = temp
    print("#{} {}".format(test_case + 1, ans))