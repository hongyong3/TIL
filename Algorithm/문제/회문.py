import sys
sys.stdin =open("글자수_input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    data_1 = str(input())
    data_2 = str(input())
    # M = len(data_1)
    # N = len(data_2)
    # print(data_1)
    # print(data_2)
    x = {}
    for i in data_1:
        x[i] = 0
    # print(ans)

    for i in data_2:
        if i in data_1:
            x[i] += 1
    # print(x)
    # print(list(x.values()))
    ans = max(list(x.values()))
    # print(ans)

    print("#{} {}".format(test_case, ans))