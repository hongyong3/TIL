import sys
sys.stdin = open("D3_5110_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(M - 1):
        temp = list(map(int, input().split()))
        for i in range(len(data)):
            if data[i] > temp[0]:
                data[i:i] += temp
                break
        else:
            data += temp
    print("#{}".format(test_case + 1), *data[- 10:][:: - 1])