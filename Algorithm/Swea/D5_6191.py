import sys
sys.stdin = open("D5_6191_input.txt", "r")

    # 점화식 fn = 1 + N * (N - 1) // 2
# if K > f(N):
#     ans = ')('



arr = [0] * 44722
arr[1] = 1
for i in range(2, 44722):
    arr[i] = arr[i - 1] + i

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    fn = 1 + N * (N - 1) // 2

    if K > fn:
        ans = ')('
    else:
        e = 44722
        # for i in range(e):
        #     if N <= arr[i]:
        #         e = i
        #         break
        # s = arr[e] - N
        # ans = ')' * (e - s) + '(' + ')' * s + '(' * (e - 1)
    print(ans)