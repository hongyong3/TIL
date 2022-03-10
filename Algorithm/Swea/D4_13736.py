import sys
sys.stdin = open("D4_13736_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B, K = map(int, input().split())
    P, Q = min(A, B), max(A, B)
    idx = 1
    arr = []
    while K:
        num = P
        P, Q = P + num, Q - num
        val = min(Q, P)
        if val not in arr:
            arr.append(val)
        else:
            break
        if P > Q:
            P, Q = Q, P
        K -= 1
        idx += 1
    print("#{} {}".format(test_case + 1, arr[K % idx - 1]))