import sys
sys.stdin = open("D4_3143_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(str, input().split())
    count = A.count(B)
    A = A.replace(B, "")
    print("#{} {}".format(test_case + 1, count + len(A)))