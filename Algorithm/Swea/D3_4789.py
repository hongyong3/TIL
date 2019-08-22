import sys
sys.stdin = open("D3_4789_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input()))
    count, sum  = 0, 0
    for i in range(len(data)):
        if sum >= i:
            sum += data[i]
        else:
            count += i - sum
            sum = i + data[i]
    print("#{} {}".format(test_case + 1, count))