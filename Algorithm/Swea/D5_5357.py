import sys
sys.stdin = open("D5_5357_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    O = list(map(int, input().split()))
    off = 0
    mat = 0 if O[0] else 1
    for i in range(1, N):
        if O[i]:
            off = 0
        else:
            off += A[i]
            if off >= H:
                mat += 1
                off = 0
                O[i] = 1

    if N > 1 and not O[- 1]:
        mat += 1
    print("#{} {}".format(test_case + 1, mat))