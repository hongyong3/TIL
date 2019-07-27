import sys
sys.stdin = open("D2_1989_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input()
    reversed_data = data[::-1]
    if data == reversed_data:
        print("#{} {}".format(test_case + 1, 1))
    else:
        print("#{} {}".format(test_case + 1, 0))