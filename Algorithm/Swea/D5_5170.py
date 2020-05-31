import sys
sys.stdin = open("D5_5170_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted([list(map(int, input().split())) for _ in range(N)])
    arr = []
    chk = False
    for i in range(N):
        for j in range(i + 1, N):
            if (data[j][1] - data[i][1]) == 0 or (data[j][0] - data[i][0]) == 0:
                chk = True
            else:
                x = (data[j][1] - data[i][1]) / (data[j][0] - data[i][0])
                arr.append(x)
    print("#{} {}".format(test_case + 1, len(set(arr)) + chk))