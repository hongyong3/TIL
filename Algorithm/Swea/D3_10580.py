import sys
sys.stdin = open("D3_10580_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted([list(map(int, input().split())) for _ in range(N)])
    ans,cnt = 0, 0

    for i in range(N):
        minVal, maxVal = min(data[i][0], data[i][1]), max(data[i][0], data[i][1])
        for j in range(N):
            if i == j:
                continue
            else:
                if minVal <= data[j][0] <= maxVal and minVal <= data[j][1] <= maxVal:
                    ans += 1
                if (minVal == data[j][0] and maxVal == data[j][1]) or (maxVal == data[j][0] and minVal == data[j][1]):
                    cnt += 1
    print("#{} {}".format(test_case + 1, ans + cnt // 2))