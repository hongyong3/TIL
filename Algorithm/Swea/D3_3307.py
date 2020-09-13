import sys
sys.stdin = open("D3_3307_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    cnt, maxCount = [0] * N, 0
    for i in range(N):
        mat = data[i]
        count = cnt[i]
        for j in range(i + 1, N):
            if mat > data[j]: continue
            if count + 1 <= cnt[j]: continue
            cnt[j] = count + 1
            if count + 1 > maxCount:
                maxCount = count + 1
    print("#{} {}".format(test_case + 1, maxCount + 1))