import sys
sys.stdin = open("D2_2357_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N = input()
#     ans = "Yes" if '9' in input() else "No"
#     print("#{} {}".format(test_case + 1, ans))

for test_case in range(int(input())):
    print("#{} {}".format(test_case + 1, "Yes" if '9' in input() else "No"))