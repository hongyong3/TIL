import sys
sys.stdin = open("D5_1814_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    line = list(map(int, input().split()))
    row = list(map(int, input().split()))
    ans = 'Yes'
    if (line.count(N) and line.count(0)) or (line.count(0) and line.count(N)):
        ans = 'No'
    else:
        pass
    print("#{} {}".format(test_case + 1, ans))