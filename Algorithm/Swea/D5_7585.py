import sys
sys.stdin = open("D5_7585_input.txt", "r")

# input시 Runtime Error...
T = int(input())
for test_case in range(T):
    A, B, N, K = map(int, input().split())
    visited = list(range(1, N + 1))
    count = 0
    for i in range(1, N + 1):
        a = pow(i, A)
        for j in range(1, N + 1):
            if i != j:
                b = pow(j, B)
                if not (a + b) % K:
                    count += 1
    print("#{} {}".format(test_case + 1, count))