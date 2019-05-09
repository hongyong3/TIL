import sys
sys.stdin = open("큰 놈, 작은 놈, 같은 놈_input.txt", "r")
T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    if N > M:
        result = ">"
    elif N == M:
        result = "="
    else:
        result = "<"
    print("#{} {}".format(test_case+1, result))
