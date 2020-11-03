import sys
sys.stdin = open("D3_8840_input.txt", "r")

T = int(input())
for test_case in range(T):
    print("#{} {}".format(test_case + 1, pow(int(input()) // 2, 2)))
    # L = int(input()) // 2
    # print(pow(L // 2, 2))