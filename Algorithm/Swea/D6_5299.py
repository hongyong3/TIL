import sys
sys.stdin = open("D6_5299_input.txt", "r")

# Bad Gate
T = int(input())
for test_case in range(T):
    N = int(input())
    mat = 0

    for b in range(2, N + 1):
        num = N % b
        x = N
        chk = 1
        while x:
            if x % b != num:
                chk = 0
                break
            x //= b
        if chk:
            mat = b
            break

    if not mat:
        for i in range(1, N + 1):
            if i * i <= N:
                if N % i:
                    continue
                x = i
                base = N // x - 1
                if base > x:
                    mat = base
        mat = N + 1
    print("#{} {}".format(test_case + 1, mat))