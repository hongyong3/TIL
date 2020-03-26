import sys
sys.stdin = open("D4_5120_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    i = 0

    for _ in range(K):
        i += M
        if i < len(data):
            data.insert(i, data[i - 1] + data[i])
        elif i == len(data):
            data.append(data[- 1] + data[0])
        else:
            i -= len(data)
            data.insert(i, data[i - 1] + data[i])

    print("#{}".format(test_case + 1), *data[:: - 1][:10])