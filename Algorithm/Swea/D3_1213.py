import sys
sys.stdin = open("D3_1213_input.txt", "r")

for test_case in range(10):
    N = int(input())
    str1 = str(input())
    data = str(input())
    count = 0

    for i  in range(len(data) - len(str1) + 1):
        if data[i:i + len(str1)] == str1:
            count += 1
    print("#{} {}".format(test_case + 1, count))