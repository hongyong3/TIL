import sys
sys.stdin = open("D3_3307_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans, maxCount = [0] * N, 0
    for i in range(N):
        ans = data[i]
        count = ans[i]
        for j in range(i + 1, N):
            if ans > data[j]: continue
            if count + 1 <= ans[j]: continue
            ans[j] = count + 1
            if count + 1 > maxCount:
                maxCount = count + 1
    print("#{} {}".format(test_case + 1, maxCount + 1))