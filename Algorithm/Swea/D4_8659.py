import sys
sys.stdin = open("D4_8659_input.txt", "r")

gcd = [[0, 0] for _ in range(91)]
gcd[1][0], gcd[1][1] = 2, 1
for i in range(2, 91):
    gcd[i][0], gcd[i][1] = gcd[i - 1][0] + gcd[i - 1][1], gcd[i - 1][0]

T = int(input())
for test_case in range(T):
    K = int(input())
    print("#{}".format(test_case + 1), *gcd[K])