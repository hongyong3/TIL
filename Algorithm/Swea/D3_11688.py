import sys
sys.stdin = open("D3_11688_input.txt", "r")

T = int(input())
for test_case in range(T):
    s = input()
    a, b = 1, 1
    for i in s:
        if i == 'L':
            b += a
        else:
            a += b
    print("#{} {} {}".format(test_case + 1, a, b))