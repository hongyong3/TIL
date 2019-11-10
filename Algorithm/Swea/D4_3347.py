import sys
sys.stdin = open("D4_3347_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = [0] * N
    for i in range(M):
        for j in range(N):
            if A[j] > B[i]:
                continue
            else:
                ans[j] += 1
                break
    print("#{} {}".format(test_case + 1,ans.index(max(ans)) + 1))