import sys
sys.stdin = open("D4_16003_input.txt", "r")

'''
<1>
1, 10, 100, ..... 즉 10^0, 10^1, 10^2 , .... 10^n 
<2>
10^n + 1 ~ 10^n + 9
<3>
11
<4>
10^n + 10^(n-1) + 1 ~ 10^n + 10^(n-1) + 9
'''

T = int(input())
for test_case in range(T):
    N = int(input())
    l = len(str(N))
    if N < 143:
        arr = sorted([str(i) + '.png' for i in range(1, N + 1)])[:min(50, N)]
    else:
        arr = []
        for i in range(l):
            x = 10 ** i
            arr.append(str(x) + '.png')
        cnt = len(arr)
        if cnt < 50:
            for i in range(x + 1, N + 1):
                arr.append(str(i) + '.png')
                if cnt == 50:
                    break

    print("#{}".format(test_case + 1), *arr)