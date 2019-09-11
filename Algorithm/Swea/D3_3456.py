import sys
sys.stdin = open("D3_3456_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = sorted(list(map(int, input().split())))
    if data[0] == data[2]:
        print("#{} {}".format(test_case + 1, data[0]))
    elif data[0] == data[1] and data[0] != data[2]:
        print("#{} {}".format(test_case + 1, data[2]))
    elif data[0] != data[1] and data[1] == data[2]:
        print("#{} {}".format(test_case + 1, data[0]))