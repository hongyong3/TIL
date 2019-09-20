import sys
sys.stdin = open("D3_2948_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    str1 = list(map(str, input().split()))
    str2 = list(map(str, input().split()))
    count = 0
    for i in str1:
        if i in str2:
            count += 1
    print("#{} {}".format(test_case + 1, count))
    # while True:
    #     if len(str1) == len(str2) == 0: break