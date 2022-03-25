import sys
sys.stdin = open("D2_14141_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = input().split()
    print("#{}".format(test_case + 1), end = ' ')
    for i in range(int(N)):
        num10 = int(M[i], 16)
        print(format(num10, 'b').zfill(4), end='')
    print()