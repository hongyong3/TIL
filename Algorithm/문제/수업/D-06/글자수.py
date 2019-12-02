import sys
sys.stdin =open("글자수_input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    data_1 = str(input())
    data_2 = str(input())
    x = {}
    for i in data_1:
        x[i] = 0
    print(x)
    for i in data_2:
        if i in data_1:
            x[i] += 1
    ans = max(list(x.values()))

    print("#{} {}".format(test_case, ans))