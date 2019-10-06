import sys
sys.stdin = open("D4_7701_input.txt", "r")

def solve(data):
    return sorted(data, key = lambda x : x[0])

T = int(input())
for test_case in range(T):
    N = int(input())
    # data = []
    # for i in range(N):
    #     data += list(map(str, input().split()))
    data = [list(map(str, input().split())) for _ in range(N)]
    print(data)