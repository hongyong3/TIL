import sys
sys.stdin = open("D3_14692_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = "Bob" if N % 2 else "Alice"
    print("#{} {}".format(test_case + 1, ans))