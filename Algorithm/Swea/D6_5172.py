import sys
sys.stdin = open("D6_5172_input.txt", "r")

T = int(input())
blue, red = [0] * 1010, [0] * 1010
for test_case in range(T):
    N = int(input())
    v = 0
    for i in range(1, N):
        data = input()
        for j in range(len(data)):
            if data[j] == '0':
                blue[i + j + 1] += 1
                blue[i] += 1
            else:
                red[i + j + 1] += 1
                red[i] += 1

    for i in range(1, N + 1):
        v += blue[i] * (blue[i] - 1) // 2
        v += red[i] * (red[i] - 1) // 2
        blue[i] = 0
        red[i] = 0
    print("#{} {}".format(test_case + 1, (v - N * (N - 1) * (N - 2) // 6) // 2))