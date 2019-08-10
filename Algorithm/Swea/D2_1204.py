import sys
sys.stdin = open("D2_1204_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    num = [0] * 101
    max, max_index = 0, 0
    for i in data:
        num[i] += 1
    for i in range(len(num)):
        if num[i] > max or max == num[i]:
            max, max_index = num[i],i
    print("#{} {}".format(test_case + 1, max_index))