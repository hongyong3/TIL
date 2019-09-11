import sys
sys.stdin = open("D3_3314_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    total = 0
    for i in range(len(data)):
        if data[i] < 40:
            data[i] = 40
        total += data[i]
    print("#{} {}".format(test_case + 1, total // len(data)))