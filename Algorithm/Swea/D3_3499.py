import sys
sys.stdin = open("D3_3499_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(str, input().split()))
    mat = []
    if N % 2 == 0:
        ans1, ans2 = data[:N // 2], data[N // 2 :]
    else:
        ans1, ans2 = data[: N // 2 + 1], data[N // 2 + 1:]
    for i in range(N//2):
        mat.append(ans1[i])
        mat.append(ans2[i])
    if N % 2 != 0:
        mat.append(ans1[-1])
    print("#{} ".format(test_case + 1), end="")
    print(*mat)