import sys
sys.stdin = open("D3_4522_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = str(input())
    result = "Exist"
    for i in range(len(data) // 2):
        if data[i] == "?" or data[len(data) - 1 - i] == "?":
            continue
        elif data[i] != data[len(data) - 1 - i]:
            result = "Not Exist"
    print("#{} {}".format(test_case + 1, result))