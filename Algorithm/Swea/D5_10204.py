import sys
sys.stdin = open("D5_10204_input.txt", "r")

# 6 / 13 rumtime error..
'''
sort를 어떻게 해야하는가...
'''
T = int(input())
for test_case in range(T):
    N = int(input())
    # data = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (- x[0], - x[1]))
    data = sorted([list(map(int, input().split())) for _ in range(N)], reverse = True)
    mat = sum([data[i][0] if not i % 2 else - data[i][1] for i in range(N)])
    # print("#{} {}".format(test_case + 1, ans))
