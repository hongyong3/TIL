import sys
sys.stdin = open("D3_9997_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    print("#{} {} {}".format(test_case + 1, N * 2 // 60, N * 2 % 60))