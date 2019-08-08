import sys
sys.stdin = open("D2_1945_input.txt", "r")

T = int(input())
num = [2, 3, 5, 7, 11]
for test_case in range(T):
    N = int(input())
    ans = [0, 0, 0, 0, 0]
    j = 4
    for i in range(N):
        while j >= 0:
            if N % num[j] == 0:
                N = int(N / num[j])
                ans[j] += 1
            else:
                j -= 1
    print("#{} ".format(test_case + 1), end="")
    print(*ans)