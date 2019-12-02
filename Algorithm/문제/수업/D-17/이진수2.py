import sys
sys.stdin = open("이진수2_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = float(input())
    ans = []
    while len(ans) <= 13:
        if N*2 >= 1:
            ans.append(1)
            N = N*2 - 1
            if len(ans) > 12:
                print("#{}".format(test_case + 1), end=" ")
                print("overflow")
        elif 0 < N*2 < 1:
            N = N*2
            ans.append(0)
            continue
            if len(ans) > 12:
                print("#{}".format(test_case+1), end= " ")
                print("overflow")
        elif N == 0:
            print("#{}".format(test_case+1), end=" ")
            for i in range(len(ans)):
                print(ans[i], end="")
            print()
            break