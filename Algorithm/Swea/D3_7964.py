import sys
sys.stdin = open("D3_7964_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    ans, idx = 0, 0

    while idx + M <= N:
        if data[idx]:
            for i in range(idx + 1, idx + M):
                if data[i]:
                    idx = i
            idx += M
        else:
            data[idx] = 1
            idx += M
            ans += 1
    print("#{} {}".format(test_case + 1, ans))