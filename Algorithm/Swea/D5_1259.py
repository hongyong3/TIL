import sys
sys.stdin = open("D5_1259_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    mat = []

    while data:
        for i in range(N):
            if data.count(data[2 * i]) == 1:
                mat.append(data.pop(2 * i))
                mat.append(data.pop(2 * i))
                N -= 1
                break

    print("#{}".format(test_case + 1), *mat)