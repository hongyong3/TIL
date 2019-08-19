import sys
sys.stdin = open("D3_5431_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = set(map(int, input().split()))
    temp = []
    for i in range(N):
        temp.append(i + 1)
    print("#{} ".format(test_case + 1), end="")
    print(*(set(temp) - data))
