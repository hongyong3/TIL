import sys
sys.stdin = open("D3_9839_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = - 1
    for i in range(N):
        for j in range(i + 1, N):
            num = data[i] * data[j]

            if num > ans:
                chk = True
                temp = num
                while temp // 10:
                    if temp % 10 != (temp // 10) % 10 + 1:
                        chk = False
                        break
                    temp //= 10
                if chk:
                    ans = num
    print("#{} {}".format(test_case + 1, ans))