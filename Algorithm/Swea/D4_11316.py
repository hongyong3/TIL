import sys
sys.stdin = open("D4_11316_input.txt", "r")

T = int(input())
for test_case in range(T):
    s, p, q, m = map(int, input().split())

    A, chk = [s], True
    num, idx = s, 1
    while chk:
        num = (p * num + q) % m

        if num in A:
            chk = False
            break
        A.append(num)
        idx += 1
    for j in range(idx):
        if num == A[j]:
            jdx = j
            break
    print("#{} {}".format(test_case + 1, idx - jdx))