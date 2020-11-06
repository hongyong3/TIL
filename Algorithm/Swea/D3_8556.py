import sys
sys.stdin = open("D3_8556_input.txt", "r")

T = int(input())
for test_case in range(T):
    S = input()
    k = 0
    dir = ""

    while k < len(S):
        dir = S[k] + dir
        k = k + 5 if S[k] == 'n' else k + 4

    num, den, n = 0, 1, 1  # 분자, 분모, 횟수
    num = 0 if dir[0] == 'n' else 90

    while n < len(dir):
        if dir[n] == 'n':
            num -= (90 / 2 ** n)
        else:
            num += (90 / 2 ** n)
        n += 1

    if num == int(num):
        print("#{} {}".format(test_case + 1, int(num)))
    else:
        while True:
            num *= 2
            den *= 2
            if num == int(num):
                break
        print("#{} {}/{}".format(test_case + 1, int(num), den))
