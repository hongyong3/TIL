import sys
sys.stdin = open("D3_4751_input.txt", "r")

T = int(input())
for test_case in range(1):
    data = list(str(input()))
    count = 4 * len(data) + 1
    print(count//2)
    temp = [['.'] * count for _ in range(5)]
    for i in range(5):
        # for j in range(count // 2):
        if i <= 2:
            temp[i][(count // 2) + i//2] = "#"
        else:
            temp[i][(count // 2) - i // 2] = "#"
    for i in temp:
        print(i)
    print()