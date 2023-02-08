import sys
sys.stdin = open("D4_16003_input.txt", "r")

# 50 // 117 Fail
T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    arr = []
    l = len(str(N))

    # 1, 10, 100, ...
    for i in range(l):
        arr.append(str(10 ** i) + '.png')
        ans += 1
    num = 1
    while ans <= 50:
        if N == ans:
            break
        for i in range(1, 100):
            if ans == 50 or 10 ** num * (l - 1) + i > N:
                break
            if str(num * 10 ** (l - 1) + i) + '.png' not in arr:
                arr.append(str(num * 10 ** (l - 1) + i) + '.png')
                ans += 1
        l -= 1

    print("#{}".format(test_case + 1), * sorted(arr)[:min(50, N)])
