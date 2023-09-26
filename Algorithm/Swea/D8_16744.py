import sys
sys.stdin = open("D8_16744_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [1] * (N + 1)
    q = [1]
    idx = 2
    while N > 0:
        v = q.pop(0)
        N -= arr[v]
        arr[v] += 1
        q.append(v)
        q.append(idx)
        idx += 1
    print("#{} {}".format(test_case + 1, v))