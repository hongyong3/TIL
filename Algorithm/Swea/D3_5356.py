import sys
sys.stdin = open("D3_5356_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = [list(map(str, input())) for _ in range(5)]
    temp = [[] * 5 for _ in range(15)]
    print("#{} ".format(test_case + 1), end="")
    for i in range(5):
        for j in range(len(data[i])):
            temp[j].append(data[i][j])
    for i in range(len(temp)):
        print(''.join(temp[i]), end="")
    print()