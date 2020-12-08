import sys
sys.stdin = open("Battle_116_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    data = list(map(int, input().split()))
    while B:
        data[data.index(min(data))] *= A
        B -= 1
    data.sort()
    for i in range(N):
        data[i] %= 1000000007
    print("#{}".format(test_case + 1), *data)