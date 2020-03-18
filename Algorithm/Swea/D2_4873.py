import sys
sys.stdin = open("D2_4873_input.txt", "r")

# 이전 풀이
T = int(input())
for test_case in range(1, T+1):
    data = list(input())
    x = 1
    while x != len(data):
        if data[x] == data[x-1]:
            del data[x]
            del data[x-1]
            x = 0
        x += 1

    print("#{} {}".format(test_case, x))

T = int(input())
for test_case in range(T):
    data = input()
    i = 1
    while i != len(data):
        if data[i] == data[i - 1]:
            data = data[: i - 1] + data[i + 1:]
            i = 0
        i += 1
    print("#{} {}".format(test_case + 1, len(data)))