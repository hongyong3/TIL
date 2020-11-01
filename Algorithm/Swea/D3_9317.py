import sys
sys.stdin = open("D3_9317_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    s1 = input()
    s2 = input()
    for x, y in zip(s1, s2):
        if x != y:
            N -= 1
    print("#{} {}".format(test_case + 1, N))