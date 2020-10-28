import sys
sys.stdin = open("D3_8658_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    minAns, maxAns = float('inf'), 0

    for i in data:
        temp = 0
        while i:
            temp += i % 10
            i //= 10
        minAns = min(temp, minAns)
        maxAns = max(temp, maxAns)
    print("#{} {} {}".format(test_case + 1, maxAns, minAns))