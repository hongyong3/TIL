import sys
sys.stdin = open("최대수 구하기_input.txt", "r")
T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    print("#{} {}".format(test_case+1, max(data)))