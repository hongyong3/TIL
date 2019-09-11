import sys
sys.stdin = open("D3_3376_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = []
    i, j = 0, 0
    while i < N:
        if i <= 2:
            ans.append(1)
        else:
            ans.append(ans[j] + ans[j + 1])
            j += 1
        i += 1
    print("#{} {}".format(test_case + 1,ans[-1]))