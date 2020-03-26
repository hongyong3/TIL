import sys
sys.stdin = open("D4_5122_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(M):
        cal = list(map(str, input().split()))
        if cal[0] == 'I':
            data.insert(int(cal[1]), int(cal[2]))
        elif cal[0] == 'D':
            data.pop(int(cal[1]))
        else:
            data[int(cal[1])] = int(cal[2])
    if len(data) - 1 >= L:
        print("#{} {}".format(test_case + 1, data[L]))
    else:
        print("#{} {}".format(test_case + 1, -1))