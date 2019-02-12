def paper(a):
    if a < 2:
        return 1
    else:
        return paper(a-1) + 2 * paper(a-2)

import sys
sys.stdin =open("종이붙이기_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = (N//10)
    print("#{} {}".format(test_case, paper(a)))