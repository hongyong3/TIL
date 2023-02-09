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


# 50 // 117 Fail

def solve(n):
    global ans, num, l
    if ans < 50:
        for i in range(l):
            arr.append(str((10 + n) * 10 ** i) + '.png')
            ans += 1
            if ans == 50:
                return



T = int(input())
for test_case in range(T):
    N = int(input())
    if N < 100:
        arr = [str(i) + '.png' for i in range(1, N + 1)][:min(50, N)]
    else:
        ans = l = len(str(N)) - 1
        arr = [str(10 ** i) + '.png' for i in range(l)] # 1, 10, 100, 10^(n - 1)...
        num, chk1, chk2 = 0, 0, 0   # 자릿수, 50개 chk, 최댓값 chk

        while ans <= 50:
            for i in range(10):
                x = 10 ** l + num * 10 ** (l - 1) + i
                if ans == 50:
                    chk1 = 1
                    break
                if x > N:
                    chk2 = 1
                    break
                if str(x) + '.png' not in arr:
                    arr.append(str(x) + '.png')
                    ans += 1
            else:
                num += 1
                solve(num)
                # if ans < 50:
                #     for i in range(l):
                #         arr.append(str((10 + num) * 10 ** i) + '.png')
                #         ans += 1
                #         if ans == 50:
                #             break
                continue
            if chk1:
                break
            if chk2:
                num += 1
                l -= 1
                solve(num)

    print("#{}".format(test_case + 1), * sorted(arr))
    print(len(arr))