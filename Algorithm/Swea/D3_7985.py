import sys
sys.stdin = open("D3_7985_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    k = 2 << N - 1

    for i in range(N):
        for j in range(pow(2, i)):
            idx = (k - 1) // pow(2, i + 1) + (j * pow(2, N - i))
            if i == 0:
                print("#{} {}".format(test_case + 1, data[idx]), end = "")
            else:
                print(data[idx], end=" ")
        print()