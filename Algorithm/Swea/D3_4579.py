import sys
sys.stdin = open("D3_4579_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = str(input())
    result = "Exist"
    for i in range(int(len(data) / 2)):
        if data[i] == "*" or data[len(data) - 1 - i] == "*": result
        elif data[i] != data[len(data) - 1 - i]:result = "Not exist"
    print("#{} {}".format(test_case + 1, result))

