import sys
sys.stdin =open("반복문자 지우기_input.txt", "r")
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