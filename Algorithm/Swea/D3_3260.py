import sys
sys.stdin = open("D3_3260_input.txt", "r")

T = int(input())
for test_case in range(T):
    num1, num2 = map(int, input().split())
    # ans = num1 + num2
    print("#{} {}".format(test_case + 1, num1 + num2))