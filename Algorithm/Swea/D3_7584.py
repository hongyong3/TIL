import sys
sys.stdin = open("D3_7584_input.txt", "r")

'''
짝수
    4의 배수는 : 0  # 1)
    4의 배수가 아닌 짝수는 :  1  # 2)
홀수
    f(2n + 1) = f(n)    # 3)
'''

T = int(input())
for test_case in range(T):
    N = int(input())- 1
    while N:
        if N % 2:   # 3)
            N = (N - 1) // 2

        if not N % 4:   # 1)
            ans = 0
            break
        elif not N % 2: # 2)
            ans = 1
            break
    print("#{} {}".format(test_case + 1, ans))