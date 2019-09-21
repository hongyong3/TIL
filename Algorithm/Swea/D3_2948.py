import sys
sys.stdin = open("D3_2948_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    str1 = set(map(str, input().split()))
    str2 = set(map(str, input().split()))
    count = 0
    for i in str2:
        if i in str1:
            count += 1
    print("#{} {}".format(test_case + 1, count))