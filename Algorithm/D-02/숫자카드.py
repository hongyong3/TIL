import sys

sys.stdin = open("card_input.txt")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = input()
    count = [0] * 10
    for i in range(len(data)):
        count[int(data[i])] += 1
    max_index = 0
    max_value = 0
    for i in range(len(count)):
        if count[i] >= max_value:
            max_value = count[i]
            max_index = i
    print("#{} {} {}".format(test_case, max_index, max_value))