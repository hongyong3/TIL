import sys
sys.stdin = open("D3_4676_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(str(input()))
    H = int(input())
    L = sorted(list(map(int, input().split())))
    sum = 0
    for i in range(H):
        data[L[i] + sum : L[i] + sum] += "-"
        sum += 1
    print("#{} {}".format(test_case + 1, "".join(data)))