import sys
sys.stdin = open("D3_10570_input.txt", "r")


T = int(input())
num = [1, 4, 9, 121, 484]   # 1 : 1, 2: 4, 3 : 9, 11 : 121, 22 : 484
for test_case in range(T):
    A, B = map(int, input().split())
    ans = 0
    for i in num:
        if A <= i <= B:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))