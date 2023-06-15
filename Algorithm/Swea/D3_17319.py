import sys
sys.stdin = open("D3_17319_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    s = input()
    print("#{} {}".format(test_case + 1, "Yes" if N % 2 == 0 and s[:N // 2] == s[N // 2:] else "No"))