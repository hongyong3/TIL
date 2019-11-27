import sys
sys.stdin = open("D4_7701_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(set([input() for _ in range(N)])), key = lambda x: (len(x), x))
    print("#{}".format(test_case + 1), *data, sep='\n')