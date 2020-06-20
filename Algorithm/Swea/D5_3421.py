import sys
sys.stdin = open("D5_3421_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans = 1
    menu = set()
    for _ in range(M):
        a, b = map(int, input().split())
        k = pow(2, a - 1) + pow(2, b - 1)   # 2진수 표현
        menu.add(k)

    for i in range(1, pow(2, N)):
        for m in menu:
            if i & m == m:
                break
        else:
            ans += 1
            
    print("#{} {}".format(test_case + 1, ans))