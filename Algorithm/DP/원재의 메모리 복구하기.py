import sys
sys.stdin = open("원재의 메모리 복구하기_input.txt", "r")
T = int(input())
for test_case in range(1):
    N = list(map(int, input()))
    data = [0] * len(N)
    count = 0
    for i in range(len(data)):
        j = i
        while j < len(N):
            if N[i] == data[i]:
                break
            elif N[i] != data[i]:
                pass
            else:
                data[j] = 1
                j += 1
            count += 1
print(N)
print(data)