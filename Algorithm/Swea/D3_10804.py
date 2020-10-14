import sys
sys.stdin = open("D3_10804_input.txt", "r")

T = int(input())
for test_case in range(T):
    s = str.maketrans('bdpq', 'dbqp')
    print("#{} {}".format(test_case + 1, input()[:: - 1].translate(s)))