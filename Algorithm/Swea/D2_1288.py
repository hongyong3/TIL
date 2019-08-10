import sys
sys.stdin = open("D2_1288_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    num, K = [], 0
    while len(num) <= 9:
        K += 1
        ans = str(K * N)
        for i in range(len(ans)):
            if ans[i] not in num:
                num.append(ans[i])
                if len(num) == 10:
                    print("#{} {}".format(test_case + 1, ans))