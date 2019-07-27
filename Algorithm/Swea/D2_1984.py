import sys
sys.stdin = open("D2_1984_input.txt", "r")

T = int(input())
for test_case in range(T):
    sum, avg = 0, 0
    data = sorted(list(map(int, input().split())))
    data.pop(0), data.pop(-1)
    for i in range(len(data)):
        sum += data[i]
        avg = sum / 8
    print("#{} {}".format(test_case + 1, int(round(avg))))