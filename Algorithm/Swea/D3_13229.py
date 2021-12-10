import sys
sys.stdin = open("D3_13229_input.txt", "r")

T = int(input())
arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for test_case in range(T):
    S = input()
    ans = 6 - arr.index(S)
    if ans == 0:
        ans = 7
    print("#{} {}".format(test_case + 1, ans))