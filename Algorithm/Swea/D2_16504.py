import sys
sys.stdin = open("D2_16504_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            if arr[i] > arr[j]:
                cnt += 1
        ans = max(ans, cnt)
    print("#{} {}".format(test_case + 1,ans))